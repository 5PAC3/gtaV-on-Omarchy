# Context for Next AI Agent - GTA V on Linux

## Mission
Continue working on getting GTA V (Epic Games Legacy Edition) to run on Linux.

## Current Status

### What's DONE ✅
1. **Script launches game**: `launch_gta_manual.sh` works
2. **ucrtbase.dll fix**: `WINEDLLOVERRIDES=ucrtbase=b` solves the _strerror_s error
3. **Heroic bypass**: Game launches without Heroic (Heroic has a bug)
4. **fix.bat**: Correctly configured in game folder
5. **Rockstar Launcher installed**: Already in Wine prefix at `C:\Program Files\Rockstar Games\Launcher\Launcher.exe`

### What's NOT Working ❌
1. **Game requires activation** - Shows "Activation requires an internet connection" error
2. **Offline flags don't work** - Tried -scOfflineOnly, -offline, commandline.txt
3. **Story Mode won't load** - Closes after ~60 seconds

## Solution in Progress

The game needs a **one-time Windows activation**. After that, it should work on Linux.

### Files Already in Place

**On External HDD:**
- Game: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- Prefix: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`
- fix.bat in game folder
- commandline.txt in game folder
- EpicGamesLauncher.exe fake in game folder

### Windows VM Info
- **Access**: http://127.0.0.1:8006/ (noVNC)
- **Username**: teoW
- **Password**: 12345678

## What to Do Next

### Step 1: Activate on Windows
1. Start the Windows VM
2. Install Rockstar Games Launcher (from the game folder or download)
3. Point to the SAME game folder on the external HDD
4. Login with Rockstar account
5. Launch GTA V - it will activate
6. Verify it loads to main menu

### Step 2: Test on Linux
1. Go back to Linux
2. Run: `/tmp/gtaV-on-Omarchy/launch_gta_manual.sh`
3. The game should now work!

## If Windows Activation Works

The game files on the external HDD should now be "activated". The Wine prefix might need the activation data too - if it still doesn't work, we may need to:
- Copy activation files from Windows to Wine prefix
- Or re-install the game on Windows once and copy back

## Key Files

- **Launch script**: `/tmp/gtaV-on-Omarchy/launch_gta_manual.sh`
- **fix.bat**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/fix.bat`
- **Game folder**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- **Wine prefix**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`

## Proton Version
Using **GE-Proton10-34**

## Important Notes

- **GTA Online will NEVER work** - Battleye anti-cheat doesn't support Linux
- **Story Mode should work** - After activation
- **The game was purchased legitimately** - Just needs to be activated
- **Performance on Linux** - Should be fine with Proton/GE-Proton10-34

## Commands for Testing

```bash
# Launch the game
/tmp/gtaV-on-Omarchy/launch_gta_manual.sh

# Kill stuck processes
pkill -f "GTA5|PlayGTAV|Rockstar|Epic|wineserver"
```
