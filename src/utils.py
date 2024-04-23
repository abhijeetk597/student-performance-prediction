import os
import sys
import dill
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as f:
            dill.dump(obj, f)

    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for name, model in models.items():
            model.fit(X_train, y_train)
            r2 = model.score(X_test, y_test)
            report[name] = r2

        return report
    
    except Exception as e:
        raise CustomException(e, sys)

def tune_hyperparameters(X_train, y_train, X_test, y_test, model, param):
    try:
        gs = GridSearchCV(model,param,cv=5)
        gs.fit(X_train,y_train)

        model.set_params(**gs.best_params_)
        model.fit(X_train,y_train)
        r2 = model.score(X_test, y_test)

        return r2, model
    
    except Exception as e:
        raise CustomException(e, sys)



def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)