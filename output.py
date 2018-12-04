#!/usr/bin/env python3

current_mode = "v"
verbose_title = " -- swapAlert: "
silent_title = " * "
logging_title = " -- swapAlert: logging: "
default_title = " default: "
critical_title = " -- swapAlert: CRITICAL: "

class error:
    def __init__(output_object, mode, msg_type, msg):
        output_object.msg_type = msg_type
        output_object.msg = msg
        output_object.mode = mode

    def func(abc):
        if(abc.mode == "v"):
            print(verbose_title + abc.msg_type + " " + abc.msg)
        elif(abc.mode == "s"):
            print(silent_title + abc.msg_type + " " + abc.msg)
        elif(abc.mode == "l"):
            print(logging_title + abc.msg_type + " " + abc.msg)
        elif(abc.mode == "c"):
            print(critical_title + abc.msg_type + " " + abc.msg)
        else:
            print(default_title + abc.msg_type + " " + abc.msg)

    def catch(code):
        print(" -- swapAlert: an error has occured")
        if code == 1: print(" -- swapAlert: exit code: 1")
        if code == 2: print(" -- swapAlert: exit code: 2")
        if code == 3: print(" -- swapAlert: exit code: 3")
        exit()


class message_mode():
    def print_current_mode(self):
        print(" -- current mode: " + str(current_mode))

    def set_mode(self, mode):
        global current_mode
        current_mode = mode




error_msg_syntax = ("mode, type, num, msg")





try:
   import os, sys, re, plistlib
   from datetime import datetime
except ImportError:
   error(1)

m1 = message_mode()
m1.set_mode("l")
m1.print_current_mode()

f1 = error(current_mode,"module_not_found", "dud.py")
f1.func()





# if __name__ == '__main__':
#     print(" -- swapAlert: Started")
#     main()


# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()