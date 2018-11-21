#!/usr/bin/python

import os
import plistlib

SI = "0" #: Swap ID
DC = "0" #: Date Created
TC = "0" #: Time Created
DM = "0" #: Date Modified
TM = "0" #: Time Modified
plist_dict = {}

class swaptrack:
   var1 = "1"
   var2 = "2"

   def function(self):
        print("swaptrack: called")

run_swaptrack = swaptrack()
print(run_swaptrack.var1)

def main():

   fileName=os.path.expanduser('~/Projects/swapAlert/swaptrack.plist')
   
   if os.path.exists(fileName):
      pl=plistlib.readPlist(fileName)
      if 'Swap ID' in pl: SW = pl['Swap ID']
      else: print("Error: Swap ID not found"); exit()
      if 'Date Created' in pl: DC = pl['Date Created']
      else: print("Error: Date Created not found"); exit()
      if 'Time Created' in pl: TC = pl['Time Created']
      else: print("Error: Time Created not found"); exit()
      if 'Date Modified' in pl: DM = pl['Date Modified']
      else: print("Error: Date Modified not found"); exit()
      if 'Time Modified' in pl: TM = pl['Time Modified']
      else: print("Error: Time Modified not found"); exit()

      plist_dict = {'Swap ID' : SW, 'Date Created' : DC, 'Time Created' : TC, 'Date Modified' : DM, 'Time Modified' : TM}
   else:
      print('%s does not exist, so can\'t be read' % fileName)

   print(plist_dict)

if __name__ == '__main__':
   main()


   #!/usr/bin/python

# import os
# import plistlib

# def main():

#    fileName=os.path.expanduser('~/Projects/swapAlert/swaptrack.plist')
   
#    if os.path.exists(fileName):
#       pl=plistlib.readPlist(fileName)
#       print '\nThe plist full contents is %s\n' % pl

#       if 'Swap ID' in pl:
#          print 'The aString value is %s\n' % pl['Swap ID']
#       else:
#          print 'There is no aString in the plist\n'

#    else:
#       print '%s does not exist, so can\'t be read' % fileName

# if __name__ == '__main__':
#    main()