from src.InfoCondense.config.configuration import ConfigManager
from src.InfoCondense.components.data_transformation import DataTransformation
from src.InfoCondense.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.InfoCondense.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH)
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()