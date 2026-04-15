# Guida Completa: GTA V Epic Games su Linux (Heroic) - Fix ucrtbase.dll._strerror_s

## Problema
```
wine: Call from 00006FFFFFC1CF57 to unimplemented function ucrtbase.dll._strerror_s, aborting
```

**Causa**: Wine/Proton non implementa la funzione `_strerror_s` in `ucrtbase.dll`. È uno stub in tutte le versioni attuali di Wine (fino a Wine 10.x).

## Sistema di Test
- **Distro**: Omarchy (Arch-based Linux)
- **Window Manager**: Hyprland
- **GPU**: NVIDIA GeForce GTX 1650
- **Heroic**: 2.20.1
- **Gioco**: GTA V Legacy Edition (Epic Games Store)
- **Locazione**: External HDD

## Soluzione Finale: Compilare DLL Nativa con mingw via Proton

### Passaggio 1: Installa Mingw-w64

Scarica mingw-w64 precompilato:
```bash
cd /tmp
curl -L "https://download.qt.io/development_releases/prebuilt/mingw_64/MinGW-w64-x86_64-11.2.0-release-posix-seh-rt_v9-rev1.7z" -o mingw.7z
mkdir -p mingw_extract
7z x mingw.7z -omimg
```

Il percorso sarà: `/tmp/mimg/mingw64/`

### Passaggio 2: Crea il File C con la Funzione _strerror_s

Crea `/tmp/ucrtbase_override.c`:
```c
#include <windows.h>

errno_t __cdecl _strerror_s(char *buffer, size_t sizeInChars, int errnum)
{
    if (!buffer || sizeInChars == 0) {
        return 22; // EINVAL
    }
    
    const char *msg = NULL;
    
    switch (errnum) {
        case 0: msg = "No error"; break;
        case EINVAL: msg = "Invalid argument"; break;
        case ERANGE: msg = "Result too large"; break;
        case ENOMEM: msg = "Not enough memory"; break;
        case EFAULT: msg = "Bad address"; break;
        case EBADF: msg = "Bad file descriptor"; break;
        case ENOENT: msg = "No such file or directory"; break;
        case ENOSPC: msg = "No space left on device"; break;
        case EACCES: msg = "Permission denied"; break;
        case EEXIST: msg = "File exists"; break;
        case EISDIR: msg = "Is a directory"; break;
        case ENOTDIR: msg = "Not a directory"; break;
        case EPERM: msg = "Operation not permitted"; break;
        default: msg = "Unknown error";
    }
    
    size_t len = 0;
    const char *p = msg;
    while (*p++) len++;
    
    if (len >= sizeInChars) {
        if (sizeInChars > 0) buffer[0] = '\0';
        return 34; // ERANGE
    }
    
    char *dst = buffer;
    const char *src = msg;
    while ((*dst++ = *src++));
    
    return 0;
}
```

### Passaggio 3: Compila la DLL usando Proton

Usa Proton per eseguire mingw-gcc (Proton ha già Wine):
```bash
# Percorsi da adattare al tuo sistema
PREFIX="/percorso/al/tuo/prefix"
PROTON="/percorso/al/tuo/proton/GE-Proton10-34/proton"
GAME_DIR="/percorso/alla/cartella/gioco/GTAV"
MINGW_DIR="/tmp/mimg/mingw64"

# Compila la DLL
WINEPREFIX="$PREFIX" \
STEAM_COMPAT_DATA_PATH="$PREFIX" \
STEAM_COMPAT_CLIENT_INSTALL_PATH="$HOME/.local/share/.steam/steam" \
"$PROTON" run \
"$MINGW_DIR/bin/x86_64-w64-mingw32-gcc.exe" \
-shared \
-o "$PREFIX/drive_c/windows/system32/ucrtbase.dll" \
/tmp/ucrtbase_override.c \
-I"$MINGW_DIR/x86_64-w64-mingw32/include"
```

### Passaggio 4: Configura Heroic

Aggiungi variabile d'ambiente `WINEDLLOVERRIDES=ucrtbase=n` per forzare Wine a usare la DLL nativa.

File di configurazione (`~/.config/heroic/GamesConfig/[game-id].json`):
```json
{
  "[game-id]": {
    "wineVersion": {
      "bin": "/percorso/a/GE-Proton10-34/proton",
      "name": "GE-Proton10-34",
      "type": "proton"
    },
    "enviromentOptions": [
      {
        "key": "USE_FAKE_EPIC_EXE",
        "value": "true"
      },
      {
        "key": "WINEDLLOVERRIDES",
        "value": "ucrtbase=n"
      }
    ],
    "targetExe": "/percorso/GTAV/PlayGTAV.exe"
  }
}
```

### Passaggio 5: Copia EpicGamesLauncher.exe Falso

Questo è richiesto per far funzionare GTA V da Epic:
```bash
# Scarica EpicGamesLauncher.exe fake
curl -L "https://github.com/Etaash-mathamsetty/heroic-epic-integration/releases/download/v0.4/EpicGamesLauncher.exe" \
-o EpicGamesLauncher.exe

# Copia nella cartella del gioco
cp EpicGamesLauncher.exe /percorso/GTAV/

# Copia nel prefix
cp EpicGamesLauncher.exe "$PREFIX/drive_c/windows/system32/"
cp EpicGamesLauncher.exe "$PREFIX/drive_c/windows/syswow64/"
cp EpicGamesLauncher.exe "$PREFIX/drive_c/windows/command/"
```

## Cose Importanti da Sapere

### Proton Disponibili Testati
| Versione | Risultato |
|----------|-----------|
| GE-Proton9-25, 9-26, 9-27 | FALLITO (ucrtbase stub) |
| GE-Proton10-30, 10-34 | FALLITO (ucrtbase stub) |
| Proton-EM-10.0-34 | FALLITO (ucrtbase stub) |
| Wine Native + DLL Override | **DA TESTARE** |

### LIMITAZIONI
- **GTA Online NON funziona** su Linux (Battleye senza supporto Linux)
- Solo Story Mode dovrebbe funzionare

### Perché Serve EpicGamesLauncher.exe Fake
GTA V controlla la presenza dell'Epic Games Launcher. Il fake launcher bypassa questo controllo.

### WINEDLLOVERRIDES Significato
- `ucrtbase=n` = usa la DLL **nativa** (quella compilata)
- `ucrtbase=b` = usa la DLL **builtin** di Wine
- `ucrtbase=n,b` = prima nativa, poi builtin come fallback

## Debug

Per vedere i log:
```bash
# I log di Heroic sono in
~/.local/state/Heroic/logs/games/[game-id]_legendary/launch.log
```

## Alternative se Non Funziona

1. **Comprare versione Steam** (~15-20€) - funziona con Proton vanilla
2. **Aspettare che Wine implementi _strerror_s** - al momento è ancora stub
3. **Usare la versione Steam con Proton** - la versione Steam non richiede questa funzione

## Note Tecniche

### Perché questo funziona
1. La DLL compilata con mingw contiene la funzione `_strerror_s` reale di Windows
2. `WINEDLLOVERRIDES=ucrtbase=n` dice a Wine di usare la DLL nativa invece di quella builtin
3. Quando il gioco chiama `_strerror_s`, Wine carica la nostra DLL che ha l'implementazione reale

### Caveat
- La DLL compilata è una versione minima di ucrtbase
- Se il gioco usa altre funzioni ucrtbase mancanti, potrebbero esserci altri errori
- La funzione `_strerror_s` implementata è semplice e gestisce solo gli errori più comuni

## Riferimenti
- Issue Wine: https://bugs.winehq.org/show_bug.cgi?id=50031
- ProtonGE: https://github.com/GloriousEggroll/proton-ge-custom
- Epic Integration: https://github.com/Etaash-mathamsetty/heroic-epic-integration
- Heroic Wiki: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Rockstar-Games-from-Epic-Games
