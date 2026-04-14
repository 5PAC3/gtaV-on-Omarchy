# GTA V on Linux (Omarchy/Heroic)

Repository to document and solve the issue of running GTA V (Windows/Epic Games version) on Linux using Heroic Games Launcher.

## IMPORTANT: Edition and Heroic Version

**GTA V Edition**: LEGACY EDITION (Standard), NOT Enhanced
**Heroic Version**: 2.14.1 (outdated - needs update to 2.17+)

## Current Status

**TEST IN PROGRESS** - Heroic 2.19 (auto-fake epic) and manual CEF cache cleanup.

## Update 2026

According to official Heroic documentation (February 2026):
- Starting from Heroic **2.17**, the entire GTA V/RDR2 installation process should be **AUTOMATIC**
- The recommended method is:
  1. Update Heroic to version >= 2.17
  2. Set environment variable `USE_FAKE_EPIC_EXE=true` in game settings

This bypasses the need for custom .bat or Python scripts.

## System Specifications

- **Distro**: Omarchy (Arch-based)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores) @ 4.30 GHz
- **GPU**: NVIDIA GeForce GTX 1650 [Discrete]
- **RAM**: 79.84 GiB / 230.87 GiB (35%)
- **Heroic Version**: 2.14.1 (NEEDS UPDATE)

## What Has Been Tried

### 1. Rockstar Games Launcher
- Launcher IS REQUIRED by GTA V (Epic version)
- After manual install, launcher PARTIALLY works but game still fails
- Errors: CEF crash, "Path Not Found", prerequisites failed

### 2. Error: Path Not Found (MAIN ISSUE)
Wine drive paths (V:\...) don't match expected Windows paths. Working directory when .bat scripts run from Heroic/Proton is different than expected.

### 3. Proton Versions Tested
All give "Path Not Found" error:
- GE-Proton-latest
- GE-Proton9-26
- GE-Proton9-25-GTA (with GTA patch)
- GE-Proton9-27

### 4. Fix Files (Chronological)

| File | Description | Result |
|------|------------|--------|
| `fix.bat` (attempt 1) | PlayGTAV.exe -useEpic -fromRGL | Path not found |
| `launch_wrapper.bat` | Launcher first, then game | Launcher install issues |
| `fix_latest.bat` | Alternative ordering with ping | Various errors |
| `launch_heroic.py` | Python wrapper attempt | Not tested |

### 5. Next Steps (Based on 2026 Docs)
1. UPDATE Heroic to 2.17+ (currently on 2.14.1)
2. Set only `USE_FAKE_EPIC_EXE=true`
3. If fails, try Lutris

## Known Problems

1. **Path Not Found Error**: Working directory issues with Proton
2. **Launcher Crashes**: CEF browser in Rockstar Launcher
3. **GTA Requires Launcher**: Game won't start without it

## Quick Summary (3 Lines)

Running GTA V on Linux with Epic + Heroic is complex because:
1. Rockstar Launcher has issues with Wine/Proton (CEF crashes, path problems)
2. The working directory mapping (V:\ vs C:\) breaks .bat scripts
3. Solution: Update Heroic to 2.17+ for built-in automation

## References

- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games
- Official fix: USE_FAKE_EPIC_EXE=true (Heroic 2.17+)
- Lutris as alternative

## Notes

- GTA Online does NOT work on Linux (Battleye)
- Only Story Mode is playable