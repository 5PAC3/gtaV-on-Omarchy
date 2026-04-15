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

# ⚠️ CURRENT STATUS: PARTIALLY WORKING

## What's Working ✅

1. **Game launches** - GTA5.exe starts without crashing
2. **No more _strerror_s error** - WINEDLLOVERRIDES=ucrtbase=b fixes this
3. **Heroic bypass works** - Can launch game directly with Proton
4. **fix.bat works** - Launches game through the chain Epic -> PlayGTAV -> GTA5

## What's NOT Working ❌

1. **Activation required** - Game requires internet connection to activate
2. **Rockstar Launcher rendering issues** - Launcher shows blank/blank with black borders
3. **Social Club authentication** - Cannot complete online verification

---

# Quick Start (Partial Solution)

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
start "" GTA5.exe
```

### commandline.txt (for offline mode attempt)

Create a file named `commandline.txt` in your game folder:

```
-scOfflineOnly
```

---

## Problems & Solutions Attempted

### 1. Heroic 2.20.1 Bug ❌ FIXED

Heroic fails when trying to copy EpicGamesLauncher.exe:
```
ENOENT: copyfile '.../EpicGamesLauncher.exe' -> ''
```
**Solution**: Bypass Heroic and launch directly with Proton.

### 2. ucrtbase.dll._strerror_s ❌ FIXED

```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```
**Solution**: Use `WINEDLLOVERRIDES=ucrtbase=b` (built-in, not native DLL).

### 3. Rockstar Launcher Doesn't Detect Game ❌ FIXED (Workaround)

The Rockstar Games Launcher doesn't detect GTA V and shows "Buy Now".
**Solution**: Use fix.bat to launch GTA5.exe directly after opening PlayGTAV.

### 4. Activation Required ❌ NOT FIXED

```
Activation requires an internet connection and you are currently in offline mode.
Your offline activation data could not be loaded.
```

**Attempted solutions**:
- Tried `-scOfflineOnly` flag - doesn't work
- Tried `commandline.txt` with `-scOfflineOnly` - doesn't work
- Tried launching Rockstar Launcher directly for login - Launcher renders blank

**Cause**: GTA V requires initial online activation to verify license. Wine/Proton cannot complete this verification.

### 5. Rockstar Launcher Rendering ❌ NOT FIXED

The Rockstar Games Launcher shows a blank window or window with black borders.
**Cause**: Unknown - possibly Wine graphics/UI rendering issues.

---

## Troubleshooting

### Game Won't Start

- Make sure all paths in the script are correct
- Verify EpicGamesLauncher.exe is in the game folder
- Check that fix.bat has correct line endings (CRLF for Windows)

### "ucrtbase.dll._strerror_s" Error

- Make sure `WINEDLLOVERRIDES=ucrtbase=b` is set
- The `b` means "built-in" - use Wine's internal implementation

### Activation Required Error

This is a known limitation. The game requires online activation which cannot be completed in Wine/Linux.
- The game has been purchased legitimately
- Activation server connection may be blocked or not working in Wine

---

## Proton Versions Tested

| Version | Result | Notes |
|---------|--------|-------|
| GE-Proton9-25, 9-26, 9-27 | ❌ | `ucrtbase.dll._strerror_s` unimplemented |
| GE-Proton10-30 | ✅ | Works with WINEDLLOVERRIDES=ucrtbase=b |
| GE-Proton10-34 | ✅ | Works with WINEDLLOVERRIDES=ucrtbase=b |
| Proton-EM-10.0-34 | ❌ | Still unimplemented |

---

## Known Issues

1. **Initial online activation required** - Cannot be bypassed in current Wine version
2. **Rockstar Launcher UI issues** - Blank/black rendering in Wine
3. **Story Mode requires activation** - Even single-player needs online verification

---

## Future Debugging Ideas

1. Try older Proton version (GE-Proton9-27)
2. Try different Wine prefix settings
3. Check if activation works on Windows (then copy activation files)
4. Try VPN to bypass connection issues
5. Check Wine registry for activation data

---

## Limitations

- **GTA Online**: ❌ Does NOT work (Battleye anti-cheat - no Linux support)
- **Story Mode**: ⚠️ Requires online activation (not yet working)

---

## Credits & References

- Original Wine bug: https://bugs.winehq.org/show_bug.cgi?id=50031
- ProtonGE: https://github.com/GloriousEggroll/proton-ge-custom
- Epic Integration: https://github.com/Etaash-mathamsetty/heroic-epic-integration
- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games
- Discord Support: https://discord.gg/HeroicGC
- GTA Offline Mode: https://achivx.com/how-to-launch-gta-5-in-offline-mode/

---

## Changelog

- **April 15, 2026**: Documented current status
  - Game launches but requires activation
  - Rockstar Launcher has rendering issues
  - Activation cannot be completed in Wine

- **April 15, 2026**: Complete working solution (initial)
  - Heroic bypassed with manual script
  - fix.bat to launch game directly
  - WINEDLLOVERRIDES=ucrtbase=b

- **April 14, 2026**: Discovered ucrtbase.dll error
  - Compiled native DLL (didn't work)
  - Found fix with built-in DLL

- **April 13, 2026**: Identified Heroic 2.20.1 bug
  - CopyFile fails with empty path
