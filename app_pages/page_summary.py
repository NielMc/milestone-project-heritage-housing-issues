import streamlit as st

def summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f"* A **House** is a building that serves as living quaters for one or more families.\n" 
        f"* The **Sale Price** is the price at which the house will sell and is also the *target variable* for this study.\n"
        
    
        f"**Project Dataset**\n"
        f"* The dataset represents properties sold in Ames, Iowa.\"
        f"It contain varying data regarding the same 24 attributes which each property is measured against.\"
        f"We use this very data to complete our study of correlative features and fit the ML Model\"
        f"and in turn predict sale prices.\"
        f"Our target variable is the 'SalePrice'\"
        f""
        f"The currency in which the sale prices are recorded is the US Dollar")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/JessMair/milestone-project-heritage-housing-issues).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"* **Business Requirement 1**\n"

	    f"The client is interested in discovering the correlations between house prices "
        f"and the varying attributes that affect their value. " 
	    f"The client requires a dashboard that displays data visualizations of the correlated variable.\n"


        f"* **Business Requirements 2**\n"

	    f"The client wants to be able to predict the sale price of any property in Ames, Iowa;"
        f"including the inherited properties."
	    f"This will require the use of data analysis tools that allow the user to interact and amend variables 2"
        f"in order to generate price predictions."
	    f"A machine learning Pipeline will also need to be deployed as a part of the 2nd business requirement."
        )