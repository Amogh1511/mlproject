import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_path: str=os.path.join("artifacts","train.csv")
    test_path: str=os.path.join("artifacts","test.csv")
    raw_path: str=os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(r"D:\mlproject\notebook\data\stud.csv")
            logging.info("Read the dataset")

            os.makedirs(os.path.dirname(self.ingestion_config.train_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.raw_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_path,index=False,header=True)

            logging.info("Train Test split done")
            train_set,test_set=train_test_split(df,test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_path,
                self.ingestion_config.test_path
            )
  
        except Exception as Exp:
            raise CustomException(Exp,sys)
        
if __name__=="__main__":
    object=DataIngestion()
    object.initiate_data_ingestion()
