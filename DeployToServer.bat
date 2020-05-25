@echo off

REM Zip Files
Powershell.exe -ExecutionPolicy Bypass -Command %~dp0ZipAndUpload.ps1 -folderToZip "E:\Projects\VS_Projects\CorrectIt\WorkerService.Image.Receiver\bin\Release\netcoreapp3.1" -server "182.61.37.221" -serverFolder "Uploads"

@echo on
pause