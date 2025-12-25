'''
example ID ranges: 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124

Invalid ID's:

any ID which is made only of some sequence of digits repeated twice


So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)


'''

def isInValid(integer):
    s = str(integer)
    # https://www.geeksforgeeks.org/python/python-check-if-string-repeats-itself/
    return (s in (s + s)[1:-1])

with open("Id_ranges.txt", "r") as f:
    id_str = f.read()

    p = id_str.split(",")
    s = []
    for id_range in p:
        s.append(list(map(int, id_range.split("-"))))
    # print(s)

    final_range = 0

    for i in s: # i = [11, 22]
        start = 0
        end = 0
        for j in i:
            if start == 0:
                start = j
            else:
             end = j
        #print("\nstart", start)
        # print("end", end)
        

        invalid = 0
        int_list = []
        for k in range(start, end + 1):
            int_list.append(k)

        not_valid = []
        for check in int_list:
            result = isInValid(check)
            if result == True:
                not_valid.append(check)

        # print(not_valid)

        final_range += sum(not_valid)

    print(final_range)

