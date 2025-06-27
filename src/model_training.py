from utility.logger import get_session_logger

 
class ModelTraining:
    def __init__(self): 
        self.logger = get_session_logger("ModelTraining")
        self.logger.info("ModelTraining initialized")


    def train_model(self, model, data): 
        self.logger.info("Starting model training") 