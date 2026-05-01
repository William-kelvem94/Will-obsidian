# vault_merge.ps1
# Mescla D:\OBSIDIAN\Will com vault atual, mantendo versoes mais recentes

param(
    [string]$SourcePath = "D:\OBSIDIAN\Will",
    [string]$TargetPath = "C:\Users\willi\Documents\GitHub\Will-obsidian",
    [switch]$DryRun = $true,
    [switch]$Verbose = $false
)

# Cores para output
$ColorInfo = "Cyan"
$ColorSuccess = "Green"
$ColorWarning = "Yellow"
$ColorError = "Red"

# Estatisticas
$stats = @{
    FilesAnalyzed = 0
    FilesSkipped = 0
    FilesCopied = 0
    FilesNewer = 0
    FilesConflict = 0
    FilesError = 0
}

function Write-Status {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

function Get-RelativePath {
    param([string]$FullPath, [string]$BasePath)
    return $FullPath.Replace($BasePath, "").TrimStart('\')
}

function Compare-FileContent {
    param([string]$File1, [string]$File2)
    
    if (-not (Test-Path $File1) -or -not (Test-Path $File2)) {
        return $false
    }
    
    $hash1 = (Get-FileHash -Path $File1 -Algorithm MD5).Hash
    $hash2 = (Get-FileHash -Path $File2 -Algorithm MD5).Hash
    
    return $hash1 -eq $hash2
}

Write-Status "`n[*] VAULT MERGE ANALYSIS" $ColorInfo
Write-Status ("=" * 60) $ColorInfo
Write-Status "Source: $SourcePath"
Write-Status "Target: $TargetPath"
Write-Status ("Mode: " + $(if ($DryRun) { "DRY RUN (no changes)" } else { "LIVE (will make changes)" }))
Write-Status ("=" * 60) $ColorInfo

# Verificar se pastas existem
if (-not (Test-Path $SourcePath)) {
    Write-Status "`n[ERROR] Source path not found: $SourcePath" $ColorError
    exit 1
}

if (-not (Test-Path $TargetPath)) {
    Write-Status "`n[ERROR] Target path not found: $TargetPath" $ColorError
    exit 1
}

# Arrays para relatorios
$filesToCopy = @()
$filesNewer = @()
$filesConflict = @()
$filesIdentical = @()
$filesError = @()

# Obter todos os arquivos markdown e canvas do source
$sourceFiles = Get-ChildItem -Path $SourcePath -Recurse -File | Where-Object {
    $_.Extension -in @('.md', '.canvas') -and
    $_.FullName -notlike "*\.obsidian\*" -and
    $_.FullName -notlike "*\.git\*"
}

Write-Status ("`n[*] Analyzing " + $sourceFiles.Count + " files...") $ColorInfo

foreach ($sourceFile in $sourceFiles) {
    $stats.FilesAnalyzed++
    
    $relativePath = Get-RelativePath -FullPath $sourceFile.FullName -BasePath $SourcePath
    $targetFile = Join-Path -Path $TargetPath -ChildPath $relativePath
    
    if ($Verbose) {
        Write-Status ("`nAnalyzing: " + $relativePath)
    }
    
    try {
        # Caso 1: Arquivo nao existe no target - COPIAR
        if (-not (Test-Path $targetFile)) {
            $filesToCopy += @{
                Source = $sourceFile.FullName
                Target = $targetFile
                RelativePath = $relativePath
                Size = $sourceFile.Length
                Modified = $sourceFile.LastWriteTime
            }
            
            if ($Verbose) {
                Write-Status "  -> NEW FILE (will copy)" $ColorSuccess
            }
        }
        # Caso 2: Arquivo existe - COMPARAR
        else {
            $targetFileInfo = Get-Item $targetFile
            
            # Verificar se conteudo e identico
            $isIdentical = Compare-FileContent -File1 $sourceFile.FullName -File2 $targetFile
            
            if ($isIdentical) {
                $filesIdentical += $relativePath
                $stats.FilesSkipped++
                
                if ($Verbose) {
                    Write-Status "  -> IDENTICAL (skip)" $ColorInfo
                }
            }
            else {
                # Arquivos diferentes - comparar timestamps
                $sourceDiff = ($sourceFile.LastWriteTime - $targetFileInfo.LastWriteTime).TotalSeconds
                
                # Source e mais recente (>60s diferenca)
                if ($sourceDiff -gt 60) {
                    $filesNewer += @{
                        RelativePath = $relativePath
                        SourceModified = $sourceFile.LastWriteTime
                        TargetModified = $targetFileInfo.LastWriteTime
                        DiffSeconds = [math]::Round($sourceDiff)
                        Source = $sourceFile.FullName
                        Target = $targetFile
                    }
                    
                    $stats.FilesNewer++
                    
                    if ($Verbose) {
                        Write-Status ("  -> SOURCE NEWER (source: " + $sourceFile.LastWriteTime + ", target: " + $targetFileInfo.LastWriteTime + ")") $ColorWarning
                    }
                }
                # Target e mais recente ou timestamps similares
                else {
                    $filesConflict += @{
                        RelativePath = $relativePath
                        SourceModified = $sourceFile.LastWriteTime
                        TargetModified = $targetFileInfo.LastWriteTime
                        DiffSeconds = [math]::Round($sourceDiff)
                        Source = $sourceFile.FullName
                        Target = $targetFile
                    }
                    
                    $stats.FilesConflict++
                    
                    if ($Verbose) {
                        Write-Status "  -> CONFLICT (manual review needed)" $ColorError
                    }
                }
            }
        }
    }
    catch {
        $filesError += @{
            RelativePath = $relativePath
            Error = $_.Exception.Message
        }
        $stats.FilesError++
        Write-Status ("  [ERROR] " + $_.Exception.Message) $ColorError
    }
}

# RELATORIO DETALHADO
Write-Status "`n`n[*] MERGE REPORT" $ColorInfo
Write-Status ("=" * 60) $ColorInfo

Write-Status "`n[*] Statistics:"
Write-Status ("  Files analyzed: " + $stats.FilesAnalyzed)
Write-Status ("  Files identical (skipped): " + $stats.FilesSkipped) $ColorInfo
Write-Status ("  New files to copy: " + $filesToCopy.Count) $ColorSuccess
Write-Status ("  Files newer in source: " + $filesNewer.Count) $ColorWarning
Write-Status ("  Conflicts (manual review): " + $filesConflict.Count) $ColorError
Write-Status ("  Errors: " + $stats.FilesError) $ColorError

# Novos arquivos
if ($filesToCopy.Count -gt 0) {
    Write-Status ("`n[+] NEW FILES TO COPY (" + $filesToCopy.Count + "):") $ColorSuccess
    foreach ($file in $filesToCopy) {
        Write-Status ("  - " + $file.RelativePath)
        Write-Status ("    Modified: " + $file.Modified)
    }
}

# Arquivos mais recentes no source
if ($filesNewer.Count -gt 0) {
    Write-Status ("`n[!] SOURCE FILES NEWER (" + $filesNewer.Count + "):") $ColorWarning
    foreach ($file in $filesNewer) {
        Write-Status ("  - " + $file.RelativePath)
        Write-Status ("    Source:  " + $file.SourceModified)
        Write-Status ("    Target:  " + $file.TargetModified)
        Write-Status ("    Diff:    " + $file.DiffSeconds + " seconds")
    }
}

# Conflitos
if ($filesConflict.Count -gt 0) {
    Write-Status ("`n[X] CONFLICTS (manual review needed) (" + $filesConflict.Count + "):") $ColorError
    foreach ($file in $filesConflict) {
        Write-Status ("  - " + $file.RelativePath)
        Write-Status ("    Source:  " + $file.SourceModified)
        Write-Status ("    Target:  " + $file.TargetModified)
        Write-Status ("    Diff:    " + $file.DiffSeconds + " seconds (target is newer or similar)")
    }
}

# Erros
if ($filesError.Count -gt 0) {
    Write-Status ("`n[ERROR] (" + $filesError.Count + "):") $ColorError
    foreach ($file in $filesError) {
        Write-Status ("  - " + $file.RelativePath)
        Write-Status ("    Error: " + $file.Error)
    }
}

# EXECUTAR MERGE (se nao for DryRun)
if (-not $DryRun) {
    Write-Status "`n`n[*] EXECUTING MERGE..." $ColorInfo
    
    $backupDir = Join-Path -Path $TargetPath -ChildPath (".backups\merge-" + (Get-Date -Format 'yyyy-MM-dd-HHmmss'))
    
    # Copiar novos arquivos
    foreach ($file in $filesToCopy) {
        try {
            $targetDir = Split-Path -Path $file.Target -Parent
            if (-not (Test-Path $targetDir)) {
                New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
            }
            
            Copy-Item -Path $file.Source -Destination $file.Target -Force
            Write-Status ("  [+] Copied: " + $file.RelativePath) $ColorSuccess
            $stats.FilesCopied++
        }
        catch {
            Write-Status ("  [ERROR] Failed to copy " + $file.RelativePath + ": " + $_.Exception.Message) $ColorError
        }
    }
    
    # Copiar arquivos mais recentes (com backup)
    foreach ($file in $filesNewer) {
        try {
            # Backup do arquivo atual
            $backupFile = Join-Path -Path $backupDir -ChildPath $file.RelativePath
            $backupFileDir = Split-Path -Path $backupFile -Parent
            
            if (-not (Test-Path $backupFileDir)) {
                New-Item -ItemType Directory -Path $backupFileDir -Force | Out-Null
            }
            
            Copy-Item -Path $file.Target -Destination $backupFile -Force
            
            # Copiar versao mais recente
            Copy-Item -Path $file.Source -Destination $file.Target -Force
            Write-Status ("  [+] Updated (backup created): " + $file.RelativePath) $ColorSuccess
            $stats.FilesCopied++
        }
        catch {
            Write-Status ("  [ERROR] Failed to update " + $file.RelativePath + ": " + $_.Exception.Message) $ColorError
        }
    }
    
    Write-Status ("`n[+] Merge completed! Files copied/updated: " + $stats.FilesCopied) $ColorSuccess
    if (Test-Path $backupDir) {
        Write-Status ("[*] Backups saved to: " + $backupDir) $ColorInfo
    }
}
else {
    Write-Status "`n`n[*] DRY RUN MODE - No changes made" $ColorWarning
    Write-Status "[*] Run with -DryRun:`$false to execute merge" $ColorWarning
}

Write-Status "`n"

# Exportar relatorio JSON
$reportPath = Join-Path -Path $TargetPath -ChildPath ".scripts\vault_merge_report.json"
$report = @{
    Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    Statistics = $stats
    NewFiles = $filesToCopy
    NewerFiles = $filesNewer
    Conflicts = $filesConflict
    Errors = $filesError
}

$report | ConvertTo-Json -Depth 10 | Out-File -FilePath $reportPath -Encoding UTF8
Write-Status ("[*] Full report saved to: " + $reportPath) $ColorInfo
