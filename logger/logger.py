import os
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logger(name: str = "buffet_logger") -> logging.Logger:
    # Crée le dossier logs s’il n’existe pas
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "buffet_game.log")

    handler = TimedRotatingFileHandler(
        filename=log_file,
        when="midnight",     # Rotation à minuit
        interval=1,          # Tous les jours
        backupCount=7,       # Garder 7 jours de logs
        encoding='utf-8'
    )

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.propagate = False  # Évite les doublons si logger global existe déjà

    return logger
