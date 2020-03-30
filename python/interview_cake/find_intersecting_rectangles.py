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

def find_common_coordinates(rect_1, rect_2):
    '''Return a list of coordinates found in both rectangles'''
    return [(5, 4), (5, 3), (5, 2), (6, 2), (6, 3), (6, 4), (7, 2), (7, 3), (7,4) ]

def get_intersect_rect(common_coordinates):
    '''
    Return a rectangle as a dictionary with the following key vaue pairs.
    'left_x': INT,
    'bottom_y': INT,
    'width': INT,
    'height': INT
    '''
    return my_rectangle = {'left_x':...}



