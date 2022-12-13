"""
Hard copy of code from churnometer - predict tenure notebook. 
Adjustments havev been made to reflect data from the current study
"""


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.evaluate_regressor import regression_performance, regression_evaluation_plots

def ml_predictor ():

    st.write("### ML Predict")

    # load tenure pipeline files
    version = 'v1'
    regressor_pipeline = load_pkl_file(f"outputs/ml_pipeline/predict_saleprice/{version}/regressor_pipeline.pkl")
    house_features = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
    sale_price_importance = plt.imread(f"outputs/ml_pipeline/predict_saleprice/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/y_train.csv")
    y_test =  pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/y_test.csv")

 

    st.write("### ML Pipeline: Predict Prospect Tenure")    
    # display pipeline training summary conclusions
    st.info(
        f"* Initially we wanted to have a Regressor model to predict tenure for a likely "
        f"churnable prospect, but the **regressor performance didn't meet project requirement**: "
        f"0.7 of R2 Score on train and test sets. "
        f"We converted the target to classes and transformed the ML task into a **classification** problem. \n"
        f"* The pipeline was tuned aiming at least 0.8 Recall on '<4 months' class, on train and test sets, "
        f"since we are interested in this project, to detect any prospect that may churn soon. "
        f"The classifer performance was 0.8 on both sets.\n"
        f"* We notice that '<4.0' and '+20.0' classes have reasonable levels of performance, where "
        f"'4.0 to 20.0' performance is poor. This will be a limitation of our project.")
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

