#!/usr/bin/env python
try:
	import os, sys, subprocess, re
	from subprocess import call
except ImportError:
	return None


swf = ""
found_swf = ""
count = 0

args = str(sys.argv[1:2])

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
# END: notify
for root, dirs, files in os.walk("/var/VM"):  
    for filename in files:
        swf = swf + filename + " "
        if(args == "['-list']"): print("> " + filename)
        
found_swf = re.findall(r'swapfile.', swf)
for f in found_swf:
	count += 1
	if(args == "['-swap']"): print("> " + f)

if(args == "['-open']"): call(["open", "/var/VM"]); exit()
if(args == "['-flush']"): print(" swap -- flush all swapfiles"); exit()

if(updated == True):
  print("swapfile" + num + " has Updated")
if(count >= 1): notify("swapAlert", str(count) + " swapfiles created")

# swapfile: created
# swapfile: changed Bigger | Smaller
# swapfile: removed
# swapfile: filename
# swapfile: silent with no change
#/Volumes/Macintosh HD/Users/Solo/Desktop/VM

# swapAlert: Total Swaps: 1
# swapAlert: swapfile0 Created
# swapAlert: swapfile0 Updated
# swapAlert: swapfile0 Removed
# swapAlert: -- No alert
# swapAlert: -- Output to Log
