#  File: Work.py
#  Student Name: Ryan Ashworth
#  Student UT EID: ryanash
#  Partner Name: Ramsay Ward
#  Partner UT EID: Rjw2777

import sys
import time


# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep

def sum_series(lines_before_coffee, prod_loss):
    if lines_before_coffee == 0:
        return 0
    else:
        return lines_before_coffee + sum_series(lines_before_coffee // prod_loss, prod_loss)


# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
#            return x, y

def linear_search(total_lines, prod_loss):
    count = 0
    for n in range(1, total_lines + 1):
        count += 1
        if sum_series(n, prod_loss) >= total_lines:
            x, y = (n, count)
            return x, y


# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee

def binary_search(total_lines, prod_loss):
    count = 0
    low = 0
    mid = total_lines // 2
    high = total_lines - 1
    while high >= low:
        count += 1
        mid = (high + low) // 2
        if sum_series(mid, prod_loss) < total_lines and sum_series(mid + 1, prod_loss) >= total_lines:
            mid += 1
            count += 1
            break
        elif sum_series(mid, prod_loss) < total_lines:
            low = mid + 1
        elif sum_series(mid, prod_loss) >= total_lines and sum_series(mid - 1, prod_loss) < total_lines:
            count += 1
            break
        elif sum_series(mid, prod_loss) > total_lines:
            high = mid - 1
        else:
            break
    x, y = (mid, count)
    return x, y


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Open input source
    # Change debug to false before submitting
    debug = False
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
