import streamlit as st

def page_summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f"* A **house** is \n"
        f"* The **Sale Price** is the sum of money goods/services are sold for, which in this case are houses. \n "
        f"* A **jargon** is .\n"

        f"**Project Dataset**\n"
        f"* The dataset represents a **customer base from a Telco company**. "
        f"Containing individual customer data on the products and services "
        f"(like internet type, online security, online backup, tech support), "
        f"account information (like contract type, payment method, monthly charges) "
        f"and profile (like gender, partner, dependents).")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Code-Institute-Solutions/churnometer).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f""
        f""
        f""
        f""
        )