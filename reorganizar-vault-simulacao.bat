@echo off
chcp 65001 > nul
echo.
echo ==========================================
echo  Simulação de reorganização do Will-obsidian
echo ==========================================
echo.
echo Nenhum arquivo será movido neste modo.
echo.
powershell -ExecutionPolicy Bypass -File ".\09-Sistema\scripts\reorganizar-vault.ps1"
echo.
pause
