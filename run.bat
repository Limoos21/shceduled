@echo off
set script_path="C:\Users\Nikita\Documents\GitHub\shceduled\main.py"
set interval=10800 

:loop
python %script_path%
timeout /t %interval% /nobreak > nul
goto loop