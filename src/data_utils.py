import datetime

import pandas as pd

def load_df():
	df = pd.read_csv('data/product-case-data.csv',
		encoding='utf_8',
		delimiter=',',
		# read col names from file itself
		header='infer',
		names=None,
		# Specify that the 'Date' column should have values converted into date objects
		parse_dates=['Date'],
		date_parser=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'),
	)
	return df

