$pythonversion = python -V
$wingetversion = winget -v

if ($pythonversion -ne $null) {

    if (Test-Path .\oauth.json -PathType Leaf) {
        Write-Output "file exists, proceding to script"
        .\Scripts\python.exe .\script.py
    }

    else {
        .\Scripts\ytmusicapi.exe oauth
    }
}

else {
    Write-Output "python is not installed"
    if ($wingetversion -ne $null) {
        Write-Output "Winget found! Proceding with python installation!"
        winget install python
    }

    else {
        Write-Output "Could not find python or winget to install it! Install python and run the script again!"
    }
}