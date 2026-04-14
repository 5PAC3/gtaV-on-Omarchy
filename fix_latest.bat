start /B ""null"" PlayGTAV.exe %*
ping -n 30 localhost > nul
start "" EpicGamesLauncher.exe PlayGTAV.exe %*