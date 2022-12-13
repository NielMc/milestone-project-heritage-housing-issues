import streamlit as st

"""
Prediction for pipeline trained on features that were most important
in effecting the house price
"""
def predict_sale_price(X_live, house_features, sale_price_pipeline):

    # from live data, subset features related to this pipeline
	X_live_churn = X_live.filter(house_features)

	# predict
	sale_price_prediction_proba = sale_price_pipeline_model.predict(X_live_price)
	
	# Create a logic to display the results
    
proba = sale_price_prediction_proba
value = float(proba.round(1))
amount = '${:,.2f}'.format(value)
statement = (
	f"### The value of your house is estimated to be {amount} "
)

st.write(statement)
		
st.write(proba)

return price_prediction