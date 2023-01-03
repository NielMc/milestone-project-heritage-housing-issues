import streamlit as st
from src.data_management import load_house_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import numpy as np
import plotly.express as px

def p2_study ():

    # load data
    df = load_house_data()

    vars_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', 'TotalBsmtSF', 'GarageArea']

    df_corr_pearson, df_corr_spearman = CalculateCorrAndPPS(df)


    st.write("### Sale Price Correlation Study")
    st.info(
        f"We will address the **first busines requirement.** \n\n"
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
        f"In conclusion: \n\n"
        f""
    )

# Code copied from 'Sale_Price_study' notebook - Data visualisation section
    df_eda = df.filter(vars_to_study + ['SalePrice'])
    if st.checkbox("Correlation of variable to Sale Price"):
        correlation_to_sale_price(df_eda, vars_to_study)


# Correlation heatmaps 

    if st.checkbox("Pearson Correlation"):
        heatmap_corr(df=df_corr_pearson, threshold=0.4,
                     figsize=(20, 12), font_annot=12)

    if st.checkbox("Spearman Correlation"):
        heatmap_corr(df=df_corr_spearman, threshold=0.4,
                     figsize=(20, 12), font_annot=12)




# Copied from Data_cleaning notebook - correlation and pps analysis 

def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


def correlation_to_sale_price(df_eda, vars_to_study):
    target_var = 'SalePrice'
    for col in ['GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")



def heatmap_corr(df,threshold, figsize=(20,12), font_annot = 8):
  if len(df.columns) > 1:
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True

    fig, axes = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                linewidth=0.5
                     )
    axes.set_yticklabels(df.columns, rotation = 0)
    plt.ylim(len(df.columns),0)
    st.pyplot(fig)


def heatmap_pps(df,threshold, figsize=(20,12), font_annot = 8):
    if len(df.columns) > 1:
      mask = np.zeros_like(df, dtype=np.bool)
      mask[abs(df) < threshold] = True

      fig, ax = plt.subplots(figsize=figsize)
      ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                       mask=mask,cmap='rocket_r', annot_kws={"size": font_annot},
                       linewidth=0.05,linecolor='grey')
      
      plt.ylim(len(df.columns),0)
      st.pyplot(fig)

def CalculateCorrAndPPS(df):
    df_corr_spearman = df.corr(method="spearman")
    df_corr_pearson = df.corr(method="pearson")


    return df_corr_pearson, df_corr_spearman

  

  