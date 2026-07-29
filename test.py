from src.dsProject.config.configuration import ConfigurationManager
from src.dsProject.components.model_trainer import ModelTrainer
config = ConfigurationManager()
model_trainer_config = config.get_model_trainer_config()
model_trainer = ModelTrainer(model_trainer_config)
model_trainer.train()