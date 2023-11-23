# Author: Bevlin Reddy
# Version: 0.21
#
# Name: Buffons_needle.py
# GitHub: https://github.com/Databreddy/buffons_needle

import random
import math

# Variables declaration
needle_length = 36
strip_width = 50
max_trials = 100_001
Y1 = strip_width*0      # board dimensions
Y2 = strip_width*1      # board dimensions
Y3 = strip_width*2      # board dimensions
Y4 = strip_width*3      # board dimensions
Y5 = strip_width*4      # board dimensions
Y6 = strip_width*5      # board dimensions
Y7 = strip_width*6      # board dimensions
Y8 = strip_width*7      # board dimensions
cross_list = []
safe_list = []

def find_length(x1, y1, x2, y2):
    length = math.trunc(math.sqrt((x2-x1)**2+(y2-y1)**2))
    return length

def generate_needles(boarder6, max_trials):
   
    count_needles = 0
    count_cross = 0
    count_safe = 0
    
    for _ in range(1, max_trials): 
        x1 = random.randint(0, Y6)
        y1 = random.randint(0, Y7)
        x2 = random.randint(0, Y6)
        y2 = random.randint(0, Y7)
    
        distance = find_length(x1, y1, x2, y2)

        if int(distance) == int(needle_length):
            count_needles += 1
        
            # print(x1, y1, x2, y2, distance)
        
            if (y1 <= Y1 <= y2 or y2 <= Y1 <= y1) or \
                (y1 <= Y2 <= y2) or (y2 <= Y2 <= y1) or \
                (y1 <= Y3 <= y2) or (y2 <= Y3 <= y1) or \
                (y1 <= Y4 <= y2) or (y2 <= Y4 <= y1) or \
                (y1 <= Y5 <= y2) or (y2 <= Y5 <= y1) or \
                (y1 <= Y6 <= y2) or (y2 <= Y6 <= y1) or \
                (y1 <= Y7 <= y2) or (y2 <= Y7 <= y1):
                count_cross += 1
            else:
                count_safe += 1
            
    return count_needles, count_cross, count_safe

# Main program
for _ in range(1, 11):
    count_needles, count_cross, count_safe = generate_needles(Y6, max_trials)
    cross_list.append(count_cross)
    safe_list.append(count_safe)

print(count_cross, count_needles, count_safe)
print("Pi = ", (2*needle_length)/(strip_width*(count_cross/count_needles)))
print("p = ", count_cross/(count_cross+count_safe))
print("average Pi = ", sum(cross_list)/((len(cross_list))))