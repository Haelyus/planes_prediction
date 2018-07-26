from flask_wtf import Form
from wtforms import TextField, IntegerField, SubmitField, SelectField

from wtforms import validators, ValidationError

import numpy as np
import pandas as pd

# Liste des compagnies
L_Carriers = ['AA', 'AS', 'B6', 'DL', 'EV', 'F9', 'HA', 'NK', 'OO', 'UA', 'VX', 'WN']

# Liste des aéroports
df = pd.read_csv('carrier_counts.csv', sep=",", low_memory=False, error_bad_lines=False)

i = 0
L_airport = []
#df['CITY_NAME'].values.sort()
#for a in df['CITY_NAME'].values:
#    i += 1
#    L_airport.append((str(i), a))
df = df.sort_values(by = 'CITY_NAME')
for index, row in df.iterrows():
    L_airport.append((str(row['NB']), row['CITY_NAME']))	

class PlaneForm(Form):
    Carrier = SelectField('Carrier', choices = [(c, c) for c in L_Carriers])
	
    day = IntegerField("Day Of Departure",[validators.InputRequired("Please enter the day."), validators.NumberRange(min=1, max=31, message="Please enter the right day.")])
    month = IntegerField("Month Of Departure",[validators.InputRequired("Please enter the month."), validators.NumberRange(min=1, max=12, message="Please enter the right month.")])
    year = IntegerField("Year Of Departure",[validators.InputRequired("Please enter the year."), validators.NumberRange(min=1900, max=2900, message="Please enter the right year.")])
    
    distance = IntegerField("Distance (miles)",[validators.InputRequired("Please enter the distance."), validators.NumberRange(min=1, max=20000, message="Please enter the distance between 1 to 20 000.")])	
    
    hour_dep = IntegerField("Hour Of Departure",[validators.InputRequired("Please enter the hour of departure."), validators.NumberRange(min=0, max=23, message="Please enter the right hour of departure.")])
    min_dep = IntegerField("Minutes Of Departure",[validators.InputRequired("Please enter the minutes of departure."), validators.NumberRange(min=0, max=59, message="Please enter the right minutes of departure.")])
    
    hour_arr = IntegerField("Hour Of Arrival",[validators.InputRequired("Please enter the hour of arrival."), validators.NumberRange(min=0, max=23, message="Please enter the right hour of arrival.")])
    min_arr = IntegerField("Minutes Of Arrival",[validators.InputRequired("Please enter the minutes of arrival."), validators.NumberRange(min=0, max=59, message="Please enter the right minutes of arrival.")])
    
    City = SelectField('City of Departure', choices = L_airport)
    submit = SubmitField("Send")