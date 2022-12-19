import streamlit as st
from src.data_management import load_house_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
from feature_engine.discretisation import ArbitraryDiscretiser
import numpy as np
import plotly.express as px

def p2_study ():

    # load data
    df = load_house_data()

    vars_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', 'TotalBsmtSF', 'GarageArea']

    st.write("### House Price Study")
    st.info(
        f"We will address the first busines requirement. \n\n"
        f"* The client is interested in discovering the patterns from the dataset pertaining to house sales in Iowa. "
        f"This is so that she is aware of which variable are correlated and their sale price "
    )

    # inspect data
    if st.checkbox("Inspect House Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")
        
        st.write(df.head(10))

    st.write("---")


    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to the 'SalePrice'. \n\n"
        f"* The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "Sale_Price_Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"We used Pearson and Spearman methods to check the levels of correlations "
        f"between all variables and their correlation against the sale price. "
        f"Both Pearson and Spearman revelaved the similar insights about the inter-relationship of the "
        f"variables. "
        f"* The 'SalePrice' was strongly correlated with 'OverallQual' and 'GrLivArea'. "
        f"These variables are a common factor in influencing property price in general. "
        f"We explored this further by testing our hypothesis: "
    )

# Code copied from 'Sale_Price_study' notebook - Data visualisation section
# Individual plots per variable

    if st.checkbox("Sale Price Distribution of Variables"):
        df_eda = df.filter(vars_to_study + ['SalePrice'])
        target_var = 'SalePrice'
        variable_corr(df_eda, target_var)

def variable_corr(df_eda, target_var):
    
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot_numerical(df_eda, col, target_var)


def plot_numerical(df, col, target_var, hue_order):
    fig, axes = plt.subplots(figsize=(8, 5))
    fig = sns.histplot(data=df, x=col, hue=target_var, hue_order=hue_order, kde=True, element="step") 
    plt.title(f"{target_var} distribution", fontsize=20, y=1.05)
    st.pyplot(fig)



