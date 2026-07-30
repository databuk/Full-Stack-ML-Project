from dsProject.utils.common import load_bin, read_yaml
from dsProject.constants import CONFIG_FILE_PATH
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        config = read_yaml(CONFIG_FILE_PATH)
        self.model = load_bin(Path(config.model_evaluation.model_path))
    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction