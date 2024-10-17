#!/usr/bin/env python3

import sys

names = open("names.txt").readlines()

#LBYL - look before you leap

if len(names) >= 3:
    print(names[2])

else:
 print("[error] this field is empty")
 sys.exit(1)
