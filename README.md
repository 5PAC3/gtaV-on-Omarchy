# GTA V on Linux (Omarchy/Heroic)

Repository to document and solve the issue of running GTA V (Windows/Epic Games version) on Linux using Heroic Games Launcher.

## System Specifications

- **Distro**: Omarchy (Arch-based)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores) @ 4.30 GHz
- **GPU**: NVIDIA GeForce GTX 1650 [Discrete]
- **RAM**: 16 GB
- **Heroic Version**: 2.20.1 ✓ (UP TO DATE)

## Game Details

- **Edition**: LEGACY EDITION (Standard)
- **Store**: Epic Games
- **Install Location**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- **Wine Prefix**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`

## Proton Versions Tested

| Version | Result | Notes |
|---------|--------|-------|
| GE-Proton9-25-GTA | FAILED | `ucrtbase.dll._strerror_s` unimplemented |
| GE-Proton9-26 | FAILED | `ucrtbase.dll._strerror_s` unimplemented |
| GE-Proton9-27 | FAILED | `ucrtbase.dll._strerror_s` unimplemented |
| **GE-Proton10-30** | **TESTING** | Based on Wine 10.x - more ucrtbase functions implemented |
| **Proton-EM-10.0-34** | **READY** | EM builds sometimes work when others don't |

## How to Install New Proton Versions

### GE-Proton10-30
```bash
# Download from GitHub
curl -L "https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton10-30/GE-Proton10-30.tar.gz" -o GE-Proton10-30.tar.gz
tar -xf GE-Proton10-30.tar.gz
mv GE-Proton10-30 ~/.config/heroic/tools/proton/
```

### Proton-EM-10.0-34
```bash
# Download from GitHub
curl -L "https://github.com/Etaash-mathamsetty/Proton/releases/download/EM-10.0-34/proton-EM-10.0-34.tar.xz" -o proton-EM-10.0-34.tar.xz
tar -xf proton-EM-10.0-34.tar.xz
mv proton-EM-10.0-34 ~/.config/heroic/tools/proton/
```

## Current Configuration (Active)

- **Proton**: GE-Proton10-30
- **targetExe**: PlayGTAV.exe
- **USE_FAKE_EPIC_EXE**: true
- **DXVK/VKD3D**: Auto-installed
- **protonfixes**: GTAV fix included (removes SteamAppId env var)

## Error (Old Proton Versions)

All attempts with GE-Proton9-xx crash with:
```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```

**Root Cause**: Wine/Proton 9.x doesn't implement `ucrtbase.dll._strerror_s`.

**Solution**: Wine 10.x (Proton 10.x) has started implementing more ucrtbase functions.

## Known Issues

- **GTA Online**: Does NOT work on Linux (Battleye anti-cheat, no Linux support)
- **Story Mode**: Should work with working Proton version

## Last Updated: April 2026
