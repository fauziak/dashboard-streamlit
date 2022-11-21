import pandas as pd 
import numpy as np 
import streamlit as st 
import matplotlib.pyplot as plt

#Loading in datasets
nycparties_df = pd.read_csv('data/party_in_nyc.csv')
barlocations_df = pd.read_csv('data/bar_locations.csv')

#Creating a Header
st.header('NYC Noise Complaints')

#Creating a Histogram
st.subheader('Displaying NYC Party Complaints')
nycparties_df['Created Date'] = pd.to_datetime(nycparties_df['Created Date'])
# hist_values = 
hist_values = np.histogram(
   nycparties_df['Created Date'].dt.hour, bins=24, range=(0,24))[0] 

hist_values_df = pd.DataFrame({'Number of complaints': hist_values, 'Time': ['1am', '2am', '3am', '4am', '5am','6am','7am','8am','9am','10am','11am','12pm','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm','10pm','11pm', '12am']})
st.bar_chart(hist_values_df, x='Time', y='Number of complaints')
st.text('12am has the most complaints while 8am has the least')
st.write(hist_values_df)

hist_code = '''
hist_values_df = pd.DataFrame({'Number of complaints': hist_values, 'Time': ['1am', '2am', '3am', '4am', '5am','6am','7am','8am','9am','10am','11am','12pm','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm','10pm','11pm', '12am']})
st.bar_chart(hist_values_df, x='Time', y='Number of complaints')    
'''
st.code(hist_code, language='python')

# Creating a Scatter Plot
st.subheader('Scatter Plot on a Map Based on the Number of Calls and Latitude and Longitude')
scatterplot_df = barlocations_df[['Latitude', 'Longitude', 'num_calls']]
scatterplot_df = scatterplot_df.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})
st.map(scatterplot_df)

st.text('Manhattan has the most amount of complaints seen on the scatter plot')

st.write(scatterplot_df)
scatterplot_code = '''
scatterplot_df = barlocations_df[['Latitude', 'Longitude', 'num_calls']]
scatterplot_df = scatterplot_df.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})
st.map(scatterplot_df)    
'''
st.code(scatterplot_code, language='python')

