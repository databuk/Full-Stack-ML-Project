# from src.dsProject.config.configuration import ConfigurationManager
# from src.dsProject.components.model_trainer import ModelTrainer
# config = ConfigurationManager()
# model_trainer_config = config.get_model_trainer_config()
# model_trainer = ModelTrainer(model_trainer_config)
# model_trainer.train()

from dsProject.pipeline.prediction_pipeline import PredictionPipeline
import pandas as pd
from dsProject.utils.common import load_bin, read_yaml
from dsProject.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH
from pathlib import Path
config = read_yaml(CONFIG_FILE_PATH)
schema = read_yaml(SCHEMA_FILE_PATH)

test = pd.read_csv(config.model_trainer.test_data_path)
data = test.drop([schema.TARGET_COLUMN.name], axis=1)
prediction_pipeline = PredictionPipeline()
prediction = prediction_pipeline.predict(data)
print(prediction[:5])
