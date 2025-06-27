import logging
import os
from datetime import datetime

def get_session_logger(session_name: str, log_dir: str = "logs") -> logging.Logger:
    """
    Returns a logger that logs both to a file and console for a given session.
    Ensures a new file per session based on timestamp.
    """
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_file = os.path.join(log_dir, f"{session_name}_{timestamp}.log")

    logger = logging.getLogger(f"CaseStudy6_{session_name}")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Avoid duplicate logs

    if not logger.handlers:
        # File handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        fh.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s - %(message)s'))

        # Console handler (optional)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s - %(message)s'))

        logger.addHandler(fh)
        logger.addHandler(ch)

        logger.info(f"===== SESSION '{session_name}' STARTED =====")
        logger.info(f"Log file: {log_file}")

    return logger
