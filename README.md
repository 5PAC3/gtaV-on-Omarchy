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

## PROBLEMA

```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```

**Causa**: Wine/Proton non implementa la funzione `_strerror_s` in `ucrtbase.dll`. È uno stub in tutte le versioni attuali di Wine (fino a Wine 10.x).

## SOLUZIONE: Compilare DLL Nativa

Vedi **`GUIDE_ucrtbase_fix.md`** per la guida completa step-by-step.

### Quick Summary

1. **Scarica mingw-w64**: https://download.qt.io/development_releases/prebuilt/mingw_64/MinGW-w64-x86_64-11.2.0-release-posix-seh-rt_v9-rev1.7z

2. **Compila la DLL** usando Proton come compilatore:
```bash
WINEPREFIX="$PREFIX" \
STEAM_COMPAT_DATA_PATH="$PREFIX" \
STEAM_COMPAT_CLIENT_INSTALL_PATH="$HOME/.local/share/.steam/steam" \
"$PROTON_PATH/proton" run \
"$MINGW_DIR/bin/x86_64-w64-mingw32-gcc.exe" \
-shared \
-o "$PREFIX/drive_c/windows/system32/ucrtbase.dll" \
ucrtbase_override.c
```

3. **Configura Heroic** con:
```json
{
  "enviromentOptions": [
    { "key": "USE_FAKE_EPIC_EXE", "value": "true" },
    { "key": "WINEDLLOVERRIDES", "value": "ucrtbase=n" }
  ]
}
```

4. **Copia EpicGamesLauncher.exe fake** nella cartella del gioco e nel prefix.

## Proton Versions Tested

| Version | Result | Notes |
|---------|--------|-------|
| GE-Proton9-25, 9-26, 9-27 | FAILED | `ucrtbase.dll._strerror_s` unimplemented |
| GE-Proton10-30, 10-34 | FAILED | Still unimplemented in Wine 10.x |
| Proton-EM-10.0-34 | FAILED | Still unimplemented |
| **DLL Override** | **TESTING** | Compile native DLL with _strerror_s |

## LIMITAZIONI

- **GTA Online**: Does NOT work on Linux (Battleye anti-cheat, no Linux support)
- **Story Mode**: Should work with DLL override

## Files in this Repo

- `ucrtbase_override.c` - C source code for _strerror_s implementation
- `GUIDE_ucrtbase_fix.md` - Complete step-by-step guide
- `gta_config.json` - Heroic config template
- `fix.bat` - Launch wrapper script

## Riferimenti

- Wine Bug: https://bugs.winehq.org/show_bug.cgi?id=50031
- ProtonGE: https://github.com/GloriousEggroll/proton-ge-custom
- Epic Integration: https://github.com/Etaash-mathamsetty/heroic-epic-integration
- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games

## Last Updated: April 2026
