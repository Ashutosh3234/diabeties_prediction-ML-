
# DIABETES PREDICTION USING MACHINE LEARNING

This project is a machine learning project in which the diabetes is predicted by using various ML algorithms and checking accuracy
of each of the algorithms.


## Problem Statement:

 - Diabetes is a common disease which occurs when your blood glucose (blood sugar) is too high. Blood glucose is your main source of energy and comes from the food you eat. A diabetic patient either produces low amounts of Insulin, a hormone made by the pancreas which helps the glucose from food get into your cells in order to be used as energy, or their body is incapable of using this insulin well. 
- There are three main types of diabetes - Type 1, Type 2 and Gestational, all of which require treatment and if detected at an early stage, can be treated properly while avoiding any further complications associated with them



## Dataset 

- https://www.kaggle.com/datasets/mathchi/diabetes-data-set
- The dataset is from kaggle and I have also collected some data from the hospitals around my town.
- the data set contains the columns which contains the information of patients related to diabetes from the hosspitals.
It contains 9 columns as:

Pregnancies: Number of times pregnant.

Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test

BloodPressure: Diastolic blood pressure (mm Hg)

SkinThickness: Triceps skin fold thickness (mm)

Insulin: 2-Hour serum insulin (mu U/ml)

BMI: Body mass index (weight in kg/(height in m)^2)

DiabetesPedigreeFunction: Diabetes pedigree function

Age: Age (years)

Outcome: Class variable (0 or 1)
![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/dataset.png?raw=true)




## Algorithms Used:


-Logistic Regression

-Random Forest and decision tree

-KNN





## Methedology

Perform EDA on Dataset i.e. remove null values and insert median in place of them

Generate the correlation matrix, pair plots and box-plots.

Split the train test data.

Normalize the training data with min-max scalar.

Perform machine learning Algorithm's mention above.

Check the accuracy and the confusion matrix.

Calculate the F1 score.

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/methedology.png?raw=true)





## Performing EDA

EDA stand for exploratory data analysis,in which many operations on the data is done and data is been clean.

EDA is basically data modelling of the data in which varios relations between the columns is observed and the unnecessary data is been removed.

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/EDA/EDA%201.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/EDA/EDA2.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/EDA/EDA%203.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/EDA/EDA%204.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/EDA/EDA%205.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/EDA/EDA%206.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/EDA/EDA%207.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/EDA/EDA%208.png?raw=true)



## Using Logistic Regression 

Logistic regression is one of the most popular Machine Learning algorithms, which comes under the Supervised Learning technique.

It is used for predicting the categorical dependent variable using a given set of independent variables.

Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value.

It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.

Logistic Regression is much similar to the Linear Regression except that how they are used.

Linear Regression is used for solving Regression problems, whereas Logistic regression is used for solving the classification problems.

In Logistic regression, instead of fitting a regression line, we fit an "S" shaped logistic function, which predicts two maximum values (0 or 1).

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/logistic/Screenshot%202023-03-27%20134435.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/logistic/logistic%202.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/logistic/logistic%203.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/logistic/logistic%204.png?raw=true)


## Using KNN

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/knn/knn1.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/knn/knn%202.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/knn/knn%203.png?raw=true)





## Using Random Forest

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/rf/rf%201.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/rf/rf%202.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/rf/rf%203.png?raw=true)

![Login](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/rf/rf%204.png?raw=true)





## Final Outcome

We have perform the ML operations using Logistic Regression,KNN and random forest classifier.

We have got the different accuracy and f1 scores from different algorithms.

![Final](https://github.com/Ashutosh3234/diabeties_prediction-ML-/blob/master/ScreenShots/final.png?raw=true)

