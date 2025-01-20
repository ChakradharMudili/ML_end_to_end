import pandas as pd
import numpy as np
import sys
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from data_ingestion import DataIngestion
from src.logger import logging
from src.exception import customException
from sklearn.compose import ColumnTransformer

class DataTransformation:
    def __init__(self):
        pass
    def data_transformation_intiate(self):
        try:
            logging.info("Data Transformation started")
            train_data_path, test_data_path = DataIngestion().initiate_data_ingestion()
            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)
            logging.info("Loaded train and test datasets")
            numeric_col = [i for i in train_data.columns if train_data[i].dtype!="object"]
            numeric_col.remove("math_score")
            catergorical_col = [i for i in train_data.columns if train_data[i].dtype =="object"]
            logging.info("Fetch Numeric columns and Categorical columns")
            X_train = train_data.drop("math_score", axis=1)
            X_test = test_data.drop("math_score", axis=1)
            y_train = train_data["math_score"]
            y_test = test_data["math_score"]
            logging.info("Split data to dependent and independent data")
            oh_encoder = OneHotEncoder()
            numeric_transformer = StandardScaler()
            logging.info("Loaded Label Encoders and standard scaler")
            preprocessor = ColumnTransformer(
                [
                    ("OneHotEncoder", oh_encoder, catergorical_col),
                    ("StandardScaler", numeric_transformer, numeric_col),        
                ]
            )
            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")
            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.fit_transform(X_test)

            return(
                X_train,
                X_test,
                y_train,
                y_test
            )
        
        except Exception as e:
            raise customException(e, sys)

if __name__ == "__main__":
    obj = DataTransformation()
    obj.data_transformation_intiate()



