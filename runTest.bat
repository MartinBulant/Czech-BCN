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
    python -m unittest test.test_validator
    python -m unittest test.test_generator
    exit /b 0

:verboseMode
    python -m unittest -v test.test_validator
    python -m unittest -v test.test_generator
    exit /b 0