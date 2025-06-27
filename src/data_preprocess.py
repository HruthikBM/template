from utility.logger import get_session_logger

 
class DataPreprocessor:
    def __init__(self): 
        self.logger = get_session_logger("DataPreprocessor")
        self.logger.info("DataPreprocessor initialized")


    def load_data(self, file_path: str):
        self.logger.info(f"Loading data from {file_path}")