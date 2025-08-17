import os
from pathlib import Path

list_of_files = [
    "data/text.txt",
    "research/notebook-1.ipynb",
    "research/notebook-2.ipynb",
    "apps.py",
    "Dockerfile",
    "requirements.txt",
    "general-info.md",
    "model/test.txt",
    "model/train.py",
    ".gitignore"
]

for file in list_of_files:
    file_path = Path(file)
    if not file_path.exists():
        # Create the directory if it does not exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        # Create an empty file
        file_path.touch()
        print(f"Created: {file_path}")
    else:
        print(f"File already exists: {file_path}")