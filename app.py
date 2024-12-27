print("Hi")

import sys
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))  # Using insert(0) for higher priority

from src.textSummarizer.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainPipeline
from src.textSummarizer.pipeline.stage_02_data_validation_pipeline import DataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_03_data_traformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.logging.logging import logger

print("================================================")

STAGE_NAME = "data_ingestion_stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Starting {STAGE_NAME} pipeline...")
    pipeline = DataIngestionTrainPipeline()
    pipeline.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} pipeline completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e