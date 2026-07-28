from dsProject.config.configuration import ConfigurationManager
from dsProject.components.data_transformation import DataTransformation
from dsProject.constants import *
from dsProject.utils.common import *


class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = read_yaml(CONFIG_FILE_PATH)
            with open(config.data_validation.STATUS_FILE, "r") as f:
                validation_status = f.read().split(" ")[-1]
            if validation_status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            print(e)