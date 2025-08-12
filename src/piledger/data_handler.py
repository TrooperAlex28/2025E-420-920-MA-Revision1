"""Module pour la gestion des données et lecture des fichiers"""

import csv
from pathlib import Path

def read_data_file():
    """Fonction pour lire le fichier de données"""
    # Méthode plus moderne avec pathlib
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent  # Remonte à la racine du projet
    data_file_path = project_root / "src" / "data" / "transactions.csv"
    
    print(f"Debug - Chemin recherché: {data_file_path}")
    print(f"Debug - Fichier existe: {data_file_path.exists()}")
    
    try:
        if not data_file_path.exists():
            print(f"❌ Fichier non trouvé: {data_file_path}")
            return None
            
        with open(data_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            print(f"✅ {len(data)} lignes lues depuis {data_file_path}")
            return data
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier: {e}")
        return None