@echo off
title Sistema Tikler
color 0A
echo ========================================
echo    INICIANDO SISTEMA TIKLER
echo ========================================
echo.

:: Caminhos principais (usando PIM2SE~1)
set "PROJ_DIR=C:\Users\josericardo\Desktop\PIM2SE~1\PROJETO_TKINTER"
set "JSON_DIR=C:\Users\josericardo\Desktop\PIM2SE~1"

cd /d "%PROJ_DIR%"
echo Diretorio do projeto: %PROJ_DIR%
echo Diretorio dos JSONs: %JSON_DIR%
echo.

:: Verificar se os JSONs obrigatórios existem
set "JSON1=usuarios.json"
set "JSON2=alunos.json"
set "JSON3=notas.json"
set "JSON4=disciplinas.json"  ;;* CORREÇÃO AQUI *;;

echo Verificando arquivos JSON...
for %%F in (%JSON1% %JSON2% %JSON3% %JSON4%) do (
    if not exist "%JSON_DIR%\%%F" (
        echo ERRO: O arquivo %%F NAO FOI ENCONTRADO em "%JSON_DIR%"
        echo O sistema requer que todos os JSON ja existam.
        echo.
        pause
        exit /b
    )
)
echo Todos os arquivos JSON foram encontrados!
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

:: Executar o aplicativo passando o caminho dos JSONs como argumento
echo ========================================
echo    EXECUTANDO APLICATIVO
echo ========================================
echo.
python tikler.py "%JSON_DIR%"

echo.
echo ========================================
echo    SISTEMA FINALIZADO
echo ========================================
echo.
pause