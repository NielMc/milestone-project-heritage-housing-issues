import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_project_summary
from app_pages.page_business_two import page_business_requirement_one
from app_pages.page_business_two import page_business_requirement_two
from app_pages.page_project_hypothesis import page_project_hypothesis_and_validation
from app_pages.page_correlation_study import page_correlation_study_and_data_visulisation
from app_pages.page_predict import page_house_price_prediction_tool
from app_pages.page_metrics import page_ml_prediction_metrics

app = MultiPage(app_name= "Heritage") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_project_summary)
app.add_page("Business Requirement One", page_business_requirement_one)
app.add_page("Business Requirement Two", page_business_requirement_two)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_and_validation)
app.add_page("ML: Correlation Study and Data Visualtion",page_correlation_study_and_data_visulisation)
app.add_page("ML: House Price Prediction", page_house_price_prediction_tool)
app.add_page("ML: ML Prediction Metrics", page_ml_prediction_metrics)

app.run() # Run the  app