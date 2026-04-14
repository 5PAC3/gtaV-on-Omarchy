# GTA V on Linux (Omarchy/Heroic)

Repository to document and solve the issue of running GTA V (Windows/Epic Games version) on Linux using Heroic Games Launcher.

## System Specifications

- **Distro**: Omarchy (Arch-based)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores) @ 4.30 GHz
- **GPU**: NVIDIA GeForce GTX 1650 [Discrete]
- **RAM**: ~80 GB
- **Heroic Version**: 2.20.1 ✓ (UP TO DATE)

## Current Configuration

- **targetExe**: PlayGTAV.exe (also tried GTA5.exe - same result)
- **Proton**: GE-Proton9-27, GE-Proton9-26, GE-Proton-latest (all failed)
- **USE_FAKE_EPIC_EXE**: true
- **offlineMode**: false
- **DXVK/VKD3D**: Auto-installed

## Game Details

- **Edition**: LEGACY EDITION (Standard)
- **Store**: Epic Games
- **Install Location**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- **Wine Prefix**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`

## What Was Tried

### Heroic (Official Method - Heroic 2.17+)
1. Updated Heroic to 2.20.1 ✓
2. Set `USE_FAKE_EPIC_EXE=true` ✓
3. Used PlayGTAV.exe as target
4. Tried multiple Proton versions: GE-Proton-latest, GE-Proton9-26, GE-Proton9-27

### Result: FAILED
All attempts crash with the same error:
```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```

### Lutris
- Installed Lutris
- Tried multiple configurations
- Same ucrtbase.dll error

## Root Cause

The error `ucrtbase.dll._strerror_s` is an **unimplemented function in Wine**. This is a known limitation of Wine/Proton that cannot be easily fixed. The function `_strerror_s` is part of the Universal C Runtime (UCRT) and Wine doesn't implement it.

## Solutions

### 1. GTA V Steam Version (RECOMMENDED)
The Steam version of GTA V works perfectly with Proton. This is the only reliable solution.
- Cost: ~15-20€ on key shops
- Works: 100% with Proton/Steam
- GTA Online: Does NOT work on Linux (Battleye)

### 2. Wait for Wine Fix
This is a Wine bug that may be fixed in future versions. Monitor:
- Wine GitHub issues
- ProtonGE releases

## Known Issues

- **GTA Online**: Does NOT work on Linux (Battleye anti-cheat)
- **Story Mode**: Should work with Steam version

## Last Updated: April 2026