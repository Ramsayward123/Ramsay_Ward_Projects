#  File: Spiral.py
#  Student Name: Ryan Ashworth
#  Student UT EID: ryanash
#  Partner Name: Ramsay Ward
#  Partner UT EID: Rjw2777

import sys
from typing import List, Any


# Input: n
# Output:
def get_dimension(in_data):
    pass
    cont = True
    while cont:
        num = in_data.readline()
        try:
            size = int(num)
            if size > 0:
                cont = False
            else:
                print("Invalid data")
                num = in_data.readline()
        except ValueError:
            print("Invalid data")
            num = in_data.readline()
    return size



# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    pass
    num_boxes_needed = 1
    box_counter = 0
    move_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    move_dir_index = 0
    if not n % 2:
        n += 1
    r = n // 2
    c = n // 2
    spiral = []
    for row in range(n):
        spiral.append([])
        for col in range(n):
            spiral[row].append([])
    spiral[r][c] = 1
    for i in range( 2, ( n ** 2 + 1 )):
        if box_counter != num_boxes_needed:
            r = r + move_dir[move_dir_index][0]
            c = c + move_dir[move_dir_index][1]
            spiral[r][c] = i
            box_counter += 1
        else:
            box_counter = 0
            move_dir_index += 1
            if move_dir_index == 4:
                move_dir_index = 0
            if not move_dir_index % 2:
                num_boxes_needed += 1
            r = r + move_dir[move_dir_index][0]
            c = c + move_dir[move_dir_index][1]
            spiral[r][c] = i
            box_counter += 1
    return spiral



# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    pass
    line = in_data.readline()
    while line:
        try:
            line = int(line)
            sum_adjacent_numbers(spiral, line)
        except:
            print("Invalid data")
        line = in_data.readline()


# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    pass
    adjacent_boxes = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    sum_adjacent = 0
    for i in range( len(spiral)):
        for j in range (len(spiral[0])):
            if spiral[i][j] == n:
                x, y = (i, j)
                for box in adjacent_boxes:
                    if 0 <= (x + box[0]) <= len(spiral[0])-1 and 0 <= (y + box[1]) <= len(spiral[0])-1:
                        sum_adjacent += spiral[(x + box[0])][(y + box[1])]
    print(sum_adjacent)







# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print('%4s'%(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():
    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    #print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
