import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
if n%2==0 and n>1 and n<6 or n>20 and n%2==0:
    print("Not Weird") 
elif n%2==0 and n>5 and n<21 or n%2==1:
    print("Weird")
