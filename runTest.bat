@echo off

echo  Test - Runnig 

IF "%1"=="-v" (
    call :verboseMode
) ELSE (
    call :classicMode
)



IF %ERRORLEVEL% EQU 0 (
    echo Test - Done
) ELSE (
    echo Something went wrong.
)



exit /b 0
:classicMode
    python -m unittest
    exit /b 0

:verboseMode
    python -m unittest -v
    exit /b 0