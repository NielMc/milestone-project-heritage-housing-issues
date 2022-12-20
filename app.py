import streamlit as st
from app_pages.multi_pages import MultiPage
from app_pages.page_summary import p1_summary_body
from app_pages.page_sale_price_study import p2_study
from app_pages.page_predictor import p5_widgets
from app_pages.page_hypothesis import p4_hypothesis_and_validation
from app_pages.page_ml_predict import p5_ml_predictor

app = MultiPage(app_name= "Heritage Housing")
app.add_page("Project Summary", p1_summary_body)
app.add_page("Sale Price Correlation Study", p2_study)
app.add_page("House Price Prediction", p5_widgets)
app.add_page("Hypothesis and Validation", p4_hypothesis_and_validation)
app.add_page("ML Model", p5_ml_predictor)

app.run() # Run the  app