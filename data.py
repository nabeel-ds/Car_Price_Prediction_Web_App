# S6.1: Design the View Data page of the multipage app.
# Import necessary modules
import streamlit as st
import numpy as np  
import pandas as pd
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header("View Data")
  with st.beta_expander("View Dataset"):
    st.table(car_df)

# S6.2: Design the View Data page of the multipage app.
# Import necessary modules
import numpy as np  
import pandas as pd
import streamlit as st

# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(car_df)
    st.subheader("Columns description")
    if st.checkbox("Show summary"):
      st.table(car_df.describe())

# S6.3: Divide the web page into three columns to add more widgets.
def app(car_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(car_df)

    # Display descriptive statistics.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())    
    
    # ADD NEW CODE FROM HERE
    beta_column1,beta_column2,beta_column3=st.beta_columns(3)
    with beta_column1:
      if st.checkbox("Show all columns names "):
        st.table(list(car_df.columns))
    with beta_column2:
      if st.checkbox("View columns data type"):
        st.table(car_df.dtypes)
    with beta_column3:
      if st.checkbox("View columns data"):
        a = st.selectbox("Select columns",tuple(car_df.columns))
        st.write(car_df[a])