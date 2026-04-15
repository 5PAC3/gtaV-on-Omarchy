# GTA V on Linux (Omarchy/Heroic)

Repository to document and solve the issue of running GTA V (Windows/Epic Games version) on Linux using Heroic Games Launcher.

## System Specifications

- **Distro**: Omarchy (Arch-based)
- **Window Manager**: Hyprland
- **CPU**: Intel Core i5-10400F (12 cores) @ 4.30 GHz
- **GPU**: NVIDIA GeForce GTX 1650 [Discrete]
- **RAM**: 16 GB
- **Heroic Version**: 2.20.1
- **Proton**: GE-Proton10-34

## Game Details

- **Edition**: LEGACY EDITION (Standard)
- **Store**: Epic Games
- **Install Location**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV/`
- **Wine Prefix**: `/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes`

---

# ✅ SOLUZIONE FUNZIONANTE - 15 Aprile 2026

## Problemi Risolti

### 1. Heroic 2.20.1 Bug
Heroic fallisce cercando di copiare EpicGamesLauncher.exe:
```
ENOENT: copyfile '/opt/Heroic/resources/app.asar.unpacked/build/bin/x64/win32/EpicGamesLauncher.exe' -> ''
```
**Soluzione**: Bypassare Heroic e lanciare direttamente con Proton.

### 2. ucrtbase.dll._strerror_s
```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```
**Soluzione**: Usare `WINEDLLOVERRIDES=ucrtbase=b` (built-in, non native DLL).

### 3. Rockstar Launcher Non Rileva il Gioco
Il Rockstar Games Launcher non detecta GTA V e mostra "Buy Now".
**Soluzione**: Usare fix.bat che lancia GTA5.exe direttamente dopo aver aperto PlayGTAV.

---

## Quick Start

### 1. Copia lo script di launch
```bash
cp /tmp/gtaV-on-Omarchy/launch_gta_manual.sh ~/.local/bin/launch_gta.sh
chmod +x ~/.local/bin/launch_gta.sh
```

### 2. Esegui il gioco
```bash
~/.local/bin/launch_gta.sh
```

---

## File Necessari

### fix.bat (deve essere nella cartella del gioco)
```bat
start "" EpicGamesLauncher.exe PlayGTAV.exe %*
ping -n 30 localhost > nul
start "" GTA5.exe -useEpic -fromRGL
```

### EpicGamesLauncher.exe
Scaricato da: https://github.com/Etaash-mathamsetty/heroic-epic-integration/releases/download/v0.4/EpicGamesLauncher.exe
Copiato in: cartella del gioco

### Rockstar Games Launcher
Già presente in: `GTAV/Redistributables/Rockstar-Games-Launcher.exe`
Copiato in: `$WINEPREFIX/drive_c/Program Files/Rockstar Games/Launcher/Launcher.exe`

---

## Configurazione Script

Variabili d'ambiente necessarie:
```bash
export WINEDLLOVERRIDES="ucrtbase=b"       # Risolve errore _strerror_s
export USE_FAKE_EPIC_EXE=true               # Abilita fake Epic exe
export STEAM_COMPAT_DATA_PATH="$WINEPREFIX"
export STEAM_COMPAT_CLIENT_INSTALL_PATH="$HOME/.local/share/steam"
```

---

## Proton Versions Tested

| Version | Result | Notes |
|---------|--------|-------|
| GE-Proton9-25, 9-26, 9-27 | ❌ | `ucrtbase.dll._strerror_s` unimplemented |
| GE-Proton10-30, 10-34 | ✅ | Funziona con WINEDLLOVERRIDES=ucrtbase=b |
| Proton-EM-10.0-34 | ❌ | Still unimplemented |

---

## Limitationi

- **GTA Online**: ❌ Non funziona (Battleye anti-cheat)
- **Story Mode**: ✅ Funziona

---

## Cronologia Fix

- **15 Apr 2026**: Soluzione completa funzionante
  - Heroic bypassato con script manuale
  - fix.bat per lanciare il gioco direttamente
  - WINEDLLOVERRIDES=ucrtbase=b

- **14 Apr 2026**: Scoperto errore ucrtbase.dll
  - Compilata DLL nativa (non funziona)
  - Trovato fix con built-in DLL

- **13 Apr 2026**: Identificato bug Heroic 2.20.1
  - CopyFile fallisce con percorso vuoto

---

## Riferimenti

- Wine Bug: https://bugs.winehq.org/show_bug.cgi?id=50031
- ProtonGE: https://github.com/GloriousEggroll/proton-ge-custom
- Epic Integration: https://github.com/Etaash-mathamsetty/heroic-epic-integration
- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games
- Discord Support: https://discord.gg/HeroicGC
