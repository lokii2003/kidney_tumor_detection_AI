from src.cnnClassifier.pipeline.stage_01_dataingpipeline import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_perparebasepipeline import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.Stage_03_model_trainingpeline import ModelTrainingPipeline
from src.cnnClassifier import *




STAGE_NAME = "Data Ingestion stage"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  data_ingestion = DataIngestionTrainingPipeline()
  data_ingestion.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e



STAGE_NAME = "Prepere base model"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  perpare_base_model = PrepareBaseModelTrainingPipeline()
  perpare_base_model.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e


STAGE_NAME = "Model training"
try:
  logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
  model_training = ModelTrainingPipeline()
  model_training.main()
  logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e
