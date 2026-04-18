# GTA V (Epic Games) on Linux - Complete Guide

A comprehensive guide to running GTA V (Epic Games Store - Legacy Edition) on Linux.

## System Specifications

- **Distro**: Omarchy (Arch-based Linux)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores)
- **GPU**: NVIDIA GeForce GTX 1650
- **RAM**: 16 GB
- **Heroic Version**: 2.20.1
- **Proton**: GE-Proton10-34

## Game Details

- **Edition**: LEGACY EDITION
- **Store**: Epic Games (purchased legitimately)
- **Install Location**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- **Wine Prefix**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`

---

# ⚠️ CURRENT STATUS: NEEDS WINDOWS ACTIVATION

## What's Working ✅

1. **Game launches** - GTA5.exe starts without crashing
2. **No more _strerror_s error** - WINEDLLOVERRIDES=ucrtbase=b fixes this
3. **Heroic bypass works** - Can launch game directly with Proton
4. **fix.bat works** - Launches game through Rockstar Launcher

## What's NOT Working ❌

1. **Activation required** - Game requires online activation on Windows
2. **Rockstar Launcher rendering issues** - UI doesn't render correctly in Wine
3. **Story Mode requires activation** - Cannot be completed in Wine

---

# QUICK START (After Windows Activation)

### Launch Script

```bash
/tmp/gtaV-on-Omarchy/launch_gta_manual.sh
```

Or copy to your local bin:
```bash
cp /tmp/gtaV-on-Omarchy/launch_gta_manual.sh ~/.local/bin/launch_gta.sh
chmod +x ~/.local/bin/launch_gta.sh
~/.local/bin/launch_gta.sh
```

---

# FILES IN THIS REPO

### launch_gta_manual.sh
Main launch script. Located at: `/tmp/gtaV-on-Omarchy/launch_gta_manual.sh`

### fix.bat
Must be in the game folder. Content:
```bat
@echo off
start "" "C:\Program Files\Rockstar Games\Launcher\Launcher.exe" -skipPatcherCheck -epicAppId=gta5 -useEpic -fromRGL -offline
ping -n 30 localhost > nul
start "" GTA5.exe -scOfflineOnly -offline
```

### commandline.txt
Located in game folder, content:
```
-scOfflineOnly -offline
```

---

# PROBLEMS SOLVED

## 1. Heroic 2.20.1 Bug - FIXED ✅

**Problem**: Heroic fails copying EpicGamesLauncher.exe
```
ENOENT: copyfile '.../EpicGamesLauncher.exe' -> ''
```

**Solution**: Use launch_gta_manual.sh to bypass Heroic

## 2. ucrtbase.dll._strerror_s - FIXED ✅

**Problem**:
```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```

**Solution**: Use `WINEDLLOVERRIDES=ucrtbase=b`

## 3. Rockstar Launcher - FIXED ✅

**Problem**: Launcher doesn't detect GTA V

**Solution**: fix.bat launches directly with correct paths

---

# NEXT STEP: WINDOWS ACTIVATION

## Why Windows is Needed

GTA V requires **initial online activation** to verify the license. This cannot be completed in Wine/Proton because:
1. Social Club connection fails in Wine
2. Offline mode flags don't work
3. Rockstar Launcher doesn't render correctly

## Solution: One-time Windows Activation

### What to do in Windows VM:

1. **Install Rockstar Games Launcher**
   - Download from: https://socialclub.rockstargames.com/
   - Or use the installer from: `GTAV/Redistributables/Rockstar-Games-Launcher.exe`

2. **Make sure GTA V is detected**
   - Point the installer to the same game folder on the external HDD
   - Path: `E:\heroic\GTAV\` (or wherever your GTAV folder is)

3. **Login to Rockstar Social Club**
   - Use your account (same as on Epic Games)

4. **Launch GTA V**
   - The game will complete activation automatically
   - You'll see it loads into the main menu

5. **Done!**
   - Close Windows, go back to Linux
   - The activation should now work on Linux

### Files that get created/modified:

After activation on Windows, these files will contain the activation data:
- Game folder: `GTAV/` (some config files)
- User folder: `C:\Users\teoW\AppData\Local\Rockstar Games\`
- User folder: `C:\Users\teoW\Documents\Rockstar Games\`

---

# ENVIRONMENT VARIABLES REQUIRED

```bash
WINEDLLOVERRIDES="ucrtbase=b"       # Fixes _strerror_s error
USE_FAKE_EPIC_EXE=true              # Uses fake Epic exe
STEAM_COMPAT_DATA_PATH              # Wine prefix path
STEAM_COMPAT_CLIENT_INSTALL_PATH    # Required by Proton
```

---

# PROTON VERSIONS TESTED

| Version | Result | Notes |
|---------|--------|-------|
| GE-Proton9-25, 9-26, 9-27 | ❌ | `ucrtbase.dll._strerror_s` unimplemented |
| GE-Proton10-30 | ✅ | Works with WINEDLLOVERRIDES=ucrtbase=b |
| GE-Proton10-34 | ✅ | Current version used |
| Proton-EM-10.0-34 | ❌ | Still unimplemented |

---

# LIMITATIONS

- **GTA Online**: ❌ Does NOT work (Battleye anti-cheat - no Linux support)
- **Story Mode**: ⚠️ Works after Windows activation

---

# CREDITS & REFERENCES

- Original Wine bug: https://bugs.winehq.org/show_bug.cgi?id=50031
- ProtonGE: https://github.com/GloriousEggroll/proton-ge-custom
- Epic Integration: https://github.com/Etaash-mathamsetty/heroic-epic-integration
- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games

---

# CHANGELOG

- **April 18, 2026**: Additional attempts to bypass activation
  - Tried Faugus wine prefix (instead of Heroic default)
  - Rockstar Launcher works but game still requires authentication session
  - Tried registry entries, symlinks, same-session launch - all failed
  - Game sees launcher as separate process, not authenticated session
  - Root cause: game validates session via Rockstar server

- **April 15, 2026**: Complete working solution (waiting for Windows activation)
  - Heroic bypassed with manual script
  - fix.bat launches game through Rockstar Launcher
  - WINEDLLOVERRIDES=ucrtbase=b

- **April 15, 2026**: Documented current status
  - Game launches but requires activation
  - Rockstar Launcher has rendering issues
  - Activation cannot be completed in Wine

- **April 14, 2026**: Discovered ucrtbase.dll error
  - Compiled native DLL (didn't work)
  - Found fix with built-in DLL

- **April 13, 2026**: Identified Heroic 2.20.1 bug
  - CopyFile fails with empty path
