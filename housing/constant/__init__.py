

import os
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

    
ROOT_DIR = os.getcwd()  #to get current working directory
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)



CURRENT_TIME_STAMP = get_current_time_stamp()






# Data Ingestion related variable

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"


# Data Validation

DATA_VALIDATION_ARTIFACT_DIR='data_validation'
DATA_VALIDATION_SCEHMA_FILE_PATH_KEY='schema_file_path'
DATA_VALIDATION_REPORT_FILE_PATH_KEY='report_file_path'
DATA_VALIDATION_REPORT_FILR_PATH_KEY='report_page_file_path'


#DATA TRANSFORMATION
DATA_TRANSFORMATION_ARTIFACT_DIR='data_transformation'
DATA_TRANSFORMATION_TRAIN_DIR_KEY='transformed_train_dir'
DATA_TRANSFORMATION_TEST_DIR_KEY='transformed_test_dir'
DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_PATH_KEY='preprocessed_object_file_path'


#Model Trainnner

DATA_TRAINER_ARTIFACT_DIR='data_trainer'
DATA_TRAINER_TRAINED_MODEL_FILE_PATH_KEY='trained_model_file_path'
DATA_TRAINER_BASE_ACCURACY_KEY='base_accuracy'
# DATA_'model_config_file_path'




