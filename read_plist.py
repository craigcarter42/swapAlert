#!/usr/bin/env python

def error(code):
   print(" -- swapAlert: an error has occured")
   if code == 1: print(" -- swapAlert: exit code: 1")
   if code == 2: print(" -- swapAlert: exit code: 2")
   if code == 3: print(" -- swapAlert: exit code: 3")
   exit()

try:
   import os, plistlib
except ImportError:
   error(1)

# SW = "0" #: Swap ID
# DC = "0" #: Date Created
# TC = "0" #: Time Created
# DM = "0" #: Date Modified
# TM = "0" #: Time Modified

# - All errors are fatal:
# Error code: 1 - Module could not be loaded
# Error code: 2 - Damaged plist file
# Error code: 3 - Plist file not found


class swaptrack:
   def read_plist(self):
      plist_dict = {}
      SW = "0"
      DC = "0"
      TC = "0"
      DM = "0"
      TM = "0"
      print(" -- read_plist: called")
      fileName=os.path.expanduser('~/Projects/swapAlert/swaptrack.plist')
      if os.path.exists(fileName):
         pl=plistlib.readPlist(fileName)
         if 'Swap ID' in pl: SW = pl['Swap ID']
         else: error(2)
         if 'Date Created' in pl: DC = pl['Date Created']
         else: error(2)
         if 'Time Created' in pl: TC = pl['Time Created']
         else: error(2)
         if 'Date Modified' in pl: DM = pl['Date Modified']
         else: error(2)
         if 'Time Modified' in pl: TM = pl['Time Modified']
         else: error(2)
      else:
         error(3)
      plist_dict = {'Swap ID' : SW, 'Date Created' : DC, 'Time Created' : TC, 'Date Modified' : DM, 'Time Modified' : TM}
      print(plist_dict)

   def write_plist():
      pl = {
      "Swap ID" : "01",
      "Date Created" : "08/12/1987",
      "Time Created" : "08/12/1987",
      "Date Modified" : "08/12/1987",
      "Time Modified" : "08/12/1987",
      "Good" : "Bye",
      }
      fileName=os.path.expanduser('~/Projects/swapAlert/swaptrack.plist')
      plistlib.writePlist(pl, fileName)

   def function(self):
      print(" -- swaptrack: called")
   

def main():
   run_swaptrack = swaptrack()
   run_swaptrack.function()
   run_swaptrack.read_plist()

if __name__ == '__main__':
   main()
