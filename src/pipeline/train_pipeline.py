from src.exception import CustomException
from src.logger import logging
import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

def train_model():
    try:
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

        modeltrainer = ModelTrainer()
        print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
        logging.info("Model training completed")
    
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    train_model()