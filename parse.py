import os
import argparse
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

def ingest_data(merge_file, val):
	merge_data = set()
	file = open(merge_file, 'r')
	for line in file.readlines():
		name = line.replace("\n", "").split(" ")[0]
		size = line.replace("\n", "").split(" ")[1]
		hash = line.replace("\n", "").split(" ")[2]
		
		if val == 1:
			list = name + "-" + size + "-" + hash
			merge_data.add(list)
		elif val == 0:
			merge_data.add(name)
		else:
			merge_data.add(int(size) )
	file.close()
	return merge_data

def print_diff(diff_set):
	I = 1
	#for ds in diff_set:
		#print "\t",ds

parser = argparse.ArgumentParser(description='Merge hash and size files from VM images.')
parser.add_argument('-i1', action='store', required=True, help='file containing merge data 1')
parser.add_argument('-i2', action='store', required=True, help='file containing merge data 2')
parser.add_argument('-i3', action='store', required=True, help='file containing merge data 2')
parser.add_argument('-i4', action='store', required=True, help='file containing merge data 2')

parser.add_argument('-o', action='store', required=True, help='output file')
args = parser.parse_args()

merge_file_len1 = 86434
merge_file_len2 = 86671
merge_file_len3 = 91494
merge_file_len4 = 91869

merge_data1 = ingest_data(args.i1, 0)
merge_data2 = ingest_data(args.i2, 0)
merge_data3 = ingest_data(args.i3, 0)
merge_data4 = ingest_data(args.i4, 0)

diff12_0 = merge_data1.difference(merge_data2)
diff21_0 = merge_data2.difference(merge_data1)
diff13_0 = merge_data1.difference(merge_data3)
diff31_0 = merge_data3.difference(merge_data2)
diff14_0 = merge_data1.difference(merge_data4)
diff41_0 = merge_data4.difference(merge_data2)
diff23_0 = merge_data2.difference(merge_data3)
diff32_0 = merge_data3.difference(merge_data2)
diff24_0 = merge_data2.difference(merge_data4)
diff42_0 = merge_data4.difference(merge_data2)
diff34_0 = merge_data3.difference(merge_data4)
diff43_0 = merge_data4.difference(merge_data3)

merge_data1 = ingest_data(args.i1, 1)
merge_data2 = ingest_data(args.i2, 1)
merge_data3 = ingest_data(args.i3, 1)
merge_data4 = ingest_data(args.i4, 1)

diff12_1 = merge_data1.difference(merge_data2)
diff21_1 = merge_data2.difference(merge_data1)
diff13_1 = merge_data1.difference(merge_data3)
diff31_1 = merge_data3.difference(merge_data2)
diff14_1 = merge_data1.difference(merge_data4)
diff41_1 = merge_data4.difference(merge_data2)
diff23_1 = merge_data2.difference(merge_data3)
diff32_1 = merge_data3.difference(merge_data2)
diff24_1 = merge_data2.difference(merge_data4)
diff42_1 = merge_data4.difference(merge_data2)
diff34_1 = merge_data3.difference(merge_data4)
diff43_1 = merge_data4.difference(merge_data3)


test = ingest_data(args.i1, 2)

# Generate a normal distribution, center at x=0 and y=5
x = list(test)
y = 100000
n_bins = 20


fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
axs[0].hist(x, bins=n_bins)

plt.show()

exit()

#NF - New Files
#CF - Changed Files
print "Diff 1-2:", " NF -", len(diff12_0), "\tCF -", len(diff12_1)
print_diff(diff12_1)

print "Diff 2-1:", " NF -", len(diff21_0), "\tCF -", len(diff21_1)
print_diff(diff21_1)

print "Diff 1-3:", " NF -", len(diff13_0), "\tCF -", len(diff13_1)
print_diff(diff13_1)

print "Diff 3-1:", " NF -", len(diff31_0), "\tCF -", len(diff31_1)
print_diff(diff31_1)

print "Diff 1-4:", " NF -", len(diff14_0), "\tCF -", len(diff14_1)
print_diff(diff14_1)

print "Diff 4-1:", " NF -", len(diff41_0), "\tCF -", len(diff41_1)
print_diff(diff41_1)

print "Diff 2-3:", " NF -", len(diff23_0), "\tCF -", len(diff23_1)
print_diff(diff23_1)
print diff23_0

print "Diff 3-2:", " NF -", len(diff32_0), "\tCF -", len(diff32_1)
print_diff(diff32_1)

print "Diff 2-4:", " NF -", len(diff24_0), "\tCF -", len(diff24_1)
print_diff(diff24_1)
print diff24_0

print "Diff 4-2:", " NF -", len(diff42_0), "\tCF -", len(diff42_1)
print_diff(diff42_1)

print "Diff 3-4:", " NF -", len(diff34_0), "\tCF -", len(diff34_1)
print_diff(diff34_1)

print "Diff 4-3:", " NF -", len(diff43_0), "\tCF -", len(diff43_1)
print_diff(diff43_1)





