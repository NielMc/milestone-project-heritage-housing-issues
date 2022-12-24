# Heritage Housing Issues

This is my 5th and final project for the Code Institute "Full Stack Dveloper" Diploma. 
Predictive Analytics is something which has always interested me and I have been very excited to reach this point in the course. I had longed to learn and practice these skills, as well as gain an understanding into a world which fascinates me. I present my [first ever dashboard,](https://heritagehouse.herokuapp.com/) but certainly not my last. 

![Head image](media/amiresponsive.png)

---
# Table of Contents
<details>
<summary>Table of Contents</summary>

* [Dataset Content](#dataset-content)
* [Business Requirements](#business-requirements)
* [User Stories](#user-stories)
* [Hypothesis and how to validate?](#hypothesis-and-how-to-validate?)
* [Rationale to map the business requirements to the Data Visualizations and ML tasks](#rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks) 
* [ML Business Case](#ml-business-case)
* [Dashboard Design](#dashboard-design)
* [Bugs](#bugs)
* [Deployment](#deployment)  
* [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries) 
* [Credits](#credits)  
</details>
<hr>

---
## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). 
We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 

* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|



## Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.

2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.



## Hypothesis and how to validate?

- Hypothesis 1 - The larger the square footage of the property the higher the price 
        * By studying correlations between the size of the property (in square footage) and the sale value, we will be able to observe if this variable is a factor that influences price. 

        - A correlation study will help with validating this. We will use relevant data visualisation tools here. 

- Hypothesis 2 - The more recent the property build, the higher the property sale price/value (null hypothesis)
        * We will study data regarding the house build data and observe whether it correlates with a higher house value. 
       
        - A correlation study will help with validating this. We will use relevant data visualisation tools here.

- Hypothesis 3 - The better the overall quality of the property, the higher the price
        * We will check whether a property that has been rated as having a higher "overall quality" will also be higher in value 
       
        - A correlation study will help with validating this. We will use relevant data visualisation tools here.


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* ### Business Requirement 1: Data Visualisation and Correlation Study 


* ### Business Requirement 2: Regression Pipeline 


## ML Business Case
* We want to build an ML Model that will predict the sale price of a house in Ames, Iowa. 


## Dashboard Design

### Page 1 
### Project Summary 

![summary](media/p1.png)


### Page 2
### Sale Price Correlation Study 
![study](media/p2.png)

### 
![plot1](media/p2part1.png)
![plot2](media/p2part2.png)
![plot3](media/p2part3.png)
![plot4](media/p2part4.png)

### Page 3
### Estimate House Price
![predicthouse](media/p3.png)

### Page 4
### Hypothesis
![hypothesis](media/p4.png)

### Page 5
### ML Pipeline
![mlpipe](media/p5.png)
![mlpipe2](media/p5part2.png)

## Epics
* Information gathering and data collection.

* Data visualization, cleaning, and preparation.

* Model training, optimization and validation.

* Dashboard planning, designing, and development.

* Dashboard deployment and release.



## Unfixed Bugs
### Inherited house dataset

![housedata](media/inheritedhouses.png)
I had a bit of a struggle initially trying to link the kaggle dataset, however after much trouble shooting and with the help of Neil, I was able to pull through the dataset. I Checked the data and all seemed well. However when I developed the 'House Price Prediction' page of the dashboard, I found that the data being pulled through under the inherited houses file was infact a duplicate of the full dataset. After I had completed the rest of the dashboard, I tried to pull the kaggle dataset once again to correct this error, but then realsied that the steps would have to be repeated with the dataset. This would take sometime and there is a possibility of other issue cropping up and this was not a risk I wanted to take. 
This is something I would definetly correct when time permits, however for nthe time being it seemed sensible to explain what had happened and that I understand what the error is and how it needs to be corrected in the future. 

### Deployment fail 
I had orginally successfully deployed the application to via Heroku when I first started reating the dashboard. This was done in the hopes that there will be no issues further down the line when time is of the essence. However, it is sods law that a dpendency issue cropped up when I went to check the application via Heroku prior to submission. This happened when there was no tutor support available to help troubleshoot the problem. My mentor, Mo Shami spent a good 45 mins trying to help me with this, however we were unsuccesfull. 

![Herokuerror](media/deployissue.png)

The issue really came down to the incompatbility between numpy version 1.18.5 and the other packages. I tried changing the version a few times but more compatibility issues with numpy kept cropping up. I tried version 1.20.0 and version 1.21.5 and I believe 1.21.0 also. I reverted back to the original 1.18.5 version of numpy as Heroku says the deployment has been successful but upon opening the app there is an error page stating "ModuleNotFoundError: No Module named 'numpy.random.bit_generator'. 

![Herokuissue](media/deploymentheroku.png)

Naturally I did my best to resolve this issue. I was very disappointed that it could not be resolved. This is something I will revisit again in the future, once permitted to ensure that the site is live. 





## Deployment
### Heroku

* The App live link is: https://heritagehouse.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App

2. At the Deploy tab, select GitHub as the deployment method.

3. Select your repository name and click Search. Once it is found, click Connect.

4. Select the branch you want to deploy, then click Deploy Branch.

5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.


## Technologies used 
* Github - 
* Gitpod - Used as a local workspace 
* Streamlit - To develop and display dashboard
* Heroku - 

## Languages used
* Python 

## Refrences
https://pythonguides.com/how-to-find-duplicates-in-python-dataframe/ - Checking for duplicated data  


https://pip.pypa.io/en/stable/topics/dependency-resolution/ - 'Dependency hell', troubleshooting deployment issue. 
https://stackoverflow.com/questions/72157517/error-resolutionimpossible-error-when-deploying-web-application-on-aws-beanstal- Trouble shhooting deployment issue. 

## Credits 

- Kaggle - dataset on which the study was based
- Code Institute - for the learning materials and template for the project
- 
* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)



## Acknowledgements (optional)
* I would like to thank Neil McEwen of Code Institute for his patience and assitance with my many queries on slack


