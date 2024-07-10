from src.InfoCondense.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.InfoCondense.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.InfoCondense.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.InfoCondense.logging import logger
import os
import json

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

existing_filepath = os.path.join("artifacts", "data_ingestion", "samsum_dataset", "dataset_dict.json")

with open(existing_filepath, 'r') as f:
    dataset_dict = json.load(f)

save_dir = os.path.join("data", "dict_file")
os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

# Save dataset_dict.json to specified directory
filepath = os.path.join(save_dir, "dataset_dict.json")
with open(filepath, 'w') as f:
    json.dump(dataset_dict, f)

print(f"{filepath} saved successfully.")

if os.path.exists(existing_filepath):
    os.remove(existing_filepath)
    print(f"{existing_filepath} has been deleted.")
else:
    print(f"The file {filepath} does not exist.")

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

with open(filepath, 'r') as f:
    dataset_dict = json.load(f)

with open(existing_filepath, 'w') as f:
    json.dump(dataset_dict, f)

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    raise e
