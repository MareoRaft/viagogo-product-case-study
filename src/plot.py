import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
plt.style.use('seaborn')
COLORS = {
	'green': '#64bf7b',
	'blue': '#5e88bd',
	'red': '#d06464',
	'purple': '#9388bf',
}


def metrics_graph(df, series1, series2):
	'''
	Generate graph showing BOTH metrics combined, control group only.
	'''
	metric_to_series = {
		'conversion': series1,
		'bounce': series2,
	}
	for metric in ('bounce', 'conversion'):
		series = metric_to_series[metric]
		x = series.index.values
		y = [Y[0] for Y in series]
		# plot results
		# plt.plot(x, y)
		# line, = plt.plot_date(x, y, linestyle='solid', color=metric_to_color[metric])
		line, = plt.plot_date(x, y, linestyle='solid',)
		# make date labels diagonal
		# plt.gcf().autofmt_xdate()
		# format date strings
		date_format = mpl_dates.DateFormatter('%d')
		axes = plt.gca()
		xaxis = axes.xaxis
		xaxis.set_major_formatter(date_format)
		# xaxis.set_major_locator(matplotlib.ticker.Locator())
		axes.set_xticks(x)
		# make label for legend
		line.set_label(f'{metric} rate')
	# label things
	plt.title(f'User metrics during October, 2014')
	plt.xlabel('Date (in October, 2014)')
	plt.ylabel(f'Metric Rate')
	# add the legend
	plt.legend()
	# finally, print the graph
	plt.show()


def metric_graph(df, metric, series):
	'''
	Generate graph for a SINGLE metric, showing BOTH control and variant groups.
	  * `series` -- data in form of Pandas Series
	'''
	ab_group_to_index = {
		'control': 0,
		'variant': 1,
	}
	x = series.index.values
	for ab_group in ('control', 'variant'):
		y = [Y[ab_group_to_index[ab_group]] for Y in series]
		# plot results
		line, = plt.plot_date(x, y, linestyle='solid')
		# format date strings
		date_format = mpl_dates.DateFormatter('%d')
		axes = plt.gca()
		xaxis = axes.xaxis
		xaxis.set_major_formatter(date_format)
		# make 1 tick per date
		axes.set_xticks(x)
		# make label for legend
		line.set_label(f'{ab_group} group')
	# label things
	plt.title(f'User {metric.capitalize()} Rate during October, 2014')
	plt.xlabel('Date (in October, 2014)')
	plt.ylabel(f'{metric.capitalize()} Rate')
	# add the legend
	plt.legend()
	# finally, print the graph
	plt.show()


def graph(df, metric, x, ys):
	'''
	Generate graph for a SINGLE metric, showing BOTH control and variant groups.
	  * `series` -- data in form of Pandas Series
	'''
	ab_group = 'control'
	_, axeses = plt.subplots(len(ys), sharey=True)
	# plot results
	for i,y in enumerate(ys):
		axes = axeses[i]
		line, = axes.plot_date(x, y, linestyle='solid', color=list(sorted(COLORS.values()))[i])
		axes.set_xticks(x)
		axes.xaxis.set_ticklabels([])
		# make label for legend
		line.set_label(['outlier', 'trend line', 'weekly periodic behavior', 'noise'][i])
		# add the legend
		axes.legend()
	# format date strings
	date_format = mpl_dates.DateFormatter('%d')
	axes = plt.gca()
	xaxis = axes.xaxis
	xaxis.set_major_formatter(date_format)
	# make 1 tick per date
	axes.set_xticks(x)
	# label things
	axeses[0].set(title=f'{metric.capitalize()} Rate time series analysis breakdown')
	plt.xlabel('Date (in October, 2014)')
	# finally, print the graph
	plt.show()

