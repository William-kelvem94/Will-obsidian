@echo off
chcp 65001 > nul
echo.
echo ==========================================
echo  APLICAR reorganização do Will-obsidian
echo ==========================================
echo.
echo ATENÇÃO: este modo move arquivos e pastas de verdade.
echo Rode primeiro reorganizar-vault-simulacao.bat.
echo.
set /p CONFIRMA="Digite APLICAR para continuar: "
if /I not "%CONFIRMA%"=="APLICAR" (
    echo Operação cancelada.
    pause
    exit /b 0
)

powershell -ExecutionPolicy Bypass -File ".\09-Sistema\scripts\reorganizar-vault.ps1" -Aplicar
echo.
echo Rode agora: git status
echo Depois abra o Obsidian e revise os links.
echo.
pause
