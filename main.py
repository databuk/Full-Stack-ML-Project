from dsProject.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from dsProject.pipeline.data_validation_pipeline import DataValidationPipeline
from dsProject.pipeline.data_transformation_pipeline import DataTransformationPipeline
from dsProject import logger

STAGE_NAME = "Data Ingestion Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    ingestion_pipeline = DataIngestionPipeline()
    ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    validation_pipeline = DataValidationPipeline()
    validation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    transformation_pipeline = DataTransformationPipeline()
    transformation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e