'''
The password has changed and is now in the document attached
It is locked in a safe with number 0 to 99
the attached document (input document )
the dial start poiting at 50
So the input sequence is one instruction per line indicating which direction to rotate and
then move the pointer. 
we need to track all moves, and when the dial points at zero we need to sum up the number of
time the dial points at zero
That number is the password.
'''
dial_size = 100
pos = 50
num_instr = 0
count_zeros = 0

with open("sequence.txt") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])
        
        if direction == "L":
            # Count complete wraps
            complete_wraps = steps // dial_size
            count_zeros += complete_wraps
            
            # Check partial rotation
            remaining_steps = steps % dial_size
            new_pos = (pos - steps) % dial_size
            
            # Did we cross zero in the partial rotation?
            # Going left from pos, we cross 0 if remaining_steps >= pos (but pos != 0)
            if remaining_steps > 0 and remaining_steps >= pos and pos != 0:
                count_zeros += 1
            # Or if we land exactly on zero and didn't already count it as a crossing
            elif new_pos == 0 and not (remaining_steps > 0 and remaining_steps == pos and pos != 0):
                count_zeros += 1
                
        else:  # 'R'
            # Count complete wraps
            complete_wraps = steps // dial_size
            count_zeros += complete_wraps
            
            # Check partial rotation
            remaining_steps = steps % dial_size
            new_pos = (pos + steps) % dial_size
            
            # Did we cross zero in the partial rotation?
            # Going right from pos, we cross 0 if pos + remaining_steps >= dial_size (but pos != 0)
            if remaining_steps > 0 and pos + remaining_steps >= dial_size and pos != 0:
                count_zeros += 1
            # Or if we land exactly on zero and didn't already count it as a crossing
            elif new_pos == 0 and not (remaining_steps > 0 and pos + remaining_steps == dial_size and pos != 0):
                count_zeros += 1
        
        event = f"-> count now {count_zeros}"
        print(f"Start {pos:2d}, instr {line:4s} -> new {new_pos:2d} {event}")
        pos = new_pos
        num_instr += 1
        
print(f"\nTotal zero events: {count_zeros} after {num_instr} instructions")