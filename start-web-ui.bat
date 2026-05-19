@echo off
echo.
echo ========================================
echo   Will-obsidian — Interface Web de Busca
echo ========================================
echo.
echo Iniciando servidor em http://localhost:8080
echo Pressione Ctrl+C para parar.
echo.
python -m http.server 8080 -d "%~dp0web-ui"
pause
