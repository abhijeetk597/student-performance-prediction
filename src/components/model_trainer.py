import os
import sys
from dataclasses import dataclass
import yaml

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models, tune_hyperparameters

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "KNN Regressor": KNeighborsRegressor(),
                "XGB Regressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor()
            }

            # Evaluate models
            model_report:dict = evaluate_models(X_train=X_train, y_train=y_train, 
                                               X_test=X_test, y_test=y_test,
                                               models=models)
            print(model_report)
            best_model = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model]
            print(best_model)
            best_model_obj = models[best_model]
            if best_model_score < 0.6:
                logging.info("No best model found")
                raise CustomException("No best model found", "No best model found")
            else:
                logging.info(f"Best Model: {best_model} | R2 Score: {best_model_score}")
            
            # Read in hyperparameters from Yaml file
            with open("params.yaml", 'r') as f:
                params = yaml.safe_load(f)

            # Tune hyperparameters of the best model
            if params[best_model]:
                r2, best_model_tuned = tune_hyperparameters(X_train=X_train, y_train=y_train, 
                                               X_test=X_test, y_test=y_test,
                                               model=best_model_obj, param=params[best_model])
                if r2 > best_model_score:
                    best_model_obj = best_model_tuned
                    best_model_score = r2
                logging.info(f"Hyperparameter for {best_model} tuned | R2 Score: {best_model_score}")

            # Save the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model_obj
            )

            return f"Best Model: {best_model} | R2 Score: {best_model_score}"
        
        except Exception as e:
            raise CustomException(e, sys)
        
