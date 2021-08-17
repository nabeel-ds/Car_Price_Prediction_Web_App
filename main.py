import streamlit as st

# Configure your home page.
st.set_page_config(page_title = 'Car Price Prediction',
                    page_icon = ':car:',
                    layout = 'centered',
                    initial_sidebar_state = 'auto'
                    )

# Importing the necessary Python modules.
import numpy as np
import pandas as pd

# Dictionary containing positive integers in the form of words as keys and corresponding former as values.
words_dict = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "eight": 8, "twelve": 12}
def num_map(series):
    return series.map(words_dict)

# Loading the dataset.
@st.cache()
def load_data():
    # Reading the dataset
    cars_df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/car-prices.csv")
    # Extract the name of the manufactures from the car names and display the first 25 cars to verify whether names are extracted successfully.
    car_companies = pd.Series([car.split(" ")[0] for car in cars_df['CarName']], index = cars_df.index)
    # Create a new column named 'car_company'. It should store the company names of a the cars.
    cars_df['car_company'] = car_companies
    # Replace the misspelled 'car_company' names with their correct names.
    cars_df.loc[(cars_df['car_company'] == "vw") | (cars_df['car_company'] == "vokswagen"), 'car_company'] = 'volkswagen'
    cars_df.loc[cars_df['car_company'] == "porcshce", 'car_company'] = 'porsche'
    cars_df.loc[cars_df['car_company'] == "toyouta", 'car_company'] = 'toyota'
    cars_df.loc[cars_df['car_company'] == "Nissan", 'car_company'] = 'nissan'
    cars_df.loc[cars_df['car_company'] == "maxda", 'car_company'] = 'mazda'
    cars_df.drop(columns= ['CarName'], axis = 1, inplace = True)
    cars_numeric_df = cars_df.select_dtypes(include = ['int64', 'float64']) 
    cars_numeric_df.drop(columns = ['car_ID'], axis = 1, inplace = True)
    # Map the values of the 'doornumber' and 'cylindernumber' columns to their corresponding numeric values.
    cars_df[['cylindernumber', 'doornumber']] = cars_df[['cylindernumber', 'doornumber']].apply(num_map, axis = 1)
    # Create dummy variables for the 'carbody' columns.
    car_body_dummies = pd.get_dummies(cars_df['carbody'], dtype = int)
    # Create dummy variables for the 'carbody' columns with 1 column less.
    car_body_new_dummies = pd.get_dummies(cars_df['carbody'], drop_first = True, dtype = int)
    # Create a DataFrame containing all the non-numeric type features.
    cars_categorical_df = cars_df.select_dtypes(include = ['object'])
    #Get dummy variables for all the categorical type columns using the dummy coding process.
    cars_dummies_df = pd.get_dummies(cars_categorical_df, drop_first = True, dtype = int)
    #  Drop the categorical type columns from the 'cars_df' DataFrame.
    cars_df.drop(list(cars_categorical_df.columns), axis = 1, inplace = True)
    # Concatenate the 'cars_df' and 'cars_dummies_df' DataFrames.
    cars_df = pd.concat([cars_df, cars_dummies_df], axis = 1)
    #  Drop the 'car_ID' column
    cars_df.drop('car_ID', axis = 1, inplace = True)
    final_columns = ['carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price']
    return cars_df[final_columns]
  
final_cars_df = load_data()

import home
import data
import plots
import predict

# create a dictionary 'pages_dict'
pages_dict = {
                "Home": home,
                "View Data": data, 
                "Visualise Data": plots, 
                "Predict": predict
            }

# Add radio buttons in the sidebar for navigation and call the respective pages based on 'user_choice'.
st.sidebar.title('Navigation')
user_choice = st.sidebar.radio("Go to", tuple(pages_dict.keys()))
if user_choice == "Home":
    home.app() # The 'app()' function should not take any input if the selection option is "Home".
else:
    selected_page = pages_dict[user_choice]
    selected_page.app(final_cars_df) 

