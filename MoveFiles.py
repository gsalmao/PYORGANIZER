from pathlib import Path
import shutil


def moveToDirectory(extensions, directory):
    curDir = Path()
    destination = Path(directory)
    for extension in extensions:
        files = curDir.glob(f"*{extension}")
        for file in files:
            print(f"\nMoving {file} to {destination} folder.")
            shutil.move(file, destination)

