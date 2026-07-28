from dsProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from dsProject import logger

STAGE_NAME = "Data Ingestion Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_pipeline = DataIngestionTrainingPipeline()
    data_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e