
# valid are non-duplicates: 111, 4890
# invalid duplicates: 11 (1 twice), 4040 (40 and 40)
p = [11, 12, 111, 1188511885, 12345]


def isInValid(integer):
    s = str(integer)
    # If s appears again inside (s+s)[1:-1], then s is a repeated substring.
    return (s in (s + s)[1:-1])

for i in p:
    print(isInValid(i))