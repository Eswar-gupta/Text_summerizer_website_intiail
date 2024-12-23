import sys
import os
from pathlib import Path

# Get absolute path to project root
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.append(str(PROJECT_ROOT))

from src.textSummarizer.constants import config_yaml_file_path, prams_yaml_file_path
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import DataingestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = config_yaml_file_path,
        params_filepath = prams_yaml_file_path):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataingestionConfig:
        config = self.config.data_ingestion_config

        create_directories([config.root_dir])

        data_ingestion = DataingestionConfig(
            root_dir=config.root_dir,
            source_url =config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion