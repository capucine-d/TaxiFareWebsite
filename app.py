import streamlit as st
import datetime
import requests
import pandas as pd
'''
# Welcome to Taxi Calculator
'''

st.markdown('''
Get an estimate of the price you'll pay for your taxi
''')

'''
##  Please enter your trip information:
'''
date = st.date_input("Select a date", datetime.date(2021, 2, 19))

time = st.time_input('Select a time', datetime.time(16, 00))


pickup_longitude = st.text_input('Enter pickup longitude', '40.7128')
pickup_latitude = st.text_input('Enter pickup latitude', '74.0060')

dropoff_longitude = st.text_input('Enter dropoff longitude', '40.7128')
dropoff_latitude = st.text_input('Enter dropoff latitude', '74.0060')

passenger_count = st.number_input('Insert a number of passengers')

'''
##  Trip Summary:
'''
st.write('Your trip will take place on ', date,
         'at ',time, 'with', int(passenger_count) ,'passenger(s)')
st.write('Pickup location: ', '(', pickup_longitude,' ,',pickup_latitude,')')
st.write('Dropoff location: ', '(', dropoff_longitude,' ,',dropoff_latitude,')')

url = 'https://api-taxifare-5sppn64aja-ew.a.run.app/predict_fare'
#url = 'http://localhost:8000/predict_fare'


params = {
        'key': 'key',
        'pickup_datetime': f'{date} {time} UTC',
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': int(passenger_count)
        }

response = requests.get(url, params)
prediction = response.json()['prediction']

'''
## Find out your taxi fare
'''

st.write('Predicted fare:', prediction)
