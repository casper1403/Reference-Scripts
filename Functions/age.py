from dateutil.relativedelta import relativedelta
import datetime

""" Script that prints the date someone would have turned 18 as of today"""

years_ago = datetime.datetime.now() - relativedelta(years=18)
print(years_ago.date())
