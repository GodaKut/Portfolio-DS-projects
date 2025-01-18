# DS.v2.5.3.4.1

# Payment difficulties prediction

The goal is to predict payment difficulties by analyzing the datasets provided and composing a model that would make the predictions. 

### Objectives
* Practice translating business requirements into data science tasks.
* Practice performing EDA.
* Practice applying statistical inference procedures.
* Practice using machine learning to solve business problems.
* Practice deploying multiple machine learning models.

## Summary

This project successfully tackled the challenging task of predicting client payment difficulties using a highly imbalanced dataset. Key steps and insights gained throughout the process are as follows:
##### Data Exploration and Preparation
* A thorough exploratory data analysis revealed critical issues, including significant missingness, class imbalance, and multicollinearity, all of which were effectively addressed through imputation, feature selection, and strategic handling of imbalance.
* Feature engineering and selection emphasized the importance of nuanced financial indicators, such as AVG_INSTALMENT_DEBT and CREDIT_ACTIVE_COUNT, which emerged as strong predictors.
* Careful consideration of multicollinearity and VIF values ensured that only relevant, non-redundant features were retained for modeling.
##### Modeling and Performance
* Among several algorithms tested, CatBoost, LightGBM, and XGBoost emerged as top performers, balancing recall and AUCPR scores effectively to prioritize the identification of positive cases.
* Hyperparameter tuning via Bayesian Optimization further improved model performance, with XGBoost achieving the most significant recall improvement (+8.13%), followed by CatBoost and LightGBM, which maintained strong and stable results.
* SHAP value analysis facilitated refined feature selection, reducing feature sets while preserving predictive strength. CatBoost retained its position as the most consistent model, excelling in recall and true positive detection.
##### Deployment Readiness
* CatBoost was identified as the most reliable deployment candidate due to its consistent recall (0.687), superior ability to capture true positives, and robust performance across metrics.
The model’s interpretability, enhanced through SHAP value analysis, adds confidence to its deployment in decision-making scenarios, ensuring transparency and actionable insights.
##### Business Impact
The deployment of this model has the potential to significantly improve risk management processes by accurately identifying clients at risk of payment difficulties. This allows for targeted interventions, reducing financial losses while supporting clients in mitigating repayment challenges.


## Getting Started

### Dependencies


* python
* pandas
* numpy
* matplotlib
* seaborn
* scipy
* statsmodels
* scikit-learn
* xgboost
* catboost

For more information see REQUIREMENTS.txt

### Datasets

Internal Turing datasets:
[Datasets ZIP]((https://storage.googleapis.com/341-home-credit-default/home-credit-default-risk.zip)): https://storage.googleapis.com/341-home-credit-default/home-credit-default-risk.zip

### Deployments

* Local deployment files are in the GIT folder. Note that *.json key to access Google Platform Cloud bucket is not present on purpose.
* Public deployment in theory should work however  since I have chosen free Render option the limit of memory is 512 MB which is running out due to preprocesing pipeline being 2 GB. Deploying on Google Cloud was atempted however unsuccessful due to several reasons some of whch being that the Catboost cannot be packed to Tensorflow format, quota limitations being reached and others. 
  * Public deployment links:
    * [Streamlit app]((https://m3-capstone-banking.streamlit.app/)) : https://m3-capstone-banking.streamlit.app/
    * [FastAPI on Render]((https://m3-capstone-live.onrender.com/docs)) : https://m3-capstone-live.onrender.com/docs
    * Public GIT : https://github.com/GodaKut/m3_capstone_app/tree/main

## Authors

Goda Kutkeviciute 

## Version History
 
* 0.1
    * Initial Release
