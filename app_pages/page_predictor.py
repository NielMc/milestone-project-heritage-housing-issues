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

    if st.button("Run Predictive Analysis"):
        predict_sale_price(DrawInputsWidgets(), house_features, sale_price_pipeline)

    st.write("---")
    st.write("Below we have the information the client requires regarding the sale price of "
    "of the clients inherited houses")

    in_df = load_inherited_house_data()
    filtered_df = in_df[['OverallQual', 'GrLivArea', 'YearBuilt', 'TotalBsmtSF', 'GarageArea']]

    st.write(filtered_df)

    st.write("The data pertaining to the inherited house was processed through the prediction application. "
        "Here are the figures of their estimated value: \n\n "
            "* $126,449 \n "
          "* $150,322 \n "
          "* $170,148 \n "
          "* $181,897 ")

    st.write("---")

def DrawInputsWidgets():

# load dataset
  df = load_house_data()
  percentageMin, percentageMax = 0.4, 2.0

# We create input widgets only for 6 features
  col1, col2, col3 = st.beta_columns(2)
  col4, col5 = st.beta_columns(2)

# We are using these features to feed the ML pipeline
# Create an empty DataFrame, which will be the live data

  X_live = pd.DataFrame([], index=[0])
    
  """from here on we draw the widget based on the variable type (numerical or categorical)
  # and set initial values"""

with col1:
    feature = "OverallQual"
    st_widget = st.number_input(
        label= feature,
        min_value= 0,
        max_value= 10,
        value= df[feature].median()
        )

(DrawInputsWidgets())[feature] = st_widget

with col2:
    feature = "GrLivArea"
    st_widget = st.number_input(
        label= feature,
        min_value= df[feature].min()*percentageMin,
        max_value= df[feature].max()*percentageMax,
        value= int(df[feature].median())
        )

(DrawInputsWidgets())[feature] = st_widget

with col3:
  feature = "YearBuilt"
  st_widget = st.number_input(
    label= feature,
    min_value= df[feature].min()*percentageMin,
    max_value= df[feature].max()*percentageMax,
    value= df[feature].median()
    )

(DrawInputsWidgets())[feature] = st_widget

with col4:
  feature = "TotalBsmtSF"
  st_widget = st.number_input(
    label= feature,
    min_value= df[feature].min()*percentageMin,
    max_value= df[feature].max()*percentageMax,
    value= df[feature].median()
    )

(DrawInputsWidgets())[feature] = st_widget

with col5:
  st_widget = st.number_input(
  label= feature,
    min_value= df[feature].min()*percentageMin,
    max_value= df[feature].max()*percentageMax,
    value= df[feature].median()
    )
    
(DrawInputsWidgets())[feature] = st_widget

# st.write(X_live)

#return X_live
