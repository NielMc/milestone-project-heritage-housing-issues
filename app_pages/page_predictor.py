import streamlit as st
import pandas as pd
from src.data_management import load_house_data, load_pkl_file, load_inherited_house_data
# from src.machine_learning.predictive_analysis_ui import predict_sale_price
# from datetime import date

def p5_widgets():
    #load required files
    version = 'v1'
    df_inherited = load_inherited_house_data()
    regressor_pipeline = load_pkl_file(f"outputs/ml_pipeline/predict_saleprice/{version}/regressor_pipeline.pkl")
    house_features = (pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
                            .columns
                            .to_list())

    st.write("### Predict House Sale Price")

    st.info(
    f"### Business requirement 2 \n\n"
    f"The client has requested a feature on the dashboard which enables her to "
    f"predict the value of any house in Ames, Iowa. \n\n"
    f"She also wishes to be able to predict the value of her own inherited houses. "
    f"We have designed and used a predictive tool to estimate the value of her 4 inherited properties. \n\n"
)

    st.write("---")

    st.write("We can use the toggles below to input and amend data to gain insights in the "
    "estimated house price. Please note, the values are set at a default of median value")

    # Generate Live Data