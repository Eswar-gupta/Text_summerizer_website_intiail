import os,sys
from pathlib import Path

ROOT_dir = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.insert(0, str(ROOT_dir))

from src.textSummarizer.logging.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.data_validation import DataValiadtion


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()

