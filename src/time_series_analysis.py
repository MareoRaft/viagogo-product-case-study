'''
This file contains functions for performing a time series analysis.
'''
import math

import numpy as np

def get_trend(y, spread_radius):
	'''
	Given a list `y` of points, compute the corresponding trend points `y_trend`.  For example, given a point `y[i]`, the corresponding `y_trend[i]` is the average of points `y[i - spread_radius]` through `y[i + spread_radius]`.

	This is often referred to as a 'moving average' or a 'rolling average'.
	'''
	y_trend = []
	for i,_ in enumerate(y):
		left_endpoint_i = max(0, i - spread_radius)
		right_endpoint_i = min(len(y) - 1, i + spread_radius)
		points = y[left_endpoint_i:right_endpoint_i+1]
		avg = np.average(points)
		y_trend.append(avg)
	return np.array(y_trend)

def get_periodic_average(y, period):
	'''
	Find the average periodic behavior in a list `y`.  For example, given a point `y[i]`, then the corresponding output point `y_avg[i]` will be equal to the average of points `..., y[i - 2*period], y[i - period], y[i], y[i + period], y[i + 2*period]...`.  That is, all points of index `i` modulo `period`.
	'''
	assert period > 0
	# compute the averages
	y_period_avg = []
	for i in range(min(period, len(y))):
		yi_avg = np.average([y[i] for i in range(i, len(y), period)])
		y_period_avg.append(yi_avg)
	# repeat them as necessary to get an array of length y
	num_repeats = math.ceil(len(y) / period)
	repeated_y_period_avg = y_period_avg * num_repeats
	y_avg = repeated_y_period_avg[:len(y)]
	return np.array(y_avg)

def get_outlier(y, index):
	'''
	Given a list `y` of values and an `index` assumed to be an outlier, calculate the average of all the *other* points, and return a list showing only the outlier value relative to that average.
	'''
	assert len(y) > 1
	outlier_value = y[index]
	average_other_values = (np.sum(y) - outlier_value) / (len(y) - 1)
	outlier_value_diff = outlier_value - average_other_values
	y_out = [0] * len(y)
	y_out[index] = outlier_value_diff
	return np.array(y_out)

def get_analysis(y):
	'''
	Compute the full time series analysis for our specific situation.
	'''
	# 1. take outlier (day 18, index 8)
	outlier = get_outlier(y, 8)
	y = y - outlier
	# 2. take trend (averaging over 7 = 3+1+3 days)
	trend = get_trend(y, 3)
	y = y - trend
	# 3. take periodic (assume a 1-week period)
	periodic = get_periodic_average(y, 7)
	y = y - periodic
	# 4. observe noise
	noise = y
	# return
	return outlier, trend, periodic, noise

