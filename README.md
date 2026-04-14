# GTA V on Linux (Omarchy/Heroic)

Repository to document and solve the issue of running GTA V (Windows/Epic Games version) on Linux using Heroic Games Launcher.

## IMPORTANT: Edition

**We are using GTA V LEGACY EDITION (Standard)**, NOT the Enhanced Edition. The Enhanced Edition is known to have significantly more issues on Linux/Wine/Proton.

## Current Status

**UNSOLVED** - The game currently does not launch.

## System Specifications

- **Distro**: Omarchy (Arch-based)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores) @ 4.30 GHz
- **GPU**: NVIDIA GeForce GTX 1650 [Discrete]
- **RAM**: 79.84 GiB / 230.87 GiB (35%)
- **Heroic Version**: 2.14.1

## What Has Been Tried

### 1. Rockstar Games Launcher Issues
- The Rockstar Games Launcher is required by GTA V (Epic version)
- The launcher shows errors:
  - "An error has occurred. Please make sure all instances of the Rockstar Games Launcher have been closed"
  - "Unable to install prerequisites, please try reinstalling the game"
  - CEF browser crash: "The CEF browser for the Rockstar Games Launcher crashed and could not restart"
  - "A newer version of the Rockstar Games Launcher is already installed, exiting installer"

### 2. Error: Path Not Found
This is the most common and blocking error. Wine drive paths (V:\...) don't match expected Windows paths. The working directory when .bat scripts run from Heroic/Proton is different than expected.

### 3. Proton Versions Tested
- GE-Proton-latest - Various issues
- GE-Proton9-26 - Path not found error
- GE-Proton9-25-GTA (with GTA patch) - Path not found error
- GE-Proton9-27 - Various issues

### 4. Fixes Attempted (Chronological Order)

| File | Description | Result |
|------|------------|--------|
| `fix.bat` | Initial attempt with PlayGTAV.exe -useEpic -fromRGL | Path not found |
| `launch_wrapper.bat` | Launch launcher first, then game | Launcher install issues |
| `fix_latest.bat` | Alternative ordering with ping delay | Various errors |
| `launch_heroic.py` | Python wrapper attempt | Not tested |

#### Environment Variables Tried
```json
"USE_FAKE_EPIC_EXE": "true"
"PROTON_NO_NTSYNC": "1"
"SteamDeck": "1"
"WINEDLLOVERRIDES": "dxgi=n"
```

### 5. Configuration Changes
- Disabled DXVK/VKD3D (force wined3d)
- Disabled Esync/Fsync
- Changed winePrefix path

### 6. Manual Installation Attempts
- Extracted Rockstar Games Launcher to prefix using bsdtar
- Attempted wine64 installation of launcher
- Copied files from Redistributables folder

## Known Problems

1. **Path Not Found Error**: The most common error - working directory issues
2. **Win32 Path Issues**: Wine drive paths (V:\...) don't match expected Windows paths
3. **Launcher Crashes**: CEF browser in Rockstar Launcher crashes
4. **GTA Requires Launcher**: Game refuses to start without Rockstar Games Launcher

## Potential Solutions to Try

### 1. Absolute Paths in .bat Files
Instead of relative paths like `PlayGTAV.exe`, try using the full Windows-style path with the drive letter Proton assigns:

```batch
C:\Program Files (x86)\Epic Games\GTAV\PlayGTAV.exe -EpicPortal
```

or if using an external library, the path might be like:
```batch
E:\GTAV\PlayGTAV.exe -EpicPortal
```

### 2. Try Lutris (Recommended Alternative)
Lutris has better built-in support for Epic Games Launcher and GTA V. The Lutris installer for GTA V (Epic) often includes installation scripts that more robustly handle the Rockstar Games Launcher and dependencies (Visual C++ Redistributables) directly in the Wine prefix.

### 3. Re-authenticate with Epic
Some users reported that:
1. Updated Heroic
2. Clear cache
3. Re-authenticate with Epic through Heroic
4. Re-authenticate with Rockstar Launcher

Then the game worked.

## Workarounds

1. **Use Steam Version**: The original repo was designed for Steam version which works better with Proton
2. **Try Lutris**: Some users report Lutris works better for Rockstar games
3. **Wine System Install**: Try installing Wine system-wide and running launcher outside Proton

## Help Needed

If you've solved running GTA V (Legacy) on Linux with Epic + Heroic, please open an issue or PR with your solution.

### Questions to Solve
1. How to properly install Rockstar Games Launcher in Proton prefix?
2. How to make GTA V accept the Epic credentials without launcher?
3. What is the correct working directory for .bat scripts in Heroic/Proton?

## References

- Original Guide: https://github.com/shuvozula/steam-gta5-linux
- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki
- GTA V Enhanced on Linux: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games
- Proton-GE Custom: https://github.com/GloriousEggroll/proton-ge-custom
- telqor GTA patch: https://github.com/telqor/proton-ge-custom

## Notes

- GTA Online does NOT work on Linux (Battleye anti-cheat not supported)
- Only Story Mode is playable on Linux
- Legacy/Standard Edition is easier to run than Enhanced Edition