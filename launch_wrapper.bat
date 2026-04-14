start "" "C:\Program Files\Rockstar Games\Launcher\Launcher.exe"
ping -n 5 localhost > nul
start "" "PlayGTAV.exe" -useEpic -fromRGL %*