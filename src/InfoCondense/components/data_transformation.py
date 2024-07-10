from transformers import AutoTokenizer
import os
from src.InfoCondense.logging import logger
from datasets import load_dataset, load_from_disk
from src.InfoCondense.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True, padding=True)
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True, padding=True)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        try:
            dataset_samsum = load_from_disk(str(self.config.data_path))
            dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
            target_dir = os.path.join(self.config.root_dir, "samsum_dataset_transformed")
            dataset_samsum_pt.save_to_disk(target_dir)
        except Exception as e:
            raise e


