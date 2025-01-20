import pandas as pd
import os
import sys
from src.exception import customException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class ingestion_config:
    train_data_path: str = os.path.join("artifacts","train_data.csv")
    test_data_path: str = os.path.join("artifacts", "test_data.csv")
    data_path: str = os.path.join("artifacts", "dataset.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = ingestion_config
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion started")
            df = pd.read_csv(r"D:\P1 Anna\python_ml_end_to_end\notebook\data\data.csv")
            logging.info("Read dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.data_path, index=False, header=True)
            logging.info("Stored original dataset as dataset.csv")
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Split dataset into train and test data")
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Stored train and test datasets as csv files")
            logging.info("Data Ingestion done successfully.")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise customException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()