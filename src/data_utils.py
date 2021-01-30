import pandas as pd

def load_df():
	df = pd.read_csv('data/product-case-data.csv',
		encoding='utf_8',
		delimiter=',',
		# read col names from file itself
		header='infer',
		# since 'infer' is used above
		names=None,
	)
	return df

