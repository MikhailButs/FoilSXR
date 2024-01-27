@echo off
echo -------------------------------------------------------------------------------- >> errors.log
echo %date% >> errors.log
echo %time% >> errors.log
python mainWindow.py >> errors.log 2>&1