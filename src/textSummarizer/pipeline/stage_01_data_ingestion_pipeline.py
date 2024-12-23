import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))  # Using insert(0) for higher priority

from src.textSummarizer.logging.logging import logger
from src.textSummarizer.conponents.data_ingenstion import DataIngestion
from src.textSummarizer.config.configuration import ConfigurationManager

class DataIngestionTrainPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager() ##Note there are deflaut arguments like config.yaml and params.yaml files etc.. which are intizalized in the configration.py where it tood care all those things
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        

