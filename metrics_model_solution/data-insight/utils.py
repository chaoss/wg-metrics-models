from grimoirelab_toolkit.datetime import str_to_datetime
import datetime
import pandas as pd
from matplotlib import pyplot as plt
  
def get_time_diff_months(start, end):
    ''' Number of months between two dates in UTC format  '''

    if start is None or end is None:
        return None
    if type(start) is not datetime:
        start = str_to_datetime(start).replace(tzinfo=None)
    if type(end) is not datetime:
        end = str_to_datetime(end).replace(tzinfo=None)

    seconds_month = float(60 * 60 * 24 * 30)
    diff_months = (end - start).total_seconds() / seconds_month
    diff_months = float('%.2f' % diff_months)

    return diff_months
    
#Version message for community_A
def community_A_version_message(df):
    df['date'] = pd.to_datetime(df.grimoire_creation_date, format='%Y-%m-%d')
    x_dates = df['date'].dt.strftime('%Y-%m-%d').sort_values().unique()
    for i in ['2019-10-24', '2020-04-23', '2020-10-22', '2021-04-22','2021-10-28']:
        diff_mon = [abs(get_time_diff_months(i,j)) for j in x_dates]
        plt.axvline(x=diff_mon.index(min(diff_mon)), linewidth=4, color='#ff9933')
           
#Version message for openEuler
def openEuler_version_message(df):
    df['date'] = pd.to_datetime(df.grimoire_creation_date)
    x_dates = df['date'].dt.strftime('%Y-%m-%d').sort_values().unique()
    for i in ['2020-3-30', '2020-09-24', '2020-12-17','2021-03-25','2021-06-24', '2021-09-30','2021-12-30']:
        diff_mon = [abs(get_time_diff_months(i,j)) for j in x_dates]
        plt.axvline(x=diff_mon.index(min(diff_mon)), linewidth=4, color='green')