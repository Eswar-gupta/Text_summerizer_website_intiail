import os,sys
from pathlib import Path

ROOT_dir = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.insert(0, str(ROOT_dir))

from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.data_tranformation import DataTransformation
from src.textSummarizer.logging.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()