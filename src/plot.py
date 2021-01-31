import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
plt.style.use('seaborn')
# seaborn colors
# green: #55a868


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

