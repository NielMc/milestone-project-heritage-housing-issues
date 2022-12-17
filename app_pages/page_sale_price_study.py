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
        f"We explored this further:"
    )


 # Individual plots per variable
    if st.checkbox("Churn Levels per Variable"):
        churn_level_per_variable(df_eda)
        
    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(f"* Information in yellow indicates the profile from a churned customer")
        parallel_plot_churn(df_eda)


# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,order = df[col].value_counts().index)
    plt.xticks(rotation=90) 
    plt.title(f"{col}", fontsize=20,y=1.05)        
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()


# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True,element="step") 
    plt.title(f"{col}", fontsize=20,y=1.05)
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()



# function created using "02 - Churned Customer Study" notebook code - Parallel Plot section
def parallel_plot_churn(df_eda):

    tenure_map = [-np.Inf, 6, 12, 18, 24, np.Inf] # hard coded from "disc.binner_dict_['tenure']"" result,
                                                  # found at "02 - Churned Customer Study" notebook
                                                  # under "Parallel Plot" section
    disc = ArbitraryDiscretiser(binning_dict={'tenure': tenure_map})
    df_parallel = disc.fit_transform(df_eda)
    
    n_classes = len(tenure_map) - 1
    classes_ranges = disc.binner_dict_['tenure'][1:-1]
    LabelsMap = {}
    for n in range(0,n_classes):
        if n == 0: LabelsMap[n] = f"<{classes_ranges[0]}"
        elif n == n_classes-1: LabelsMap[n] = f"+{classes_ranges[-1]}"
        else: LabelsMap[n] = f"{classes_ranges[n-1]} to {classes_ranges[n]}"


    df_parallel['tenure'] = df_parallel['tenure'].replace(LabelsMap)
    fig = px.parallel_categories(df_parallel, color="Churn", width=750, height=500)
    st.plotly_chart(fig)  # we use st.plotly_chart() to render, in notebook is fig.show()