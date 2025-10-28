@echo off
title Sistema Tikler
color 0A
echo ========================================
echo    INICIANDO SISTEMA TIKLER
echo ========================================
echo.

:: Navegar para o projeto
cd /d C:\Users\josericardo\Desktop\PIM2SE~1\PROJETO_TKINTER
echo Diretorio: %CD%
echo.

:: Verificar e instalar Pillow se necessário
echo Verificando Pillow...
python -c "import PIL" 2>nul
if errorlevel 1 (
    echo Instalando Pillow...
    pip install pillow
    echo.
) else (
    echo Pillow ja instalado!
    echo.
)

:: Executar o aplicativo (usará os JSON do projeto)
echo ========================================
echo    EXECUTANDO APLICATIVO
echo ========================================
echo.
python tikler.py

echo.
echo ========================================
echo    SISTEMA FINALIZADO
echo ========================================
echo.
pause