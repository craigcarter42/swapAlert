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
file_path = "/Volumes/Macintosh HD/Users/craigcarter/Projects/swapAlert/VM/"
if os.path.exists(file_path): pass
else:
	error(3)

# Path to plist file.
# Check if file exists
# Attempt to generate new plist if file not found.
fileName = "/Volumes/Macintosh HD/Users/craigcarter/Projects/swapAlert/swaptrack.plist"
if os.path.exists(fileName): fileName = os.path.expanduser('~/Projects/swapAlert/swaptrack.plist')
else:
	error(3)
# SETUP: END

# Program starts here.
print(" -- swapAlert: Started")

swf = []
final_swf = []
past_dict = {}
found_swf = ""
swaps = ""
count = 0
counter = 0
file_count = 0

# Used for current swapfiles that in VM
# when program runs.
current_dict = {}
current_dict["swapfiles"] = []
current_swapfiles = current_dict["swapfiles"]

# Program starts here.
# Checks to see how many files are in VM.
for root, dirs, files in os.walk(file_path):  
    for filename in files:
        swf.append(filename)

# print(" > swf: " + str(swf))
for x in swf:
	if x == "swapfile":
		final_swf.append(x)
	for x in swf:
		if x == "swapfile" + str(count):
			final_swf.append(x)
	count += 1

# print(" > final_swf: " + str(final_swf))

# Gets file name, last modified, and size.
# Creates dictionary with list
for file in final_swf:
	add_swapfile = {"x0" + str(file_count) + "swf" : file}
	current_swapfiles.append(add_swapfile)

# Creates file path for current swapfile
	final_file_path = file_path + file

# Gets the last modified date/time of file
	lastmodified = os.stat(final_file_path).st_mtime
	lastmod = datetime.fromtimestamp(lastmodified)

# Gets size of current swap file
	filesize = os.stat(final_file_path).st_size
	# print(" > size: " + str(filesize))
# Adds numbering to file names
	file_count += 1
print(current_dict)

# new_current_swapfiles = dict(current_swapfiles)
# print(dict.keys(new_current_swapfiles))


# NEXTUP:
# Consolidate all swapfile/s information into single dictionary.
# Read plist file.
# Compare current swapfile/s to plist.
# Notify user if needed.
# Update plist file.
# Exit.


counter = 0

for cd in current_swapfiles:
	print(":: " + str(cd))
	pl = {
	str(counter) + " Swap ID" : cd,
	"Date Modified" : lastmod
	}
	counter += 1

	plistlib.writePlist(pl, fileName)

	


# if __name__ == '__main__':
#    main()

#/Volumes/Macintosh HD/Users/craigcarter/Desktop/VM
#current_dict.update({"swap-file" : file})
# head, tail = os.path.split(file_path)
#print(" > tail: " + str(tail))
