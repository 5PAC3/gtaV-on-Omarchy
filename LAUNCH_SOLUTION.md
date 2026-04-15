# GTA V Epic Games - Soluzione Funzionante

## Soluzione: Launch Manuale + fix.bat

**NOTA**: Heroic 2.20.1 ha un bug che impedisce il lancio del gioco. La soluzione è bypassare Heroic e usare uno script fix.bat.

### Script di Launch

Copia `launch_gta_manual.sh` in una posizione accessibile (es. `~/.local/bin/launch_gta.sh`):

```bash
#!/usr/bin/env bash
set -e

export WINEPREFIX="/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/prefixes"
export PROTON_PATH="/home/teo/.config/heroic/tools/proton/GE-Proton10-34"
export STEAM_COMPAT_DATA_PATH="$WINEPREFIX"
export STEAM_COMPAT_CLIENT_INSTALL_PATH="$HOME/.local/share/steam"
export GAME_PATH="/run/media/teo/370787c0-3b29-4394-8a39-2e0ffd9f87b2/heroic/GTAV"
export USE_FAKE_EPIC_EXE=true
export WINEDLLOVERRIDES="ucrtbase=b"

echo "Setting up Rockstar Games Launcher..."
mkdir -p "$WINEPREFIX/drive_c/Program Files/Rockstar Games/Launcher"
cp "$GAME_PATH/Redistributables/Rockstar-Games-Launcher.exe" "$WINEPREFIX/drive_c/Program Files/Rockstar Games/Launcher/Launcher.exe"

cd "$GAME_PATH"

"$PROTON_PATH/proton" run "fix.bat" "$@"
```

### fix.bat (deve essere nella cartella del gioco)

```bat
start "" EpicGamesLauncher.exe PlayGTAV.exe %*
ping -n 30 localhost > nul
start "" GTA5.exe -useEpic -fromRGL
```

### Spiegazione

1. **EpicGamesLauncher.exe fake**: Simula l'Epic Games Launcher
2. **PlayGTAV.exe**: Launcher che avvia il Rockstar Games Launcher  
3. **wait 30 sec**: Lascia tempo al Rockstar Launcher di avviarsi
4. **GTA5.exe**: Avvia il gioco direttamente con flag Epic
5. **WINEDLLOVERRIDES=ucrtbase=b**: Risolve l'errore `_strerror_s`

### Funziona!

Il gioco ora si avvia correttamente. Testato con:
- GE-Proton10-34
- GTA V Legacy Edition (Epic Games)

### Limitazioni

- **GTA Online**: Non funziona (Battleye)
- **Story Mode**: ✅ Funziona

### Crediti

- Soluzione trovata: Aprile 2026
- Sistema: Arch Linux + Hyprland + GTX 1650
