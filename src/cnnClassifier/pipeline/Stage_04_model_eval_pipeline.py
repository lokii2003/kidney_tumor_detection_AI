from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_eval_componemt import Evaluation
from src.cnnClassifier import logger
import os


STAGE_NAME = "Evaluation stage"




class EvaluationPipeline:
    def __init__(self):
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/lokii2003/kidney_tumor_detection_AI.mlflow"
        # Set your DagsHub credentials (MLflow uses HTTP Basic Auth)
        os.environ["MLFLOW_TRACKING_USERNAME"] = "lokii2003"
        os.environ["MLFLOW_TRACKING_PASSWORD"] = "5caadabb5d09c044bad44caaf56d9fb6a2bf0122"


    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()