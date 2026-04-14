# Context Prompt for New Session: GTA V on Linux with Heroic

You are helping a user run GTA V (Windows/Epic Games version) on Linux using Heroic Games Launcher.

## SYSTEM SPECIFICATIONS
- **Distro**: Omarchy (Arch-based Linux)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores) @ 4.30 GHz
- **GPU**: NVIDIA GeForce GTX 1650 [Discrete]
- **RAM**: ~80 GB
- **Heroic Version**: 2.14.1 (needs update to 2.17+)

## GAME DETAILS
- **Game**: GTA V - LEGACY EDITION (Standard, NOT Enhanced)
- **Store**: Epic Games (installed via Heroic)
- **Location**: External HDD at `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- **Prefix**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`

## THE PROBLEM
The user has GTA V files from Epic Games installed via Heroic, but the game won't launch. The main issues are:
1. "Path Not Found" error when trying to run the game
2. Rockstar Games Launcher (required by Epic version) has CEF browser crashes
3. Game refuses to start without the launcher

## WHAT HAS BEEN TRIED (Chronological)

### 1. Proton Versions (all failed with "Path Not Found")
- GE-Proton-latest
- GE-Proton9-26
- GE-Proton9-25-GTA (with GTA patch for wine bug)
- GE-Proton9-27

### 2. Environment Variables (various combinations)
- USE_FAKE_EPIC_EXE=true
- PROTON_NO_NTSYNC=1
- SteamDeck=1
- WINEDLLOVERRIDES=dxgi=n
- Disable DXVK/VKD3D

### 3. Custom Scripts Created
- `fix.bat` - Launch PlayGTAV.exe with Epic parameters
- `launch_wrapper.bat` - Launch Rockstar Launcher first, then game
- `fix_latest.bat` - Alternative ordering with ping delay
- `launch_heroic.py` - Python wrapper (not tested)

### 4. Manual Actions
- Extracted Rockstar Games Launcher to prefix manually
- Deleted and recreated Wine prefix multiple times
- Installed vcredist manually via winetricks

### 5. Heroic Settings Modified
- targetExe (various attempts)
- winePrefix path
- enableEsync/Fsync disabled

## CURRENT STATE (as of April 2026)
- The Rockstar Games Launcher was successfully installed manually
- When launching the game, it shows "Path Not Found" error
- The game requires the Rockstar Games Launcher but launcher integration is broken on Linux/Proton

## LATEST FINDINGS (February 2026 Heroic Wiki)
According to official Heroic documentation:
Starting from Heroic **2.17**, GTA V installation should be AUTOMATIC.
The official fix is:
1. Update Heroic to version >= 2.17
2. Set environment variable `USE_FAKE_EPIC_EXE=true` in game settings

The user is currently on Heroic 2.14.1 - needs UPDATE.

## REPOSITORY
All work has been documented at: `git@github.com:5PAC3/gtaV-on-Omarchy.git`
Contains: README.md, fix scripts, logs, and Heroic config.

## YOUR TASK
Help the user:
1. First: Update Heroic to latest version (2.17+)
2. Then: Test with USE_FAKE_EPIC_EXE=true only (no custom scripts)
3. If still fails: Consider Lutris as alternative or Steam version of GTA V

Note: GTA Online does NOT work on Linux due to Battleye anti-cheat. Only Story Mode is playable.