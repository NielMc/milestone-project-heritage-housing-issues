import streamlit as st
from app_pages.multi_pages import MultiPage
from app_pages.page_summary import summary_body
from app_pages.page_sale_price_study import study
from app_pages.page_predict import predict_house_price
from app_pages.page_hypothesis import hypothesis_and_validation
from app_pages.page_ml_predict import ml_predictor

app = MultiPage(app_name= "Heritage Housing")
app.add_page("Project Summary", summary_body)
app.add_page("Sale Price Correlation Study", study)
app.add_page("House Price Prediction", predict_house_price)
app.add_page("Hypothesis and Validation", hypothesis_and_validation)
app.add_page("ML Model", ml_predictor)

app.run() # Run the  app