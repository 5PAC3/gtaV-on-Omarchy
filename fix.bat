@echo off
start "" "C:\Program Files\Rockstar Games\Launcher\Launcher.exe" -skipPatcherCheck -epicAppId=gta5 -useEpic -fromRGL -offline
ping -n 30 localhost > nul
start "" GTA5.exe -scOfflineOnly -offline
