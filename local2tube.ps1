$version = python -V

if ($version -ne $null) {

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
}