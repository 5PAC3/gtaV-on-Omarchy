# GTA V (Epic Games) on Linux - Complete Guide

A comprehensive guide to running GTA V (Epic Games Store - Legacy Edition) on Linux using Heroic Games Launcher or direct Proton launch.

## System Specifications

- **Distro**: Arch-based Linux (Omarchy)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores)
- **GPU**: NVIDIA GeForce GTX 1650
- **RAM**: 16 GB
- **Heroic Version**: 2.20.1
- **Proton**: GE-Proton10-34

## Game Details

- **Edition**: LEGACY EDITION
- **Store**: Epic Games
- **Install Location**: `/path/to/heroic/GTAV/`
- **Wine Prefix**: `/path/to/heroic/prefixes`

---

# ✅ WORKING SOLUTION - April 2026

## Problems Solved

### 1. Heroic 2.20.1 Bug
Heroic fails when trying to copy EpicGamesLauncher.exe:
```
ENOENT: copyfile '/opt/Heroic/resources/app.asar.unpacked/build/bin/x64/win32/EpicGamesLauncher.exe' -> ''
```
**Solution**: Bypass Heroic and launch directly with Proton.

### 2. ucrtbase.dll._strerror_s
```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```
**Solution**: Use `WINEDLLOVERRIDES=ucrtbase=b` (built-in, not native DLL).

### 3. Rockstar Launcher Doesn't Detect Game
The Rockstar Games Launcher doesn't detect GTA V and shows "Buy Now".
**Solution**: Use fix.bat to launch GTA5.exe directly after opening PlayGTAV.

### 4. Rockstar Login Modal
After launching, Rockstar Games Launcher shows a login modal.
**Solution**: The fix.bat approach should handle this, but you may need to log in once manually.

---

## Quick Start

### Prerequisites

1. **EpicGamesLauncher.exe fake** - Download from:
   https://github.com/Etaash-mathamsetty/heroic-epic-integration/releases/download/v0.4/EpicGamesLauncher.exe

2. **Place it in your game folder** (next to PlayGTAV.exe)

### Launch Script

```bash
#!/usr/bin/env bash
set -e

# EDIT THESE PATHS FOR YOUR SETUP
export WINEPREFIX="/path/to/heroic/prefixes"
export PROTON_PATH="/home/$USER/.config/heroic/tools/proton/GE-Proton10-34"
export GAME_PATH="/path/to/heroic/GTAV"

export STEAM_COMPAT_DATA_PATH="$WINEPREFIX"
export STEAM_COMPAT_CLIENT_INSTALL_PATH="$HOME/.local/share/steam"
export USE_FAKE_EPIC_EXE=true
export WINEDLLOVERRIDES="ucrtbase=b"

# Setup Rockstar Games Launcher
mkdir -p "$WINEPREFIX/drive_c/Program Files/Rockstar Games/Launcher"
cp "$GAME_PATH/Redistributables/Rockstar-Games-Launcher.exe" "$WINEPREFIX/drive_c/Program Files/Rockstar Games/Launcher/Launcher.exe"

cd "$GAME_PATH"

"$PROTON_PATH/proton" run "fix.bat" "$@"
```

### fix.bat (must be in game folder)

Create a file named `fix.bat` in your game folder with this content:

```bat
start "" EpicGamesLauncher.exe PlayGTAV.exe %*
ping -n 30 localhost > nul
start "" GTA5.exe -useEpic -fromRGL
```

---

## Step-by-Step Installation

### Step 1: Get EpicGamesLauncher.exe Fake

Download from: https://github.com/Etaash-mathamsetty/heroic-epic-integration/releases

Place it in your GTA V game folder (where PlayGTAV.exe is located).

### Step 2: Create fix.bat

Create `fix.bat` in your game folder with the content shown above.

### Step 3: Create Launch Script

Save the launch script above as `launch_gta.sh` and make it executable:
```bash
chmod +x launch_gta.sh
```

Edit the paths to match your setup:
- `WINEPREFIX`: Your Wine prefix path
- `PROTON_PATH`: Path to GE-Proton10-34
- `GAME_PATH`: Path to GTA V installation

### Step 4: First Launch

1. Run the script: `./launch_gta.sh`
2. The Rockstar Games Launcher will open
3. **Log in with your Rockstar Social Club account** (only needed once)
4. After logging in, the game should launch automatically

If the game doesn't launch after login, run the script again.

### Step 5: Enjoy!

The game should now launch directly without the Rockstar login modal on subsequent runs.

---

## Configuration Details

### Environment Variables

```bash
WINEDLLOVERRIDES=ucrtbase=b    # Fixes _strerror_s error
USE_FAKE_EPIC_EXE=true        # Enables fake Epic exe
STEAM_COMPAT_DATA_PATH        # Wine prefix path
STEAM_COMPAT_CLIENT_INSTALL_PATH  # Steam path (required by Proton)
```

### Why This Works

1. **EpicGamesLauncher.exe fake**: Simulates the Epic Games Launcher
2. **PlayGTAV.exe**: Launcher that triggers Rockstar Games Launcher
3. **Wait 30 sec**: Gives time for Rockstar Launcher to initialize
4. **GTA5.exe**: Launches the game directly with Epic flags
5. **WINEDLLOVERRIDES=ucrtbase=b**: Fixes the ucrtbase.dll._strerror_s error

---

## Troubleshooting

### Game Won't Start

- Make sure all paths in the script are correct
- Verify EpicGamesLauncher.exe is in the game folder
- Check that fix.bat has correct line endings (CRLF for Windows)

### Rockstar Login Modal Appears Every Time

- Log in manually once during the first launch
- The credentials should be saved for future launches

### "ucrtbase.dll._strerror_s" Error

- Make sure `WINEDLLOVERRIDES=ucrtbase=b` is set
- The `b` means "built-in" - use Wine's internal implementation

### Game Shows "Buy Now" in Rockstar Launcher

- This is handled by fix.bat launching GTA5.exe directly
- Make sure fix.bat is in the correct location

---

## Proton Versions Tested

| Version | Result | Notes |
|---------|--------|-------|
| GE-Proton9-25, 9-26, 9-27 | ❌ | `ucrtbase.dll._strerror_s` unimplemented |
| GE-Proton10-30 | ✅ | Works with WINEDLLOVERRIDES=ucrtbase=b |
| GE-Proton10-34 | ✅ | Works with WINEDLLOVERRIDES=ucrtbase=b |
| Proton-EM-10.0-34 | ❌ | Still unimplemented |

---

## Limitations

- **GTA Online**: ❌ Does NOT work (Battleye anti-cheat - no Linux support)
- **Story Mode**: ✅ Works perfectly

---

## Credits & References

- Original Wine bug: https://bugs.winehq.org/show_bug.cgi?id=50031
- ProtonGE: https://github.com/GloriousEggroll/proton-ge-custom
- Epic Integration: https://github.com/Etaash-mathamsetty/heroic-epic-integration
- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games
- Discord Support: https://discord.gg/HeroicGC

---

## Changelog

- **April 15, 2026**: Complete working solution
  - Heroic bypassed with manual script
  - fix.bat to launch game directly
  - WINEDLLOVERRIDES=ucrtbase=b

- **April 14, 2026**: Discovered ucrtbase.dll error
  - Compiled native DLL (didn't work)
  - Found fix with built-in DLL

- **April 13, 2026**: Identified Heroic 2.20.1 bug
  - CopyFile fails with empty path
