import streamlit as st

def p1_summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.success(
        f"**Project Terms & Jargons** \n"
        f"* A **House** is a building that serves as living quarters for one or more families.\n\n"
        f"* The **Sale Price** is the price at which the house will sell and is also the *target variable* for this study.\n\n"
        f"Our client, Lydia Doe has received four houses as an inheritance. All four houses are located in Ames, Iowa, USA. "
        f"Lydia lives in Belgium and is not familiar with the property market in the USA. "
        f" We have been asked by our client to conduct a business case assessment to qualify which attributes "
        f"correlate with sale price. Data visualisations of correlated variable are required. "
        f"Our client also wishes to be able to predict the sums for which her 4 inherited properties would sell for as well "
        f"as the sale value of any other house in Ames, Iowa.\n\n"

    # copied from README file - "Business Requirements" section
        f"Here are the two business requirements which we need to fulfill: \n\n"
        f"* **Business Requirement 1**\n"

	    f"The client is interested in discovering the correlations between house prices "
        f"and the varying attributes that affect their value. " 
	    f"The client requires a dashboard that displays data visualizations of the correlated variable.\n\n"


        f"* **Business Requirements 2**\n"

	    f"The client wants to be able to predict the sale price of any property in Ames, Iowa; "
        f"including the inherited properties. \n"
	    f"This will require the use of data analysis tools that allow the user to interact and amend variables "
        f"to generate price predictions. "
	    f"A machine learning Pipeline will also need to be deployed as a part of the 2nd business requirement."
        )
    
    
    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/JessMair/milestone-project-heritage-housing-issues). "
        )
    

    st.info(
            
        f"**Project Dataset**\n"
        f"* The **dataset** represents properties sold in Ames, Iowa. "
        f"Here is a link to the live dataset from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data). "
        f"It contains varying data regarding the same 24 attributes which each property is measured against. "
        f"We use this very data to complete our study of correlative features and fit the **ML Model** "
        f"and in turn predict the sale prices of properties in that area. "
        f"Our **target** variable is the **'SalePrice'**. "
        f"The currency in which the sale prices are recorded is the US Dollar "
        )