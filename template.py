import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format= "[%(asctime)s]: %(message)s:")

project_name = "End_to_End_ML"  
files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in files:
    filepath = Path(filepath)

    file_dir, filename = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating folders {file_dir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            pass
            logging.info(f"{filename} created")
    
    else:
        logging.info(f"{filename} already created")
        