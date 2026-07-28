import os
import urllib.request as request
import zipfile
from dsProject import logger
from dsProject.utils.common import get_size
from pathlib import Path
from dsProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded succesfully with the following info:{headers}")
        else:
            logger.info(f"File already exists with the size: {os.path.getsize(self.config.local_data_file)}")
    
    def extract_zip_file(self):
        """zip_file_path:str
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        
        
