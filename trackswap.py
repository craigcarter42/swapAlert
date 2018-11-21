#!/usr/bin/env python
try:
   import os, plistlib
except ImportError:
   print("Error: Module not loaded")

# Setup global variables
SI = "" #: Swap ID
DC = "" #: Date Created
TC = "" #: Time Created
DM = "" #: Date Modified
TM = "" #: Time Modified

def read_plist():
   fileName=os.path.expanduser('~/Projects/swapAlert/swaptrack.plist')
   if os.path.exists(fileName):
      pl=plistlib.readPlist(fileName)
      if 'Swap ID' in pl: SW = pl['Swap ID']
      if 'Date Created' in pl: DC = pl['Date Created']
      if 'Time Created' in pl: TC = pl['Time Created']
      if 'Date Modified' in pl: DM = pl['Date Modified']
      if 'Time Modified' in pl: TM = pl['Time Modified']
      else:
         print 'There is no aString in the plist\n'
   else:
      print '%s does not exist, so can\'t be read' % fileName

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

def main():
   print("Welcome to plist read/write")

if __name__ == '__main__':
   main()