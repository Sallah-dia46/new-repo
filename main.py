import git
import os
from pathlib import Path

def git_repo_init(folder_path):
    try:
        # Vérifier si le chemin du fichier est valide
        if not os.path.exists(folder_path):
            raise FileNotFoundError("Le dossier spécifié n'existe pas.")

        # Récupérer le répertoire parent du fichier
        #parent_directory = os.path.dirname(file_path)

        # Initialiser le dépôt Git
        repo = git.Repo.init(folder_path)

        # Get the IndexFile object
        index = repo.index
        # Ajouter le fichier au dépôt Git
        #repo.index.add([folder_path])

        # Faire un commit initial
        repo.index.commit("Initial commit")

        print(f"Le fichier {folder_path} a été initialisé en tant que dépôt Git.")
    except git.exc.GitCommandError as e:
        print(f"Erreur Git : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
import os

def create_project_data_path(root_path, method = "os"):

    if method == "os":
        directories = [
            'data',
            'data/cleaned',
            'data/raw',
            'data/processed',
            'docs',
            'models',
            'notebooks',
            'reports',
            'src'
        ]

        # Create directories
        for directory in directories:
            os.makedirs(os.path.join(root_path, directory), exist_ok=True)

        # Create specific files
        files = [
            'LICENCE',
            'Makefile',
            'notebooks/main.ipynb',
            'requirements.txt',
            'src/utils.py',
            'src/process.py',
            'src/train.py'
        ]

        for file in files:
            with open(os.path.join(root_path, file), 'w'):
                pass
    elif  method == "pathlib" :

        # Chemin racine du projet
        project_root = Path(root_path)

        # Répertoires de premier niveau
        data_dir = project_root / "data"
        docs_dir = project_root / "docs"
        models_dir = project_root / "models"
        notebooks_dir = project_root / "notebooks"
        reports_dir = project_root / "reports"
        src_dir = project_root / "src"

        # Sous-répertoires de data/
        data_cleaned_dir = data_dir / "cleaned"
        data_raw_dir = data_dir / "raw"
        data_process_dir = data_dir/"processed"

        # Création de l'arborescence
        project_root.mkdir()
        data_dir.mkdir()
        docs_dir.mkdir()
        models_dir.mkdir()
        notebooks_dir.mkdir()
        reports_dir.mkdir()
        src_dir.mkdir()
        data_cleaned_dir.mkdir()
        data_raw_dir.mkdir()

        # Création de quelques fichiers de démonstration
        main_notebook_file = notebooks_dir / "main.ipynb"
        utils_file = src_dir / "utils.py"
        train_file= src_dir / "train.py"
        process_file = src_dir / "process.py"

        main_file.touch()
        utils_file.touch()
        train_file.touch()
        process_file.touch()

  
