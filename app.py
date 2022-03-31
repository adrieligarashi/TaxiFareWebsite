import streamlit as st
import requests
from datetime import datetime
import pytz
import numpy as np
import pandas as pd


def predict(pickup_datetime='2012-10-06 12:10:20',
            pickup_longitude=40.7614327,
            pickup_latitude=-73.9798156,
            dropoff_longitude=40.6513111,
            dropoff_latitude=-73.8803331,
            passenger_count=2):

    # pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")


    # # localize the user datetime with NYC timezone
    # eastern = pytz.timezone("US/Eastern")
    # localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)

    # # localize the datetime to UTC
    # utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)

    # formatted_pickup_datetime = utc_pickup_datetime.strftime(
    #     "%Y-%m-%d %H:%M:%S UTC")


    key = datetime.now()

    params = {
        'key': key,
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }
    url = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(url, params=params)

    return response.json()


'''
# TaxiFareModel front
'''



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Taxi Value Calculator'
    )



date_pickup = st.date_input("Date Pickup", datetime(2012, 10, 6))

time_pickup = st.time_input(
    'Hour pickup',
    datetime(date_pickup.year, date_pickup.month, date_pickup.day, 8, 45))

datetime_pickup = datetime(date_pickup.year, date_pickup.month,
                           date_pickup.day, time_pickup.hour, time_pickup.minute)

pickup_datetime = datetime_pickup.isoformat()

pickup_longitude = st.number_input('Pickup Longitude', value=40.7614327)
pickup_latitude = st.number_input('pickup Latitude', value=-73.9798156)
dropoff_longitude = st.number_input('Dropoff Longitude', value=40.6513111)
dropoff_latitude = st.number_input('Dropoff Latitude', value=-73.8803331)
passenger_count = st.number_input('Passenger Count', value=2)


# pickup_datetime = datetime.strptime(datetime_pickup.isoformat(),
#                                     "%Y-%m-%d %H:%M:%S")
# st.write(pickup_datetime)



if st.button('Predict ! ! !'):
    pred = predict(pickup_datetime=pickup_datetime,
                   pickup_longitude=pickup_longitude,
                   pickup_latitude=pickup_latitude,
                   dropoff_longitude=dropoff_longitude,
                   dropoff_latitude=dropoff_latitude,
                   passenger_count=passenger_count)
    st.write(pred)
else:
    st.write('Goodbye')







# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import requests
# import pandas as pd
# from datetime import datetime
# import pytz
# import joblib


# def predict(pickup_datetime,
#             pickup_longitude,
#             pickup_latitude,
#             dropoff_longitude,
#             dropoff_latitude,
#             passenger_count):
# ​
#     # create a datetime object from the user provided datetime
#     pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
# ​
#     # localize the user datetime with NYC timezone
#     eastern = pytz.timezone("US/Eastern")
#     localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)
# ​
#     # localize the datetime to UTC
#     utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
# ​
#     formatted_pickup_datetime = utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")
# ​
#     key = datetime.now()
# ​
#     values = {
#         'key': key,
#         'pickup_datetime': formatted_pickup_datetime,
#         'pickup_longitude': pickup_longitude,
#         'pickup_latitude': pickup_latitude,
#         'dropoff_longitude': dropoff_longitude,
#         'dropoff_latitude': dropoff_latitude,
#         'passenger_count': passenger_count
#     }
# ​
#     X = pd.DataFrame(values, index=[0])
# ​
#     #return {'oi': f'{key}'}
#     #return X.to_dict()
# ​
#     modelo = joblib.load('./model.joblib')
# ​
#     previsao = modelo.predict(X)[0]
# ​
# ​
#     return {'fare': previsao}
