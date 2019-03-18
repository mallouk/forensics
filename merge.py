import os
import argparse

full_list_sizes = []
full_list_hashes = []
full_merge_list = []

parser = argparse.ArgumentParser(description='Merge hash and size files from VM images.')
parser.add_argument('-hf', action='store', required=True, help='file containing names and hashes')
parser.add_argument('-sf', action='store', required=True, help='file containing names and sizes')
parser.add_argument('-of', action='store', required=True, help='output file')
args = parser.parse_args()


f = open(args.sf, 'r')
for line in f.readlines():
	size = line.replace("\n", "").split(" ")[0]
	filename = line.replace("\n", "").split(" ")[1]
	list = []
	list.append(filename)
	list.append(size)
	
	full_list_sizes.append(list)
f.close()

wf = open(args.of, "w+")

f = open(args.hf, 'r')
for line in f.readlines():
	hash = line.replace("\n", "").split(" ")[0]
	filename = line.replace("\n", "").split(" ")[2]
	list = []
	list.append(filename)
	list.append(hash)
	
	full_list_hashes.append(list)
f.close()
	
i = 1	
for hlist in full_list_hashes:
	filename = hlist[0]
	hash = hlist[1]
	for slist in full_list_sizes:	
		if filename in slist:
			print i, filename, hash, slist
			i = i + 1
			wf.write(filename + " " + slist[1] + " " + hash + "\n")
f.close()
wf.close()