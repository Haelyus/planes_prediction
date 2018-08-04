import datetime
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib

def validate_date(p_year, p_month, p_day):
    #import datetime
    try:
        datetime.date(p_year, p_month, p_day)
        return True
    except:
        return False

def plane_prediction(p_carrier, p_month, p_day_w, p_dist, p_dep, p_arr, p_flight):
    #import pandas as pd
    #from sklearn.ensemble import RandomForestRegressor
    #from sklearn.externals import joblib
    #file_name = str(p_carrier) + '61.pkl'
    file_name = str(p_carrier) + '_RF.pkl'
    L_title = ['MONTH', 'DAY_OF_WEEK', 'DISTANCE', 'CRS_DEP_TIME_MIN', 'CRS_ARR_TIME_MIN', 'NB_FLIGHT_ORIGIN_AIRPORT']
    L_features = [p_month, p_day_w, p_dist, p_dep, p_arr, p_flight]
    df_return = pd.DataFrame(columns=L_title)
    df_return.loc[1] = L_features
    X = df_return[L_title]
    model = joblib.load('pkl/' + file_name)
    delay = model.predict(X)
    result = 'The delay arrival of this flight is : ' + str(int(delay)) + ' minute(s).'
    return result