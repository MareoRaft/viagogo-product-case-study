import pandas as pd
import numpy as np

import data_utils
import plot


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
	# compute stats
	control_rate = get_metric(df, metric, 'Visitors_Control')
	variant_rate = get_metric(df, metric, 'Visitors_Variant')
	relative_change = get_relative_change(control_rate, variant_rate)
	# output results
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


def plot_metric(df, metric):
	series = compute_stats_for_metric_by_date(df, metric)
	plot.metric_graph(df, metric, series)


def plot_metrics(df):
	series1 = compute_stats_for_metric_by_date(df, 'conversion')
	series2 = compute_stats_for_metric_by_date(df, 'bounce')
	plot.metrics_graph(df, series1, series2)


def main():
	df = data_utils.load_df()
	# Uncomment to generate the 'conversion rate' graph
	# plot_metric(df, 'conversion')
	# Uncomment to generate the 'bounce rate' graph
	# plot_metric(df, 'bounce')
	# Uncomment to generate the 'conversion/bounce comparison' graph
	# plot_metrics(df)
	# Uncomment to generate the stat summary data
	# compute_stats(df)


if __name__ == '__main__':
	df = data_utils.load_df()
	series = compute_stats_for_metric_by_date(df, 'conversion')
	x = series.index.values
	y = [Y[0] for Y in series]
	ys = pd.Series(y)
	u = ys.mean()
	s = ys.std()
	n = len(y)
	endpoint = u - 1.64*s/np.sqrt(n)
	cc = (u - 0.05305) * np.sqrt(n) / s
	print(cc)



