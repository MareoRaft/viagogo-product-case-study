import numpy as np
import pandas as pd

from time_series_analysis import *

def test_get_trend():
	# array length 0, 1, 2
	assert get_trend([], 0) == []
	assert get_trend([2], 0) == [2]
	assert get_trend([2, 3], 0) == [2, 3]
	# spread radius 0, 1, 2
	assert get_trend([2, 4, 3], 0) == [2, 4, 3]
	assert get_trend([2, 4, 3], 1) == [3, 3, 3.5]
	assert get_trend([2, 4, 3], 2) == [3, 3, 3]
	# test a np array
	assert get_trend(np.array([2, 3]), 0) == [2, 3]
	# test a pandas series
	assert get_trend(pd.Series([2, 3]), 0) == [2, 3]

def test_get_periodic_average():
	# array length 0, 1, 2
	assert get_periodic_average([], 1) == []
	assert get_periodic_average([2], 1) == [2]
	assert get_periodic_average([2, 3], 1) == [2.5, 2.5]
	# period 1, 2, 3
	assert get_periodic_average([2, 4, 3, 0], 1) == [9/4] * 4
	assert get_periodic_average([2, 4, 3, 0], 2) == [5/2, 2] * 2
	assert get_periodic_average([2, 4, 3, 0], 3) == [1, 4, 3, 1]
	# test a np array
	assert get_periodic_average(np.array([2, 4, 3, 0]), 1) == [9/4] * 4
	# test a pandas series
	assert get_periodic_average(pd.Series([2, 4, 3, 0]), 1) == [9/4] * 4

def test_get_outlier():
	# no outlier
	assert get_outlier([4, 4], 0) == [0, 0]
	# outlier
	assert get_outlier([4, 5], 1) == [0, 1]
	# common use case
	assert get_outlier([4, 5, 4, 5, 4, 20, 5, 4, 5], 5) == [0, 0, 0, 0, 0, 15.5, 0, 0, 0]







