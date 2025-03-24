#  File: Adjacency.py

#  Description: Converts an edge list into an adjacency matrix
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number:

import sys


def edge_to_adjacency(edge_list):
    vert = set()
    for edge in edge_list:
        vert.add(edge[0])
        vert.add(edge[1])
        
    
    vert = sorted(vert)
    num = len(vert)
    adj_matrix = [[0]*num for i in range(num)]
    for edge in edge_list:
        
        from_vertex = vert.index(edge[0])
        to_vertex = vert.index(edge[1])
        weight = edge[2]
        adj_matrix[from_vertex][to_vertex] = weight
    return adj_matrix
    
    
    

        
    

             
        
    
    


# remove formatting and convert to list of tokens
# do not change this method
def clean(text):
    text = text.strip()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("”", "")
    text = text.replace(" ", "")
    text = text.replace("\"", "")
    text = text.split(",")
    return text


''' DRIVER CODE '''

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('adjacency.in')
else:
    in_data = sys.stdin

# get line of input, remove formatting, convert to list of tokens
input_text = in_data.readline()
input_text = clean(input_text)

# convert one string to 2D list of edge data
edges = []
for i in range(0, len(input_text), 3):
    newList = [input_text[i], input_text[i+1], int(input_text[i+2])]
    edges.append(newList)

# convert the 2D list to an adjacency matrix
adj_matrix = edge_to_adjacency(edges)

print('\n'.join([' '.join([str(cell) for cell in row]) for row in adj_matrix]))
