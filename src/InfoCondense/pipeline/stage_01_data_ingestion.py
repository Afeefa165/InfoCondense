from src.InfoCondense.config.configuration import ConfigManager
from src.InfoCondense.components.data_ingestion import DataIngestion
from src.InfoCondense.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.InfoCondense.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH)
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()