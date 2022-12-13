import streamlit as st

def summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f"* A **House** is .\n"
        f"* The **Sale Price** .\n"
        
    
        f"**Project Dataset**\n"
        f"* The dataset represents a . "
        f"Containing individual customer data on the products and services "
        f"(like internet type, online security, online backup, tech support), "
        f"account information (like contract type, payment method, monthly charges) "
        f"and profile (like gender, partner, dependents).")

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