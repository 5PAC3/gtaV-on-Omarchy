# Context Prompt for GTA V on Linux with Heroic

## SYSTEM SPECIFICATIONS
- **Distro**: Omarchy (Arch-based Linux)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores) @ 4.30 GHz
- **GPU**: NVIDIA GeForce GTX 1650 [Discrete]
- **RAM**: ~80 GB
- **Heroic Version**: 2.20.1 ✓

## GAME DETAILS
- **Game**: GTA V - LEGACY EDITION (Standard, NOT Enhanced)
- **Store**: Epic Games
- **Location**: External HDD at `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- **Prefix**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`

## CURRENT CONFIGURATION
- targetExe: PlayGTAV.exe
- Proton: GE-Proton10-30 (tested), Proton-EM-10.0-34 (backup)
- USE_FAKE_EPIC_EXE: true
- offlineMode: false

## PROTON VERSIONS TESTED
| Version | Status | Notes |
|---------|--------|-------|
| GE-Proton9-25-GTA | FAILED | ucrtbase.dll._strerror_s unimplemented |
| GE-Proton9-26 | FAILED | ucrtbase.dll._strerror_s unimplemented |
| GE-Proton9-27 | FAILED | ucrtbase.dll._strerror_s unimplemented |
| GE-Proton10-30 | TESTING | Based on Wine 10.x - may have ucrtbase fixes |
| Proton-EM-10.0-34 | READY | Backup option - EM builds sometimes work when others don't |

## ROOT CAUSE
The error `ucrtbase.dll._strerror_s` is an unimplemented function in older Wine/Proton versions.
Wine 10.x (used by Proton 10.x) has started implementing more ucrtbase functions.

## INSTALLED PROTONS
```
~/.config/heroic/tools/proton/
├── GE-Proton9-25-GTA/      # Legacy
├── GE-Proton9-26/           # Legacy
├── GE-Proton9-27/           # Legacy (was active)
├── GE-Proton-latest/        # Legacy
├── GE-Proton10-30/          # NEW - Wine 10.x based
└── Proton-EM-10.0-34/       # NEW - EM build, backup
```

## KNOWN ISSUES
- **GTA Online**: Does NOT work on Linux (Battleye anti-cheat, no Linux support)
- **Story Mode**: Should work with working Proton version

## LAST UPDATED: April 2026
