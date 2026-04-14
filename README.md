# GTA V on Linux (Omarchy/Heroic)

Repository to document and solve the issue of running GTA V (Windows/Epic Games version) on Linux using Heroic Games Launcher.

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

### 2. Proton Versions Tested
- GE-Proton-latest - Various issues
- GE-Proton9-26 - Path not found error
- GE-Proton9-25-GTA (with GTA patch) - Path not found error
- GE-Proton9-27 - Various issues

### 3. Fixes Attempted

#### Environment Variables
```json
"USE_FAKE_EPIC_EXE": "true"
"PROTON_NO_NTSYNC": "1"
"SteamDeck": "1"
"WINEDLLOVERRIDES": "dxgi=n"
```

#### Various .bat Scripts
- `fix.bat` - Attempts to launch PlayGTAV.exe with Epic parameters
- `launch_wrapper.bat` - Attempts to launch launcher first, then game
- Various paths: relative, absolute (C:\...), using Wine paths

### 4. Configuration Changes
- Disabled DXVK/VKD3D (force wined3d)
- Disabled Esync/Fsync
- Changed winePrefix path

### 5. Manual Installation Attempts
- Extracted Rockstar Games Launcher to prefix using bsdtar
- Attempted wine64 installation of launcher
- Copied files from Redistributables folder

## Positive Findings

1. **Heroic Works**: Heroic Games Launcher runs and manages games correctly
2. **Proton Works**: Different Proton versions run without major issues
3. **Game Files**: GTA V files from Epic are present and valid
4. **Launcher Installer**: The Rockstar-Games-Launcher.exe is present in Redistributables
5. **Social Club**: Social-Club-Setup.exe is available if needed

## Known Problems

1. **Path Not Found Error**: The most common error when trying to run the game
2. **Win32 Path Issues**: Wine drive paths (V:\...) don't match expected Windows paths
3. **Launcher Crashes**: CEF browser in Rockstar Launcher crashes
4. **GTA Requires Launcher**: Game refuses to start without Rockstar Games Launcher

## Workarounds That Might Help

1. **Use Steam Version**: The original repo was designed for Steam version which works better with Proton
2. **Try Lutris**: Some users report Lutris works better for Rockstar games
3. **Wine System Install**: Try installing Wine system-wide and running launcher outside Proton

## Help Needed

If you've solved running GTA V on Linux with Epic + Heroic, please open an issue or PR with your solution.

### Questions to Solve
1. How to properly install Rockstar Games Launcher in Proton prefix?
2. How to make GTA V accept the Epic credentials without launcher?
3. Are there specific Proton/wine versions that work better?

## References

- Original Guide: https://github.com/shuvozula/steam-gta5-linux
- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki
- GTA V Enhanced on Linux: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games
- Proton-GE Custom: https://github.com/GloriousEggroll/proton-ge-custom
- telqor GTA patch: https://github.com/telqor/proton-ge-custom

## Notes

- GTA Online does NOT work on Linux (Battleye anti-cheat not supported)
- Only Story Mode is playable on Linux
- Enhanced Edition has additional issues compared to Standard Edition