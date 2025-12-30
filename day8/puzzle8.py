'''
The input is in 3D space: input is xyz coordinates

RULES:
Junction boxes are the lines in the input
Find junction boxes that are as close together as possible

2 close junction boxes form a curcuit, then if the next two closest
junction boxes contain a junction box that is already in the circuit, the 
junction box not already in the curcuit, joints the other curcuit. 


'''
from math import sqrt
from collections import Counter

boxes = []
LIMIT = 1000

with open("day8/junctionBox.txt", "r") as f:
    for line in f:
        coords = list(map(int, line.strip().split(',')))
        boxes.append(coords)

# Distance formule (euclidian distance)
def distance(box_a, box_b):
    return sqrt((box_a[0] - box_b[0])**2 + (box_a[1] - box_b[1])**2 + (box_a[2] - box_b[2])**2)

# list of distances
distances = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        box_a = boxes[i]
        box_b = boxes[j]

        dist = distance(box_a, box_b)

        distances.append((dist, i, j))

distances.sort()

group_ids = list(range(len(boxes)))
num_groups = len(boxes)
steps_taken = 0

for dist, idx_a, idx_b in distances:
    
    # STOP if we have made the required number of connection attempts
    '''
    if steps_taken >= LIMIT:
        break
    '''
    
    group_a = group_ids[idx_a]
    group_b = group_ids[idx_b]
    
    # If in different groups -> Connect them (Merge groups)
    if group_a != group_b:
        for k in range(len(group_ids)):
            if group_ids[k] == group_b:
                group_ids[k] = group_a

                # We just merged two groups, so the total count drops by 1
        num_groups -= 1
        
        if num_groups == 1:
            box_a = boxes[idx_a]
            box_b = boxes[idx_b]
            
            print(f"Last connection was between Box #{idx_a} and Box #{idx_b}")
            print(f"Coordinates: {box_a} and {box_b}")
            
            # The puzzle asks to multiply the X coordinates (index 0)
            result = box_a[0] * box_b[0]
            print(f"Answer (X1 * X2): {result}")
            
            break
    # If in same group -> "Nothing happens" (But it still counts as a step)
    else:
        pass

    steps_taken += 1

# Count size of each circuit
#circuit_counts = Counter(group_ids).values()
#sorted_sizes = sorted(circuit_counts, reverse=True)

#print(f"Processed {steps_taken} pairs.")
#print(f"Circuit sizes: {sorted_sizes}")

#result = sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]
#print("Final Answer:", result)