import streamlit as st

def p4_hypothesis_and_validation():

    st.write("### Project Hypothesis and Validation")

    st.info(
    f"We made **predictions** on what the data will reveal at the onset.\
    We will now conclude our **findings** with an **explanation** as to how these insights were achieved : \n\n"
    )


    st.success(
    f"**Hypothesis 1** - The larger the square footage of the property the higher the price\n"
    f" By studying correlations between the size of the property (in square footage) and the sale value,\
         we will be able to observe if this variable is a factor that influences price.\n\n"

    f"**Hypothesis 2** - The more recent the property build, the higher the property sale price/value (null hypothesis)\n"
    f" We will study data regarding the house build data and observe whether it correlates with a higher house value.\n\n"

    f"**Hypothesis 3** - The better the overall quality of the property, the higher the price \n\n"
    )