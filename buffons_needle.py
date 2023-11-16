# Author: Bevlin Reddy
# Version: 0.21
#
# Name: Buffons_needle.py
# GitHub: https://github.com/Databreddy/buffons_needle

import random
import math

# Variables declaration
needle_length = 20
strip_width = needle_length*1.15
max_trials = 1_000_001
boarder0 = strip_width*0    # board dimensions
boarder1 = strip_width*1    # board dimensions
boarder2 = strip_width*2    # board dimensions
boarder3 = strip_width*3    # board dimensions
boarder4 = strip_width*4    # board dimensions
boarder5 = strip_width*5    # board dimensions
boarder6 = strip_width*6    # board dimensions
count_needles = 0
list_needless = []


def length(x1, y1, x2, y2):
    length = math.trunc(math.sqrt((x2-x1)**2+(y2-y1)**2))
    return length

def generate_needles(boarder6):
    
    x1 = random.randint(0, boarder6)
    y1 = random.randint(0, boarder6)
    x2 = random.randint(0, boarder6)
    y2 = random.randint(0, boarder6)
    
    distance = length(x1, y1, x2, y2)

    if distance == needle_length:
        count_needles += 1
        return count_needles

for i in range(1, 1000):    
    print(generate_needles(boarder6))

