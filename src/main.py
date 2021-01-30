import matplotlib.pyplot as plt

import data_utils


def get_conversion_rate(df, ab_group):
	'''
	Looking at people from a specific AB Group, compute the conversion rate, that is, the number of visitors to the home page who make a purchase, divided by the total number of visitors to the home page.
	'''
	num_visitors = df[ab_group].sum()
	num_purchase_visitors = df[df['Purchase'] == 1][ab_group].sum()
	conversion_rate = num_purchase_visitors / num_visitors
	return conversion_rate


def get_bounce_rate(df, ab_group):
	'''
	Looking at people from a specific AB Group, compute the bounce rate, that is, the number of visitors to the home page who leave after viewing only one page, divided by the total number of visitors that LAND on the home page (meaning that the first page they visit is the home page).
	'''
	num_land_visitors = df[df['Land'] == 1][ab_group].sum()
	num_bounce_visitors = df[df['Bounce'] == 1][ab_group].sum()
	bounce_rate = num_bounce_visitors / num_land_visitors
	return bounce_rate


def get_metric(df, metric, ab_group):
	'''
	Given a dataframe, get both metrics (conversion rate and bounce rate).
	'''
	if metric == 'conversion':
		return get_conversion_rate(df, ab_group)
	elif metric == 'bounce':
		return get_bounce_rate(df, ab_group)
	else:
		raise ValueError(f'unexpected metric "{metric}"')


def get_relative_change(reference_value, other_value):
	'''
	Given an original control value `reference_value` and an other value `other_value`, compute the relative change, as defined by https://en.wikipedia.org/wiki/Relative_change_and_difference#Definitions.
	'''
	relative_change = (other_value - reference_value) / reference_value
	return relative_change


def compute_stats_for_metric(df, metric):
	# compute things
	control_rate = get_metric(df, metric, 'Visitors_Control')
	variant_rate = get_metric(df, metric, 'Visitors_Variant')
	relative_change = get_relative_change(control_rate, variant_rate)
	# output results
	print()
	print(f'Control group {metric} rate:', control_rate)
	print(f'Variant group {metric} rate:', variant_rate)
	print('Relative change:', relative_change)


def compute_stats(df):
	for metric in ('conversion', 'bounce'):
		compute_stats_for_metric(df, metric)


def compute_stats_for_metric_by_date(df, metric):
	series_daily = df.groupby('Date').apply(
		lambda d: tuple(get_metric(d, metric, ab_group) for ab_group in ('Visitors_Control', 'Visitors_Variant'))
	)
	return series_daily


def compute_stats_by_date(df):
	# for metric in ('conversion', 'bounce'):
	for metric in ('bounce',):
		series = compute_stats_for_metric_by_date(df, metric)
		x = series.index.values
		y = [Y[0] for Y in series]
		# plot results
		plt.plot(x, y)
		plt.show()


def main():
	df = data_utils.load_df()
	# print(df, df.dtypes)
	# compute_stats(df)
	compute_stats_by_date(df)


if __name__ == '__main__':
	main()