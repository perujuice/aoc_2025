'''
input: 
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 

Sum or multiply the columns

Sum up each result from each column
'''

# Below is just the solution for part 1 of the puzzle.
'''
import numpy as np
with open("math.txt", "r") as f:
    rows = []
    columns = []
    col = []
    for line in f:
        rows.append(line.strip().split())
    rows = np.array(rows)
    columns = rows.T # transpose the rows to more clearly represent the operations
    col = columns.tolist() # covert back to a python list

# For part 1
def calc(column_list):
    total = 0
    for i in column_list:
        operation = i.pop(-1)
        i = list(map(int, i))
        if operation == "+":
            res = sum(i)
            total += res
        else:
            res = 1
            for j in i:
                res = j * res
            total += res
    return total
'''
import math

def solve_cephalopod_math():
    grand_total = 0
    
    # Open the file as requested
    with open("math.txt", "r") as f:
        lines = f.readlines()

    # 1. Normalization: Remove newlines and pad lines to the max width
    #    so we have a perfect rectangular grid.
    lines = [line.replace('\n', '') for line in lines]
    if not lines:
        return 0
        
    max_width = max(len(line) for line in lines)
    grid = [line.ljust(max_width) for line in lines]
    
    # 2. Parse Columns Right-to-Left
    #    We collect numbers for the "current problem" in a list.
    current_problem_nums = []
    current_operator = None
    
    # Iterate column index from Right (max_width - 1) to Left (0)
    for col_idx in range(max_width - 1, -1, -1):
        
        # Extract the vertical column
        col_chars = [row[col_idx] for row in grid]
        
        # Separate the logic: Top rows are digits, Bottom row is operator/footer
        digits_part = col_chars[:-1]
        footer_char = col_chars[-1]
        
        # Check if the entire column is empty (separator)
        is_column_empty = all(c == ' ' for c in col_chars)
        
        if is_column_empty:
            # Separator found: If we have accumulated numbers, solve the problem
            if current_problem_nums:
                result = calculate(current_problem_nums, current_operator)
                grand_total += result
                
                # Reset for the next problem
                current_problem_nums = []
                current_operator = None
            continue

        # If not empty, parse the number in this column
        # Read digits top-to-bottom
        num_str = "".join([c for c in digits_part if c.isdigit()])
        
        if num_str:
            current_problem_nums.append(int(num_str))
        
        # Check for operator in the footer (bottom row)
        # It usually appears in one of the columns of the problem block
        if footer_char in "+*-/":
            current_operator = footer_char

    # 3. Final Calculation
    #    Handle the very last problem (leftmost) if the file didn't start with spaces
    if current_problem_nums:
        result = calculate(current_problem_nums, current_operator)
        grand_total += result

    print(f"Grand Total: {grand_total}")

def calculate(numbers, operator):
    """
    Performs the operation on the list of numbers.
    """
    if not numbers:
        return 0
    
    # Default to addition if no operator is found (though the puzzle implies there always is one)
    if operator == '+' or operator is None:
        return sum(numbers)
    
    elif operator == '*':
        return math.prod(numbers)
        
    # Handling other standard operators just in case
    elif operator == '-':
        # Subtraction is usually strictly left-associative, but in this column format
        # with multiple operands, it implies: num1 - num2 - num3...
        res = numbers[0]
        for n in numbers[1:]:
            res -= n
        return res
        
    elif operator == '/':
        res = numbers[0]
        for n in numbers[1:]:
            res /= n
        return res
        
    return 0

if __name__ == "__main__":
    solve_cephalopod_math()