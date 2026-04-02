import logging
import os

def setup_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Création du formateur
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Handler pour le fichier
    file_handler = logging.FileHandler("logs/pipeline.log")
    file_handler.setFormatter(formatter)

    # Handler pour la console (le terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # On évite d'ajouter plusieurs fois les mêmes handlers si la fonction est rappelée
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger