'''
The beam enters at the S and goes downwards

They pass freely through empty space (.)

the beam stops on a splitte (^)

a new tachyon beam continues from the immediate left 
and from the immediate right of the splitter.

'''

grid = []

with open("day7/input.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))


original_grid = [row[:] for row in grid]


def start(grid):
    first_line = grid[0]
    for char in range(len(first_line)):
        if first_line[char] == "S":
            return char


def first_beam(idx):
    grid[1][idx] = "|"


def find_splitter(grid):
    for line in range(1, len(grid) - 1):
        current_line = grid[line]
        next_line = grid[line + 1]
        for char in range(1, len(current_line) - 1):

            if grid[line - 1][char] == "|" and current_line[char] == ".":
                current_line[char] = "|"
            if current_line[char] == "^" and grid[line - 1][char] == "|":
                current_line[char] = "X"
                if next_line[char - 1] == ".":
                    next_line[char - 1] = "|"
                if next_line[char + 1] == ".":
                    next_line[char + 1] = "|"

def count_split(grid):
    count = 0
    for line in grid:
        for char in line:
            if char == "X":
                count += 1
    return count

def count_timelines(grid):
    rows = len(grid)
    cols = len(grid[0])
    memo = {}

    def propagate(r, c):
        if c < 0 or c >= cols:
            return 0
        if r == rows - 1:
            return 1
        if (r, c) in memo:
            return memo[(r, c)]

        cell = grid[r][c]
        if cell == "." or cell == "S":
            result = propagate(r + 1, c)
        elif cell == "^":
            left = propagate(r + 1, c - 1) if c - 1 >= 0 else 0
            right = propagate(r + 1, c + 1) if c + 1 < cols else 0
            result = left + right
        else:
            result = 0

        memo[(r, c)] = result
        return result

    sidx = start(grid)
    return propagate(0, sidx)


sidx = start(grid)
first_beam(sidx)
find_splitter(grid)

total_splits = count_split(grid)
print("total split count:", total_splits)

# Run quantum simulation using original grid
total_timelines = count_timelines(original_grid)
print("total quantum timelines:", total_timelines)

# Just for printing the grid
for line in grid:
    print("".join(line))


