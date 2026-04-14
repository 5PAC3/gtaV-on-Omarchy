# Context Prompt for GTA V on Linux with Heroic

## SYSTEM SPECIFICATIONS
- **Distro**: Omarchy (Arch-based Linux)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores) @ 4.30 GHz
- **GPU**: NVIDIA GeForce GTX 1650 [Discrete]
- **RAM**: ~80 GB
- **Heroic Version**: 2.20.1 ✓ (UPDATED from 2.14.1)

## GAME DETAILS
- **Game**: GTA V - LEGACY EDITION (Standard, NOT Enhanced)
- **Store**: Epic Games
- **Location**: External HDD at `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- **Prefix**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`

## CURRENT CONFIGURATION (FAILED)
- targetExe: PlayGTAV.exe / GTA5.exe (both fail)
- Proton: GE-Proton-latest (10-34), GE-Proton9-26, GE-Proton9-27
- USE_FAKE_EPIC_EXE: true
- offlineMode: false

## ATTEMPTS MADE
1. Updated Heroic to 2.20.1 ✓
2. Used USE_FAKE_EPIC_EXE=true (official method)
3. Tried multiple Proton versions
4. Tried Lutris
5. Tried GTA5.exe directly

All failed with same error: `ucrtbase.dll._strerror_s unimplemented`

## ROOT CAUSE
Wine/Proton doesn't implement ucrtbase.dll._strerror_s function - known limitation.

## SOLUTION
- Buy GTA V Steam version (~15-20€) - works 100% with Proton
- GTA Online does NOT work on Linux (Battleye)

## LAST UPDATED: April 2026