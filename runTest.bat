@echo off

echo  Test - Runnig 
python -m unittest discover -s tests .

IF %ERRORLEVEL% EQU 0 (
    echo Test - Done
) ELSE (
    echo Something went wrong.
)
