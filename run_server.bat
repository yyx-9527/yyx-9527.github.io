@echo off
setlocal
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python 3.10 or later is required for this Windows preview launcher.
  exit /b 1
)
python scripts\preview.py
