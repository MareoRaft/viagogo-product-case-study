import pandas as pd
import numpy as np

import data_utils
import time_series_analysis
import plot


def get_conversion_rate(df, ab_group):
	'''
	Looking at people from a specific AB Group, compute the conversion rate, that is, the number of visitors to the home page who make a purchase, divided by the total number of visitors to the home page.
	'''
	# Change the following line if you want to restrict the data to a certain subset
	df_ = df
	# df_ = df[df['User Type'] == 'New User']
	num_visitors = df_[ab_group].sum()
	num_purchase_visitors = df_[df_['Purchase'] == 1][ab_group].sum()
	conversion_rate = num_purchase_visitors / num_visitors
	return num_visitors, num_purchase_visitors, conversion_rate


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
	a_total, a_positive, a_rate = get_metric(df, metric, 'Visitors_Control')
	b_total, b_positive, b_rate = get_metric(df, metric, 'Visitors_Variant')
	total = a_total + b_total
	positive = a_positive + b_positive
	rate = positive / total
	# relative_change = get_relative_change(a_rate, b_rate)
	# two-proportion z-test stats
	p1 = a_rate
	p2 = b_rate
	p = rate
	n1 = a_total
	n2 = b_total
	z = (p1 - p2) / np.sqrt(p * (1-p) * (1/n1 + 1/n2))
	# output results
	print(f'  Control group {metric} rate, num positive, total:', a_rate, a_positive, a_total)
	print(f'  Variant group {metric} rate, num positive, total:', b_rate, b_positive, b_total)
	print(f'Combined groups {metric} rate, num positive, total:', rate, positive, total)
	# print('Relative change:', relative_change)
	print(f'2-proportion z-stat for {metric}:', z)





def compute_stats(df):
	# for metric in ('conversion', 'bounce'):
	for metric in ('conversion',):
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


def plot_time_series_analysis(df, metric):
	series = compute_stats_for_metric_by_date(df, metric)
	print(series)
	x = series.index.values
	y = np.array([Y[0][2] for Y in series])
	print(np.shape(y))
	outlier, trend, periodic, noise = time_series_analysis.get_analysis(y)
	plot.graph(df, metric, x, [outlier, trend, periodic, noise])


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
	# Uncomment to plot time series analysis trend graph
	# plot_time_series_analysis(df, 'conversion')


if __name__ == '__main__':
	main()

