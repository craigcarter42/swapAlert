#!/usr/bin/env python3

# SETUP: START
# - All errors are fatal:
# Error code: 1 - Module could not be loaded
# Error code: 2 - Damaged plist file
# Error code: 3 - Plist file not found
''' swapAlert: Version 1.3 box256: Track swapfiles created by the OS
 when wired memory has nearly reached max capacity'''

def error(code):
   print(" -- swapAlert: an error has occured")
   if code == 1: print(" -- swapAlert: exit code: 1")
   if code == 2: print(" -- swapAlert: exit code: 2")
   if code == 3: print(" -- swapAlert: exit code: 3")
   exit()

try:
   import os, sys, re, time, plistlib
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
template_plist = "String Holder"
plist_path = "/Volumes/Macintosh HD/Users/craigcarter/Projects/swapAlert/swaptrack.plist"
if os.path.exists(plist_path): plist_path = os.path.expanduser('~/Projects/swapAlert/swaptrack.plist')
else:
    plistlib.writePlist(template_plist, plist_path)
    error(3)
# SETUP: END

# Declare variables:
i = 0
xi = 1
swap_count = 0
read_pl = {}
final_found_swapfiles = []
file_string = ""
swapid = ""
print_mode = "v"
logging_mode = "v"

# Used for current swapfiles in VM folder.
current_swaps = {}
add_swaps = {}

# Checks to see how many files are in VM.
for root, dirs, files in os.walk(vm_path):
    for f in files: file_string = file_string + f

found_swapfiles = re.findall(r'swapfile', file_string)
len_check = len(found_swapfiles)
if(len_check > 0):
    for fs in found_swapfiles:
        final_found_swapfiles.append(fs)

    for ffs in final_found_swapfiles[1:]:
        final_found_swapfiles[xi] = ffs + str(i);
        xi = xi + 1
        i = i + 1

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
    print(" -- swapAlert: printout")
    if(value == 1):
        for key, value in current_swaps.iteritems():
            print(key, value)
    if(value == 2):
        for key, value in current_swaps.iteritems():
            print(current_swaps.get(key))

def notify(title, text):
    print(" -- swapAlert: notify")
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    time.sleep(2)

def compare(dict10,dict11):
    print(" -- swapAlert: compare")
    key_count = 0
    dict10_len = len(dict10)
    dict11_len = len(dict11)
    while True:
        if(dict10_len > 0):
            dict10_len = dict10_len - 1
            dict11_len = dict11_len - 1

            key_name = "swf0" + str(key_count)

            dict10_filename = dict10.get(key_name)["filename"]
            dict11_filename = dict11.get(key_name)["filename"]

            # LASTMOD
            print(" -- lastmod:")
            print(str(key_name) + " : " + dict10_filename + ": " + str(dict10.get(key_name)["lastmod"]))
            print(str(key_name) + " : " + dict10_filename + ": " + str(dict11.get(key_name)["lastmod"]))

            dict10_lastmod = dict10.get(key_name)["lastmod"]
            dict11_lastmod = dict11.get(key_name)["lastmod"]
            if(dict10_lastmod == dict11_lastmod):
                print(str(key_name) + " -- lastmod: No Changes")
            elif(dict10_lastmod > dict11_lastmod):
                notify("swapAlert2", str(key_name) + " : " + str(dict10_filename) + " was modified")
                print(str(key_name) + " : " + str(dict10_filename) + " was modified")
            else:
                notify("swapAlert2", str(key_name) + " : " + str(dict11_filename) + " was modified")
                print(str(key_name) + " : " + str(dict11_filename) + " was modified")


            # SWAPSIZE
            print(" -- swapsize:")
            print(str(key_name) + " : " + dict10_filename + ": " + str(dict10.get(key_name)["swapsize"]))
            print(str(key_name) + " : " + dict11_filename + ": " + str(dict11.get(key_name)["swapsize"]))

            dict10_swapsize = dict10.get(key_name)["swapsize"]
            dict11_swapsize = dict11.get(key_name)["swapsize"]
            if(dict10_swapsize == dict11_swapsize):
                print(str(key_name) + " -- swapsize: No Changes")
            elif(dict10_swapsize > dict11_swapsize):
                notify("swapAlert2", str(key_name) + " : " + str(dict10_filename) + " swapfile size has increased")
                print(str(key_name) + " : " + str(dict10_filename) + " swapfile size has increased")
            else:
                notify("swapAlert2", str(key_name) + " : " + str(dict11_filename) + " swapfile size has decreased")
                print(str(key_name) + " : " + str(dict11_filename) + " swapfile size has decreased")

            print("")
            key_count = key_count + 1
        else:
            print("END:")
            break

# Write to plist file at end to save results for next cycle

# Write to plist file
def write_plist():
    global current_swaps
    print(" -- swapAlert: write_plist")
    plistlib.writePlist(current_swaps, plist_path)

def read_plist(mode):
# Silent Mode: reads plist but give no output
# Verbose Mode: reads plist and gives output
# Default Mode: Unknown args provide, defaults to verbose
    global read_pl
    read_pl = plistlib.readPlist(plist_path)
    if(mode == "v"): print(" -- swapAlert: read_plist / verbose\n"); print(read_pl)
    elif(mode == "s"): print(" -- swapAlert: read_plist / silent")
    else: print(" -- swapAlert: read_plist / default")

def args():
    global print_mode
    global logging_mode
# Print Mode: (s) Silent (v) Verbose (*) Default
# Logging Mode: (s) Silent (v) Verbose (c) Critical (*) Default
    print(" -- swapAlert: args")
    

def main():
    print(" -- swapAlert: main")
    print(logging_mode)
    print(print_mode)
    args = sys.argv[1:]
    if(len(args) > 0):
        for a in args:
            final_args = a

        if(final_args == "w"): write_plist()
        elif(final_args == "r"): read_plist()
        elif(final_args == "p"): printout(1)

    read_plist("s")
    compare(current_swaps, read_pl)
    # write_plist()
    # printout(1)


# NEXTUP:
# Consolidate all swapfile/s information into single dictionary.
# Compare current swapfile/s to plist.
# Read plist file.
# Notify user if needed.
# Update plist file.

# New Features:
# Add args for degugging.
# Add logging.
# Add CLI.

if __name__ == '__main__':
    print(" -- swapAlert: Started")
    main()



