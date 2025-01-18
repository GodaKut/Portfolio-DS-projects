# DS.v3.2.3.4
# Red Wine Quality

The goal is to analyze the Red Wine Quality dataset and identify which variables influence perceived wine quality the most by fitting a statistical model.

### Objectives
* Practice choosing variables and their transformations for a model.
* Practice fitting a linear regression model.
* Practice interpreting a fitted model’s coefficients and communicating uncertainty around them.

## Conclusions
Alcohol content emerges as the strongest predictor of wine quality with a clear positive impact, whereas volatile acidity is the main negative influence. Sulphates and citric acid show some correlation with quality but are less reliable due to violations of key model assumptions, including issues with residual normality and non-linearity. Density and chlorides have minimal relevance due to the variance of quality being covered at around 4%. The findings highlight the importance of alcohol and volatile acidity in understanding wine quality while it must be acknowledged that the assumption has also been violated. In addition, since a sample ratio mismatch was detected between the "good" and "poor" quality of wines, insights from logistic regression should be taken with caution.

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

For more information see REQUIREMENTS.txt

### Datasets

Kaggel:
[Red Wine Quality dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)



## Authors

Goda Kutkeviciute 

## Version History

* 0.2 - final version. The issues fixed:
   * added scaling when calculating VIF.  
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details

