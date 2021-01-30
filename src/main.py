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


def get_relative_change(reference_value, other_value):
	'''
	Given an original control value `reference_value` and an other value `other_value`, compute the relative change.
	'''
	relative_change = (other_value - reference_value) / reference_value
	return relative_change


def main():
	df = data_utils.load_df()

	# compute things
	control_conversion_rate = get_conversion_rate(df, 'Visitors_Control')
	variant_conversion_rate = get_conversion_rate(df, 'Visitors_Variant')
	relative_change_conversion_rate = get_relative_change(control_conversion_rate, variant_conversion_rate)
	#
	control_bounce_rate = get_bounce_rate(df, 'Visitors_Control')
	variant_bounce_rate = get_bounce_rate(df, 'Visitors_Variant')
	relative_change_bounce_rate = get_relative_change(control_bounce_rate, variant_bounce_rate)

	# output results
	print()
	print('Control group conversion rate:', control_conversion_rate)
	print('Variant group conversion rate:', variant_conversion_rate)
	print('Relative change:', relative_change_conversion_rate)
	print()
	print('Control group bounce rate:', control_bounce_rate)
	print('Variant group bounce rate:', variant_bounce_rate)
	print('Relative change:', relative_change_bounce_rate)


if __name__ == '__main__':
	main()
