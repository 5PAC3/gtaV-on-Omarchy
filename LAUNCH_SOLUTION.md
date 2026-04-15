# GTA V Epic Games - Soluzione Funzionante

## Soluzione: Launch Manuale con WINEDLLOVERRIDES=ucrtbase=b

**NOTA**: Heroic 2.20.1 ha un bug che impedisce il lancio del gioco - fallisce cercando di copiare EpicGamesLauncher.exe fake. La soluzione è bypassare Heroic e lanciare direttamente con Proton.

### Script di Launch

Copia questo script in una posizione accessibile (es. `~/.local/bin/launch_gta.sh`):

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

cd "$GAME_PATH"

"$PROTON_PATH/proton" run "PlayGTAV.exe" -useEpic -fromRGL "$@"
```

### Spiegazione

La chiave è `WINEDLLOVERRIDES=ucrtbase=b`:
- `b` = built-in: usa la DLL ucrtbase inclusa in Wine/Proton

**NON** usare `ucrtbase=n` (native) - non funziona perché la DLL custom compilata è malformata/incompatibile.

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
