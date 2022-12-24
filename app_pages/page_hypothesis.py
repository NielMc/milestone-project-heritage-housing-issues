import streamlit as st

def p4_hypothesis_and_validation():

    st.write("### Project Hypothesis and Validation")

    st.info(
    f"We made **predictions** on what the data will reveal at the onset.\
    We will now conclude our **findings** with an **explanation** as to how these insights were achieved : \n\n"
    )


    st.success(
    f"**Hypothesis 1** - The larger the square footage of the property the higher the price\n\n"

    f" - By studying correlations between the size of the property (in square footage) and the sale value,\
         we were able to observe if this variable is a factor that influences price.\n\n"
    f" - Findings: **Correct** \n\n"
    f" - Explanation: The pearson correlation score points towards the fact that the size of the house "
    f" has a relatively high correlation to the value of the house. "
    f" The scatter plot and histogram we mapped, both illustrate that as the property size increases, "
    f" so does the sale price. \n\n"
    f"* The histogram plots show that where the 'GrLivArea', "
    f" '1stflrSF', 'GarageArea' and 'TotalBmntSF' have greater square footage the sale prices generally tend "
    f" to be higher. This supports our first hypothesis. \n\n"

    f" **Hypothesis 2** - The more recent the property build, the higher the property sale price/value "
    f"  We studied data regarding the year houses were built and observed whether it correlates with a higher house value.\n\n"
    f" - Findings: **Correct** \n\n"
    f" - Explanation: Observing the histogram, it is clear to see a significant difference in the house price of more recently built. "
    f" Although the price spike could be attributed to other factors too. This would make a good case for further exploration of the data. "
    f" However, on the face of it, the data does suggest a significant correlation between the year a property was built "
    f" and a higher value, thus supporting hypothesis 2. \n\n"

    f"**Hypothesis 3** - The better the overall quality of the property, the higher the price \n\n"
    f" - Findings: **Correct** \n\n"
    f" - Explanation: With a pearson score of 0.79 which strongly signals an influence of a high specification house on house price. "
    f" This was further supported by the histogram, which once again showed a clear indication of facts. "
    f" The highest priced houses were ranked of the highest 'Overall Quality'. "
    )