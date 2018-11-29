#!/usr/bin/env python3

# SETUP: START
# - All errors are fatal:
# Error code: 1 - Module could not be loaded
# Error code: 2 - Damaged plist file
# Error code: 3 - Plist file not found
def error(code):
   print(" -- swapAlert: an error has occured")
   if code == 1: print(" -- swapAlert: exit code: 1")
   if code == 2: print(" -- swapAlert: exit code: 2")
   if code == 3: print(" -- swapAlert: exit code: 3")
   exit()

try:
   import os, re, plistlib
   from datetime import datetime
except ImportError:
   error(1)

# Path to VM folder
# Check if folder exists
vm_path = "/Volumes/Macintosh HD/Users/craigcarter/Projects/swapAlert/VM/"
if os.path.exists(vm_path): pass
else:
	error(3)

# Path to plist file.
# Check if file exists
# Attempt to generate new plist if file not found.
plist_path = "/Volumes/Macintosh HD/Users/craigcarter/Projects/swapAlert/swaptrack.plist"
if os.path.exists(plist_path): plist_path = os.path.expanduser('~/Projects/swapAlert/swaptrack.plist')
else:
	error(3)
# SETUP: END

# Program starts here.
print(" -- swapAlert: Started")

# Declare variables:
swapfiles = []
file_list = []
past_dict = {}
swapid = ""
count = 0
counter = 0
swap_count = 0

file_string = ""

# Used for current swapfiles in VM folder.
current_swaps = {}
add_swaps = {}

# Checks to see how many files are in VM.
for root, dirs, files in os.walk(vm_path):
	for f in files: file_string = file_string + f


counting_number = 0
the_swf = []
final_the_swf = []
found_swf = []
final_found_swapfiles = []
new_found_swf = []
update_swf = ""
i = 0
xi = 1

found_swapfiles = re.findall(r'swapfile', file_string)
len_check = len(found_swapfiles)
if(len_check > 0):
	for fs in found_swapfiles: final_found_swapfiles.append(fs)

	for ffs in final_found_swapfiles[1:]:
		final_found_swapfiles[xi] = ffs + str(i);
		xi = xi + 1
		i = i + 1

print(final_found_swapfiles)

# for fsw in found_swf:
# 	new_list.append(fsw)

# new_new_list.append(new_list[0])
# for nnl in new_new_list[:1]:
# 	final_new_list.append(nnl + xi)
# 	xi = xi + 1


# counting_number = 0
# the_swf = []
# final_the_swf = []
# update_swf = ""
# i = 0
# found_swf = re.findall(r'swapfile', file_string)

# for fsw in found_swf:
# 	new_list.append(fsw)

# new_new_list.append(new_list[0])
# for nnl in new_new_list[:1]:
# 	final_new_list.append(nnl + xi)
# 	xi = xi + 1




# final_the_swf.append('swapfile')
# for fs in found_swf:
# 	the_swf.append(f)

# print(the_swf)
# for ts in the_swf[1:]:
# 	final_the_swf.append(ts + str(i))
# 	i = i + 1

# print(final_the_swf)
# for th in the_swf[1:]:
# 	print(th)



	# if(counting_number == 0): swapfiles.append(f)
	# if(counting_number == 1):
	# 	update_swf = f + "0"
	# 	swapfiles.append(update_swf)
	# if(counting_number > 2):
	# 	update_swf = f + "0"
	# 	swapfiles.append(update_swf)
	# counting_number = counting_number + 1


# Gets file name, last modified, and size.
# Creates dictionary with list
for file in final_found_swapfiles:
# Creates file path for current swapfile
	final_vm_path = vm_path + file

# Gets the last modified date/time of file
	lastmodified = os.stat(final_vm_path).st_mtime
	lastmod = datetime.fromtimestamp(lastmodified)
	final_last_mod = str(lastmod)

# Gets size of current swap file
	swapsize = os.stat(final_vm_path).st_size
	# print(" > size: " + str(swapsize))

# Make Swap ID for each file
	swapid = "swf0" + str(swap_count)

	add_swaps = {swapid : {"filename" : file, "lastmod" : final_last_mod, "swapsize" : swapsize}}
	current_swaps.update(add_swaps)
# Adds numbering to file names
	swap_count += 1

def printout(value):
	if(value == 1):
		for key, value in current_swaps.iteritems():
			print(key, value)
	if(value == 2):
		for key, value in current_swaps.iteritems():
			print(current_swaps.get(key))

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def compare():
	print(" > compare")

# Write to plist file
def write_plist():
	print(" > write_plist")
	for key, value in current_swaps.iteritems():
		pl = {
			key : value
		}
	plistlib.writePlist(pl, plist_path)

def read_plist():
	print(" > read_plist")
	read_pl=plistlib.readPlist(plist_path)
	print(read_pl)

def main():
	print(" > main")
	read_plist()
	printout(1)
# NEXTUP:
# Consolidate all swapfile/s information into single dictionary.
# Read plist file.
# Compare current swapfile/s to plist.
# Notify user if needed.
# Update plist file.

# New Features:
# Add args for degugging.
# Add logging.
# Add CLI.

if __name__ == '__main__':
   main()


