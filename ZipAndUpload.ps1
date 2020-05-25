param(
    [string]$folderToZip="E:\Projects\VS_Projects\CorrectIt\WorkerService.Image.Receiver\bin\Release\netcoreapp3.1",
    [string]$server="182.61.37.221",
    [string]$serverFolder = "Uploads"
)

$sourcePath = Split-Path -Parent $MyInvocation.MyCommand.Definition
$fileName = Split-Path -Path $folderToZip -Leaf
$destination = "$sourcePath\$fileName.zip"

$userName = "sdlfly2000"
$password = "sdl@1215"
$ftp = "ftp://$server/$serverFolder"
$port = 4001    

# Compressing Folder
Compress-Archive -Path "$folderToZip/*" -DestinationPath $destination -Force

# Uploading Zip File to Server
$webClient = New-Object System.Net.WebClient
$webClient.Credentials = New-Object System.Net.NetworkCredential($userName, $password)
$uri = New-Object System.Uri("$ftp/$fileName.zip")
"Uploading to " + $uri.AbsoluteUri
Write-Output $file.FullName
$webclient.UploadFile($uri, $destination)
$webclient.Dispose()

# Unzip files
$commandAction = 0x00,0x03,0x01
$tcpClient = New-Object System.Net.Sockets.TcpClient
$tcpClient.Connect($server, $port)
$stream = $tcpClient.GetStream()
$stream.Write($commandAction,0,3)
$stream.Close()
$tcpClient.Close()

# Restart Server
$commandAction = 0x00,0x03,0x02
$tcpClient = New-Object System.Net.Sockets.TcpClient
$tcpClient.Connect($server, $port)
$stream = $tcpClient.GetStream()
$stream.Write($commandAction,0,3)
$stream.Close()
$tcpClient.Close()