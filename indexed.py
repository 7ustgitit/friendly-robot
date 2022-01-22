import math
from math import nan as NaN
from math import *

def down(nums: int) -> int:
    if nums != NaN:
        while True:
            nums += 1
            if nums == 51:
                break
    for i in range (nums):
        print(i)
    return i # this just show it's always at the end of a thread

def gest():
    counted = down(1)
    print(counted) # ^^ and here
    
gest()