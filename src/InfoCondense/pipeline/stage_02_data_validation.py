from src.InfoCondense.config.configuration import ConfigManager
from src.InfoCondense.components.data_validation import DataValidation
from src.InfoCondense.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.InfoCondense.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH)
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exit()
