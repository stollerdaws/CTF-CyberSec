# Python program for the above approach

# Taking the matrix as globally
tab = [[-1 for i in range(2000)] for j in range(2000)]


# Check if possible subset with
# given sum is possible or not
def subsetSum(a, n, sum):

	# If the sum is zero it means
	# we got our expected sum
	if (sum == 0):
		return 1

	if (n <= 0):
		return 0

	# If the value is not -1 it means it
	# already call the function
	# with the same value.
	# it will save our from the repetition.
	if (tab[n - 1][sum] != -1):
		return tab[n - 1][sum]

	# If the value of a[n-1] is
	# greater than the sum.
	# we call for the next value
	if (a[n - 1] > sum):
		tab[n - 1][sum] = subsetSum(a, n - 1, sum)
		return tab[n - 1][sum]
	else:

		# Here we do two calls because we
		# don't know which value is
		# full-fill our criteria
		# that's why we doing two calls
		tab[n - 1][sum] = subsetSum(a, n - 1, sum)
		return tab[n - 1][sum] or subsetSum(a, n - 1, sum - a[n - 1])


# Driver Code
if __name__ == '__main__':
	a = [600848253359, 617370603129, 506919465064, 218995773533, 831016169202, 501743312177, 15915022145, 902217876313, 16106924577, 339484425400, 372255158657, 612977795139, 755932592051, 188931588244, 266379866558, 661628157071, 428027838199, 929094803770, 917715204448, 103431741147, 549163664804, 398306592361, 442876575930, 641158284784, 492384131229, 524027495955, 232203211652, 213223394430, 322608432478, 721091079509, 518513918024, 397397503488, 62846154328, 725196249396, 443022485079, 547194537747, 348150826751, 522851553238, 421636467374, 12712949979]
	n = len(a)
	sum = 7929089016814
	if (subsetSum(a, n, sum)):
		print("YES")
	else:
		print("NO")

# This code is contributed by shivani.
