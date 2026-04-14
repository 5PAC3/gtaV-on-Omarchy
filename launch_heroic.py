#!/usr/bin/env python3
import sys
import os
import subprocess
import time

if __name__ == "__main__":
    game_exe = "PlayGTAV.exe"
    
    print("Launching EpicGamesLauncher wrapper...")
    time.sleep(5)
    
    if os.path.exists(game_exe):
        subprocess.run([game_exe, "-useEpic", "-fromRGL"] + sys.argv[1:])
    else:
        print(f"Game executable {game_exe} not found")
        sys.exit(1)