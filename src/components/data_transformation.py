import os
import sys
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

# imports from sklearn
from sklearn.compose import ColumnTransformer
# simple imputer will help us with missing values
from sklearn.impute import SimpleImputer 

from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.pipeline import Pipeline

from src.utils import save_object

@dataclass 
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_obj(self):
        
        # this method will be responsible for data transformation

        try:
            
          num_columns = ["writing_score", "reading_score"]
          cat_columns = [
              "gender",
              "race_ethnicity",
              "parental_level_of_education",
              "lunch",
              "test_preparation_course"
              ]
          
          num_pipeline = ColumnTransformer(
              steps = [
                  ('imputer', SimpleImputer(strategy='median')),
                  ('standard scaler',StandardScaler())
                  # by using with_mean = False, The comment is false because setting with_mean=False does not ensure that there will be no negative values. It only means that the data will not be centered around zero, but it will still be scaled by the standard deviation, which can result in both positive and negative values depending on the original data.

              ]
          )

          cat_pipeline = ColumnTransformer(
              steps = [
                  ('simple imputer' , SimpleImputer(strategy='most_frequent')),
                  ('OneHotEncoder', OneHotEncoder),
                  ('standard scaler' , StandardScaler)
                  # Using StandardScaler after OneHotEncoder can help ensure that all features are treated equally by your model, leading to improved performance, especially for distance-based algorithms and models that rely on gradient descent. This preprocessing step is particularly important when your dataset contains a mix of numerical and categorical features
              ]
          )

          logging.info(f"Categorical columns: {cat_columns}")
          logging.info(f"Numerical columns: {num_columns}")

          preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,num_columns),
                ("cat_pipelines",cat_pipeline,cat_columns)
                # cmnt , pipleine,on which we are applying this pipeline

                ]


            )

          return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)

    
    def initiate_data_transformation(self , train_path , test_path):
        
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformation_obj()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=['math_score'] , axis = 1)
            target_feature_train_df = train_df['math_score']
            
            input_feature_test_df = test_df.drop(columns=['math_score'] , axis = 1)
            target_feature_test_df = test_df['math_score']

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            # .c_ is used to concatenate arrays column-wise. This means that it takes multiple arrays as input and stacks them as columns to form a single 2D array.
            
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                # this method has been called from utlis file inside src

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
            
        
        except :
            pass

