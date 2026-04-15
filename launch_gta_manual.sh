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

echo "Launching GTA V (Epic Games) via Proton..."
echo "WINEPREFIX: $WINEPREFIX"
echo "Game: $GAME_PATH/PlayGTAV.exe"

cd "$GAME_PATH"

"$PROTON_PATH/proton" run "fix.bat" "$@"
