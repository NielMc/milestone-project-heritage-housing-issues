#The code for this file has been taken from churnometer, page prospect with amendments made

import streamlit as st
import pandas as pd
from src.data_management import load_house_data, load_pkl_file, load_inherited_house_data
from src.machine_learning.predictive_analysis_ui import predict_sale_price
from datetime import date

def prediction_tool():
	
# load predict sale_price files

    version = 'v1'
    regressor_pipeline = load_pkl_file(f"outputs/ml_pipeline/predict_saleprice/{version}/regressor_pipeline.pkl")
    house_features = (pd.read_csv(f"outputs/ml_pipeline/predict_saleprice/{version}/X_train.csv")
                            .columns
                            .to_list())


st.write("### Predict House Sale Price")
st.info(
        f"* The client is interested in being able to predict the sale price for her 4 inherited properties. "
        f" In addition to this, she also wishes to be able to predict the price of any other house in Ames, Iowa"
	)
st.write("---")

	
# Generate Live Data
X_live = DrawInputsWidgets()


# predict on live data
if st.button("Run Predictive Analysis"): 
    predict_sale_price(X_live, house_features, sale_price_pipeline)
		churn_prediction = predict_churn(X_live, churn_features, churn_pipe_dc_fe, churn_pipe_model)
		
		if churn_prediction == 1:
			predict_tenure(X_live, tenure_features, tenure_pipe, tenure_labels_map)

		predict_cluster(X_live, cluster_features, cluster_pipe, cluster_profile)
			



def check_variables_for_UI(tenure_features, churn_features, cluster_features):
	import itertools

	# The widgets inputs are the features used in all pipelines (tenure, churn, cluster)
	# We combine them only with unique values
	combined_features = set(
		list(
			itertools.chain(tenure_features, churn_features, cluster_features)
			)
		)
	st.write(f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")



def DrawInputsWidgets():

	# load dataset
	df = load_telco_data()
	percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets only for 6 features	
	col1, col2, col3, col4 = st.beta_columns(4)
	col5, col6, col7, col8 = st.beta_columns(4)

	# We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result
	# {'InternetService', 'Contract', 'OnlineBackup', 'PhoneService', 'MonthlyCharges', 'PaymentMethod'}
		

	# create an empty DataFrame, which will be the live data
	X_live = pd.DataFrame([], index=[0]) 
	
	# from here on we draw the widget based on the variable type (numerical or categorical)
	# and set initial values
	with col1:
		feature = "Contract"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget


	with col2:
		feature = "InternetService"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col3:
		feature = "MonthlyCharges"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget

	with col4:
		feature = "PaymentMethod"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col5:
		feature = "OnlineBackup"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	with col6:
		feature = "PhoneService"
		st_widget = st.selectbox(
			label= feature,
			options= df[feature].unique()
			)
	X_live[feature] = st_widget

	# st.write(X_live)

	return X_live