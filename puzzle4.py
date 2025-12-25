'''
The forklift can only access if there's fewer than 4 rolls in the adjecent position

We have to look at all toilet papers around the one in question

somehow represent the grid as a 2D array, with lines on the X axis and columns on the Y.

keep track of indexing and for each index position (x, y) check the position around 
in x +- 1 and y +-1, and if the total of "@" equals 4 or more in length, we have a problem

'''

'''
['.', '.', '@', '@', '.', '@', '@', '@', '@', '.']
['@', '@', '@', '.', '@', '.', '@', '.', '@', '@']
['@', '@', '@', '@', '@', '.', '@', '.', '@', '@']
['@', '.', '@', '@', '@', '@', '.', '.', '@', '.']
['@', '@', '.', '@', '@', '@', '@', '.', '@', '@']
['.', '@', '@', '@', '@', '@', '@', '@', '.', '@']
['.', '@', '.', '@', '.', '@', '.', '@', '@', '@']
['@', '.', '@', '@', '@', '.', '@', '@', '@', '@']
['.', '@', '@', '@', '@', '@', '@', '@', '@', '.']
['@', '.', '@', '.', '@', '@', '@', '.', '@', '.']
'''
# Represent as rows and columns in a 2D array, DONE!
with open("paper.txt") as f:
    arr = []
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        arr.append(row)

def checkAdjacent(x, y, arr):
    total = 0
    height = len(arr)
    width = len(arr[0])

    # All eight directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < width and 0 <= ny < height:
            if arr[ny][nx] == '@':
                total += 1

    return total

def count_papers(arr):
    to_remove = []
    count = 0
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == '@':
                if checkAdjacent(x, y, arr) < 4:
                    to_remove.append((x, y))
                    count += 1
    return count, to_remove

def remove_papers(arr):
    count, to_remove = count_papers(arr)
    total_removed = count
    print("Removed:", count)

    for x, y in to_remove:
        arr[y][x] = '.'

    can_remove = True
    while can_remove:
        count, to_remove = count_papers(arr)
        total_removed += count
        for x, y in to_remove:
            arr[y][x] = '.'
        if count == 0:
            can_remove = False
    return total_removed


total_removed = remove_papers(arr)

print("Total rolls that can be removed: ", total_removed)

