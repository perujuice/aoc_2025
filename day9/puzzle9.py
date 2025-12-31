from collections import deque

grid_idx = []

with open("day9/input.txt", "r") as f:
    for line in f:
        if line.strip():
            coord = list(map(int, line.strip().split(',')))
            grid_idx.append(coord)

unique_x = sorted(list(set(p[0] for p in grid_idx)))
unique_y = sorted(list(set(p[1] for p in grid_idx)))

map_x = {val: i*2 for i, val in enumerate(unique_x)}
map_y = {val: i*2 for i, val in enumerate(unique_y)}

comp_w = (len(unique_x) * 2) + 2
comp_h = (len(unique_y) * 2) + 2

grid = [[0 for _ in range(comp_w)] for _ in range(comp_h)]

num_points = len(grid_idx)
for k in range(num_points):
    p1 = grid_idx[k]
    p2 = grid_idx[(k + 1) % num_points]
    
    cx1, cy1 = map_x[p1[0]] + 1, map_y[p1[1]] + 1
    cx2, cy2 = map_x[p2[0]] + 1, map_y[p2[1]] + 1
    
    if cx1 == cx2: # Vertical
        start, end = sorted([cy1, cy2])
        for r in range(start, end + 1):
            grid[r][cx1] = 1
    else: # Horizontal
        start, end = sorted([cx1, cx2])
        for c in range(start, end + 1):
            grid[cy1][c] = 1

queue = deque([(0, 0)])
grid[0][0] = -1 

while queue:
    r, c = queue.popleft()
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < comp_h and 0 <= nc < comp_w:
            if grid[nr][nc] == 0:
                grid[nr][nc] = -1
                queue.append((nr, nc))

sum_table = [[0 for _ in range(comp_w + 1)] for _ in range(comp_h + 1)]
for r in range(comp_h):
    for c in range(comp_w):
        val = 1 if grid[r][c] != -1 else 0
        sum_table[r+1][c+1] = val + sum_table[r][c+1] + sum_table[r+1][c] - sum_table[r][c]

def get_rect_sum(r1, c1, r2, c2):
    return sum_table[r2+1][c2+1] - sum_table[r1][c2+1] - sum_table[r2+1][c1] + sum_table[r1][c1]

areas = []

for i in range(len(grid_idx)):
    for j in range(i + 1, len(grid_idx)):
        p1 = grid_idx[i]
        p2 = grid_idx[j]

        cx1, cx2 = sorted([map_x[p1[0]] + 1, map_x[p2[0]] + 1])
        cy1, cy2 = sorted([map_y[p1[1]] + 1, map_y[p2[1]] + 1])
        
        comp_w_rect = cx2 - cx1
        comp_h_rect = cy2 - cy1

        tiles_needed = (comp_w_rect + 1) * (comp_h_rect + 1)
        
        tiles_found = get_rect_sum(cy1, cx1, cy2, cx2)
        
        if tiles_found == tiles_needed:

            real_w = abs(p1[0] - p2[0])
            real_h = abs(p1[1] - p2[1])
            
            area = (real_w + 1) * (real_h + 1)
            areas.append(area)

areas.sort(reverse=True)

print("Biggest valid area:", areas[0])