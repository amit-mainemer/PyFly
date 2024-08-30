@echo off
:: Load the .env file and set environment variables
for /f "tokens=1,2 delims==" %%a in (".env") do (
    set %%a=%%b
)

:: Call the Python script (or any other script)
python app.py
