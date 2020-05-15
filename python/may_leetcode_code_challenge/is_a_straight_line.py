class Solution:
    def checkStraightLine_v1(self, coordinates: List[List[int]]) -> bool:
        # create expected variables
        expectedX = coordinates[0][0]
        expectedY = coordinates[0][1]
        # loop coordinates
        for coordinatePair in coordinates:
            if coordinatePair[0] != expectedX or coordinatePair[1] != expectedY:
                return False
            expectedX += 1
            expectedY += 1
        return True


class Solution:
    def checkStraightLine_v2(self, coordinates: List[List[int]]) -> bool:
        straight_counter = 0
        # loop coordinates
        i = 0
        while i < len(coordinates)-1:
            # check if the y values are increasing by one
            if abs(coordinates[i+1][1] - coordinates[i][1]) == 1:
                straight_counter += 1
            # check if the y values stay the same
            elif coordinates[i][1] == coordinates[i+1][1]:
                straight_counter += 1
            i += 1
        if straight_counter == len(coordinates)-1:
            return True
        return False


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True

        if coordinates[0][0] == coordinates[1][0]:

            x = coordinates[0][0]

            for i in range(2, n):
                if coordinates[i][0] != x:
                    return False
            return True

        if coordinates[0][1] == coordinates[1][1]:

            y = coordinates[0][1]

            for i in range(2, n):
                if coordinates[i][1] != y:
                    return False
            return True

        slope = (coordinates[1][1] - coordinates[0][1]) / \
            (coordinates[1][0] - coordinates[0][0])

        intercept = coordinates[0][1] - slope*coordinates[0][0]

        for i in range(2, n):
            if coordinates[i][1] != slope*coordinates[i][0] + intercept:
                return False

        return True


class Solution:
    def checkStraightLine_v3(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        slope = (coordinates[1][1]-coordinates[0][1]) / \
            (coordinates[1][0]-coordinates[0][0])
        # Check of the slope of the first two coordinates our different than than the slope of the first coordinates and every other coordinate pair
        for i in range(2, len(coordinates)):
            curr_slope = (coordinates[i][1]-coordinates[0]
                          [1])/(coordinates[i][0]-coordinates[0][0])
            if curr_slope != slope:
                return False
        return True
