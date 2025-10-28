@echo off
title Sistema Tikler
color 0A
echo ========================================
echo    RECRIANDO AMBIENTE VIRTUAL
echo ========================================
echo.

cd /d C:\Users\josericardo\Desktop\PIM2SE~1

:: Remover venv corrompida se existir
if exist ".venv" (
    echo Removendo venv corrompida...
    rmdir /s /q .venv
)

:: Criar nova venv
echo Criando nova venv...
python -m venv .venv

:: Ativar e instalar pillow
echo Instalando dependencias...
call .venv\Scripts\activate.bat
pip install pillow

:: Executar aplicativo
echo.
echo Executando aplicativo...
python PROJETO_TKINTER\tikler.py

pause