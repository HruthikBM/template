# utility/__init__.py
# Make logger and session management easily importable

try:
    from .logger import get_session_logger
    from .data_preprocess import DataPreprocessor
    
    __all__ = [
        'get_session_logger',
        'DataPreprocessor'
    ]
    
except ImportError as e:
    from .logger import get_session_logger
    logger = get_session_logger("default_session")
    logger.error(f"Failed to import utility modules: {e}")
    
     
    __all__ = ['get_session_logger', 'DataPreprocessor']