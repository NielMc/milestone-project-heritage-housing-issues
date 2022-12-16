import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.evaluate_regressor import regression_performance, regression_evaluation_plots

"""
Hard copy of code from churnometer - predict tenure notebook. 
Adjustments havev been made to reflect data from the current study
"""

def p5_ml_predictor ():

    st.write("### ML Predict")

    # load pipeline files
    version = 'v1'
    regressor_pipeline = load_pkl_file(f"outputs/ml_pipeline/predict_saleprice/{version}/regressor_pipeline.pkl")
    house_features = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
    sale_price_importance = plt.imread(f"outputs/ml_pipeline/predict_saleprice/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/y_train.csv")
    y_test = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/y_test.csv")

 

    st.write("### ML Pipeline: Predict Sale Price")    
    # display pipeline training summary conclusions
    st.info(
        f"* The ML Pipeline has been deployed to answer the **second business requirment**: \n\n"
        f"* Delivering an ML system capable of relaibly predicting the sale price of "
        f"the four inherited houses. \n\n"
        f"* We decided that a **Regressor model** would be best for predicting "
        f"the **Sale Price** of the houses. "
        f"We have completed further data cleaning and feature engineering steps to achieve the current results. "
        f"The client requires an R2 score of at least 0.75 on both train and test sets \n\n"
        f"* We have successfully met this requirement with an R2 score of **0.93** on the test and  "
        f"**0.83** on the train set. \n\n"
    )

    st.write("---")

    # show pipeline steps
    st.write("* ML pipeline to predict Sale Price")
    st.write(regressor_pipeline)
    st.write("---")

    # show best features
    st.write("* The features the model was trained and their importance")
    st.write(X_train.columns.to_list())
    st.image(sale_price_importance)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=regressor_pipeline)