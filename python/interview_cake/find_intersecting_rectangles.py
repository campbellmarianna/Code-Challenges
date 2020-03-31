'''
Return the reactangle intersection within two rectangles
  my_rectangle = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

}
'''
# Input: 2 Rectangles (format: dictionary with four key value pairs that are coordinates of the bottom left corner, width and height)
# Output: 1 Rectangle (same format)

# No diagonal rectangles
# Always straight
# Each side parallel

# Assumptions and Edge Cases
# Function arguments are always valid rectangles that intersect
# X and Y values are positive

# Solution Idea
# Find intersecting coordinates
# Find bottom-left, width, and height of intersecting triangle

rect_1 = {
    # Coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,

    # Width and height
    'width': 6, # x
    'height': 3, # y
}
#  create x boundary = width + 1 = 7
# create y boundary = height + 1 = 4
# x = 2
# for every width value 
    # Get the height increment until outside of boundary 4
    # y = 4
[(1, 1), (1, 2), (1, 3), (1, 4),
]
rect_2 = {
    # Coordinates of bottom-left corner
    'left_x': 5,
    'bottom_y': 2,

    # Width and height
    'width': 6,
    'height': 3,
}
def find_common_coordinates(rect_1, rect_2):
    '''Return a list of coordinates found in both rectangles'''
    # Generate all coordinates for rect 1
    rect_1_coordinates = []
    x_bound = rect_1['width'] + 1
    y_bound = rect_1['height'] + 1
    x = rect_1['left_x']
    for _ in range(0, x_bound):
        y = rect_1['bottom_y']
        for _ in range(0, y_bound):
            coordinate_pair = (x, y)
            # add them to a list
            rect_1_coordinates.append(coordinate_pair)
            y += 1
        x += 1
    common_coordinates = []
    # Generate all coordinates for rect 2
    x_bound = rect_2['width'] + 1
    y_bound = rect_2['height'] + 1
    x = rect_2['left_x']
    for _ in range(0, x_bound):
        y = rect_2['bottom_y']
        for _ in range(0, y_bound):
            coordinate_pair = (x, y)
            if coordinate_pair in rect_1_coordinates:
                # add them to a list
                common_coordinates.append(coordinate_pair)
            y += 1
        x += 1
    # Return common...
    return common_coordinates
    # return [(5, 4), (5, 3), (5, 2), (6, 2), (6, 3), (6, 4), (7, 2), (7, 3), (7,4) ]

def get_intersect_rect(common_coordinates):
    '''
    Return a rectangle as a dictionary with the following key vaue pairs.
    'left_x': INT,
    'bottom_y': INT,
    'width': INT,
    'height': INT
    '''
    pass
    # return my_rectangle = {'left_x':...}


print(find_common_coordinates(rect_1, rect_2))

