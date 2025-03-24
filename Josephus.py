#  File: Josephus.py
#  Student Name: Ryan Ashworth
#  Student UT EID: ryanash
#  Partner Name: Ramsay Ward
#  Partner UT EID: Rjw2777

import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        if data is not None:
            new_node = Link(data)
        if self.first is None and self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            self.last.next = self.first

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current_node = self.first
        while current_node:
            if current_node.data == data:
                return current_node
            else:
                current_node = current_node.next
        return None

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        if self.first is None:
            self.is_empty()
        elif self.first.data == data and self.first == self.first.next:
            temp = self.first
            self.first = None
            self.last = self.first
            return temp
        elif self.first.data == data:
            temp = self.first
            self.last.next = self.first.next
            self.first = self.first.next
            return temp
        elif self.last.data == data:
            current = self.first
            while current != self.last:
                temp = current
                current = current.next
            self.last = temp
            self.last.next = self.first
            return current
        else:
            current = self.first
            while current.next != self.first:
                if current.next.data == data:
                    temp = current.next
                    current.next = current.next.next
                    return temp
                else:
                    current = current.next
            return None

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        current = self.find(start)
        for n in range(step - 1):
            current = current.next
        running = True
        while running:
            x = self.delete(current.data)
            try:
                return x.data, x.next.data
            except:
                running = False
                return


    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if self.first is None:
            return "[]"
        if self.first == self.last:
            return "[" + str(self.first) + "]"
        else:
            current = self.first
            string_list = "[" + str(current)
            current = current.next
            while current != self.first:
                string_list += ", " + (str(current))
                current = current.next
            string_list += "]"
            return string_list



# Input: Number of soldiers
# Output: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    new_list = CircularList()
    for n in range(1, num_soldiers + 1):
        new_list.insert(n)
    return new_list


# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    y = start_data
    for n in range (num_soldiers):
        try:
            (x, y) = my_list.delete_after(y, step_count)
            print(x)
        except:
            print(y)






''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create circular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
