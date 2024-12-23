import sys
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))  # Using insert(0) for higher priority

from src.textSummarizer.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainPipeline
from src.textSummarizer.pipeline.stage_02_data_validation_pipeline import DataValidationTrainingPipeline
from src.textSummarizer.logging.logging import logger

STAGE_NAME = "data_ingestion_stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Starting {STAGE_NAME} pipeline...")
    pipeline = DataIngestionTrainPipeline()
    pipeline.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} pipeline completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "data_validation_stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Starting {STAGE_NAME} pipeline...")
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{STAGE_NAME} pipeline completed successfully.")
except Exception as e:
    logger.exception(e)
    raise e









