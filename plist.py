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


# Used for current swapfiles in VM folder.
current_swaps = {}
add_swaps = {}

# Checks to see how many files are in VM.
for root, dirs, files in os.walk(vm_path):
	for f in files: file_list.append(f)

# Create list containg only swap files
for fl in file_list:
	if(f == "swapfile"): swapfiles.append(fl)
	if(f == 'swapfile' + str(count)): swapfiles.append(fl)
count += 1

# Gets file name, last modified, and size.
# Creates dictionary with list
for file in swapfiles:
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

	add_swaps = {swapid : (final_last_mod, swapsize)}
	current_swaps.update(add_swaps)
# Adds numbering to file names
	swap_count += 1

for key, value in current_swaps.iteritems():
	print(key, value)


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
class swf():
	def new_swf():
		print("swf00")



# for cd in current_swapfiles:
# 	print(":: " + str(cd))
# 	pl = {
# 	str(counter) + " Swap ID" : cd,
# 	"Date Modified" : lastmod
# 	}
# 	counter += 1
# 	plistlib.writePlist(pl, plist_path)


# if __name__ == '__main__':
#    main()
