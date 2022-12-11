import streamlit as st
from app_pages.multi_pages import MultiPage

# load pages scripts
from app_pages.page_summary import summary_body
from app_pages.page_hypothesis import hypothesis_and_validation
from app_pages.page_correlation import study
from app_pages.page_predict import prediction_tool
from app_pages.page_metrics import ml_prediction_metrics

app = MultiPage(app_name= "Heritage Housing")
# # Add your app pages here using .add_page()
app.add_page("Project Summary", summary_body)
app.add_page("Hypothesis and Validation", hypothesis_and_validation)
app.add_page("Correlation Study of House Prices", study)
app.add_page("House Price Prediction", prediction_tool)
app.add_page("ML: ML Prediction Metrics", ml_prediction_metrics)

app.run() # Run the  app