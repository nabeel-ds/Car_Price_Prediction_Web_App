# Car_Price_Prediction_Web_App

# Overview:
- This is a simple machine learning web app capable of predicting the price of the car based on its technical specifications such as car manufacturer, its engine capacity, fuel efficiency, body-type (Selected using RFE)  etc. using streamlit and python. 
- It uses Linear Regression for predicting the prices of the car by taking inputs of Car Width, Engine Size, Horse Power etc from the users. 
- Results includes the predicted price of the car along with the performance metrics like Accuracy, R-squared score, Mean absolute error Mean squared log error, Root mean squared error of the model. 
- It also has the functionality to visualise the data for EDA. It can plot the plots like Scatterplot, Histogram, Boxplot and Correlation Heatmap.

#Technical Aspects: 
1- Collected the data from https://archive.ics.uci.edu/ml/datasets/Automobile. 
- Trained the ml model on this data on the streamlit framework also used various data exploration and various data preprocessing techniques along with the feature selection methods (RFE, p_value). 
2- Deploying the app on Heroku.
