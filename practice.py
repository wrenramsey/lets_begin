#!/usr/bin/python 

import sys

def inpt():
    
    if sys.argv[0] == 0:
        print "Type something silly.."
        return 
    else:
        print sys.argv[1]
        return 

inpt()
