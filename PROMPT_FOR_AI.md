# PROMPT PER AI: Risolvere GTA V Epic Games su Linux

## OBIETTIVO
Far funzionare GTA V (versione Epic Games Store, Legacy Edition) su Linux usando Heroic Games Launcher.

## ERRORE ATTUALE
```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```

## SISTEMA
- **Distro**: Arch-based Linux con Hyprland (window manager)
- **GPU**: NVIDIA GeForce GTX 1650
- **Heroic**: 2.20.1
- **Gioco**: GTA V Legacy Edition (Epic Games)
- **Locazione gioco**: External HDD
- **Prefix Wine**: Su HDD esterno

## COSA È GIÀ STATO FATTO

### 1. DLL Compilata
È stata compilata una DLL nativa di Windows con mingw (via Proton) che implementa `_strerror_s`.
- File: `/tmp/ucrtbase_override.c` contiene il codice C
- La DLL è stata compilata usando:
```bash
WINEPREFIX="$PREFIX" \
STEAM_COMPAT_DATA_PATH="$PREFIX" \
STEAM_COMPAT_CLIENT_INSTALL_PATH="$HOME/.local/share/.steam/steam" \
"$PROTON_PATH/proton" run \
"/tmp/mimg/mingw64/bin/x86_64-w64-mingw32-gcc.exe" \
-shared \
-o "$PREFIX/drive_c/windows/system32/ucrtbase.dll" \
/tmp/ucrtbase_override.c \
-I"/tmp/mimg/mingw64/x86_64-w64-mingw32/include"
```
- DLL risultante: ~1.4MB in `/prefix/drive_c/windows/system32/ucrtbase.dll`

### 2. EpicGamesLauncher.exe Fake
Scaricato da: https://github.com/Etaash-mathamsetty/heroic-epic-integration/releases/download/v0.4/EpicGamesLauncher.exe
- Copiato in: cartella gioco, system32, syswow64, command/

### 3. Configurazione Heroic Attuale
```json
{
  "wineVersion": {
    "bin": "/home/teo/.config/heroic/tools/proton/GE-Proton10-34/proton",
    "name": "GE-Proton10-34",
    "type": "proton"
  },
  "enviromentOptions": [
    { "key": "USE_FAKE_EPIC_EXE", "value": "true" },
    { "key": "WINEDLLOVERRIDES", "value": "ucrtbase=n" }
  ],
  "targetExe": "/percorso/GTAV/PlayGTAV.exe"
}
```

## COMPORTAMENTO ATTUALE
Quando si lancia il gioco da Heroic:
- Appare briefly "Installing game specific fixes" 
- La finestra si chiude
- Non succede nulla
- Nessun errore visibile

## LOG
I log di Heroic sono in: `~/.local/state/Heroic/logs/games/[game-id]_legendary/launch.log`

## COSA SERVE
1. Capire perché il gioco non si avvia (potrebbe esserci un altro errore non visibile)
2. Verificare se la DLL override funziona correttamente
3. Eventualmente debuggare ulteriormente il problema

## VINCOLI
- **Nessuna spesa**: l'utente non vuole comprare la versione Steam
- **GTA Online non funzionerà mai**: Battleye senza supporto Linux
- Solo Story Mode è l'obiettivo

## ISTRUZIONI PER L'AI
1. Analizza il log di Heroic per vedere l'errore esatto
2. Verifica se la DLL override è stata caricata correttamente
3. Prova a eseguire il gioco manualmente per vedere l'output
4. Suggerisci modifiche o comandi per debuggare ulteriormente
5. Se la DLL non funziona, proponi alternative (es. compilare DLL più completa, usare altre versioni Proton, ecc.)
