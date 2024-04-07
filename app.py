from src.MLproject.logger import logging
from src.MLproject.exception import CustomException
from src.MLproject.components.data_ingestion import DataIngestion
from src.MLproject.components.data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("The execution has started")


    try:
        #data_ingestion_config=DataIngestionConfig()
        data_Ingestion=DataIngestion()
        data_Ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e,sys)
    

