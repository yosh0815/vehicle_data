#importing necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

#reading dataframe
vehicles_df = pd.read_csv("https://github.com/yosh0815/vehicle_data/blob/main/vehicles_us.csv")

#changing null values from the 4wd columns to 0 to show which cars are not 4wd
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna(0)

#adding a manufacturer column
vehicles_df['manufacturer'] = vehicles_df['model'].apply(lambda x: x.split()[0])

#creating a display for the dataframe information
st.header('Data Viewer') 
st.dataframe(vehicles_df)

#histogram of model years per manufacturer
st.header('Model Year by Manufacturer')
manufacturer_year = px.histogram(vehicles_df, title='Model Year by Manufacturer', x='model_year', color='manufacturer')
st.write(manufacturer_year)

#scatterplot of price vs time listed
st.header('Price vs Days Listed')
price_days = px.scatter(vehicles_df, title='Price vs Days Listed', x='days_listed', y='price', opacity=.5)
st.write(price_days)

#scatterplot of price vs manufacturer with checkboxes to select transmission type
st.header('Price by Manufacturer with Transmission Filter')
auto = st.checkbox('Automatic Transmission', value=True)
if auto:
    transmission_df = vehicles_df[vehicles_df['transmission'] == 'automatic']
else:
    transmission_df = vehicles_df[vehicles_df['transmission'] != 'automatic']
transmission_fig = px.scatter(transmission_df, title='Car Price by Manufacturer', x='manufacturer', y='price', opacity=.5)
st.write(transmission_fig)