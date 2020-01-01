'''
Prompt #1
Clusters of Activity
# # Problem Link: https://repl.it/student/submissions/9814047
# Write a function that accepts a 2D plane as a dictionary. The dictionary represents a segment of a map, and it contains map coordinates as keys, and a count of outbreaks in the area as values. The map may be huge, which is why we're using a dictionary(because most of the map will be 0s otherwise.)

# Find the center of the outbreak. The center is defined as the average of all points, but treat each case as one data point(eg, if there are 10 reports in one location, add that location to the average 10 times). Round to the nearest integer values, but return as a string: "x,y".

Example Data:
reported_outbreak = {
    "5,5": 10,
    "5,6": 8,
    "5,4": 8,
    "4,5": 8,
    "4,5": 8,
    "4,6": 8,
    "6,6": 7,
    "6,5": 8,
    "4,4": 8,
    "3,4": 4,
    "3,3": 2,
    "6,7": 2
}
'''

def find_center(matrix):
  avg_x = 0
  avg_y = 0
  total_cases = 0

  for coords, cases in matrix.items():
    while cases > 0:
      total_cases += 1
      cases -= 1
      print(coord)
      x, y = coords.split(" , ")
      avg_x += x
      avg_y += y

  avg_x = avg_x / total_cases
  avg_y = avg_y / total_cases
  return avg_x, avg_y


reported_outbreak = {
    "5,5": 10,
    "5,6": 8,
    "5,4": 8,
    "4,5": 8,
    "4,5": 8,
    "4,6": 8,
    "6,6": 7,
    "6,5": 8,
    "4,4": 8,
    "3,4": 4,
    "3,3": 2,
    "6,7": 2
}

print(find_center(reported_outbreak))

'''
Prompt 2:
Natural Language Calculator
You are working on a very small part of a natural language processing engine. You want your engine to be able to respond to math properly. Your colleagues have written a program that can identify when a user is asking a math question, but they haven't written a calculator!
Your job is to create a calculator that will parse natural language, and speak in natural language. To simplify the problem, you will only ever receive two operands, and all operands will be under one hundred.

Given a statement like:
"add two and seven"
return "nine".

"subtract six from four"
return "negative two"


To help with this, recognize that dictionaries can hold any value, including functions!
'''


def nlp_calculator(statement):
  commands = statement.split(" ")
  # translate the command into a function
  func = translator.get(commands[0])
  # print(f"Commands:{commands}")
  first_number = translator.get(commands[1])
  second_number = translator.get(commands[3])
  # print(f"first_number: {first_number }, second_number: {second_number} ")
  result = func(second_number, first_number)
  # print(f"result:{result}")
  transalted_result = translator.get(result)
  # print(f"transalted_result:{transalted_result}")
  return transalted_result
  # return ""


def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


translator = {
    "add": add,
    "subtract": subtract,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    -2: "negative two"
}

test1 = "add two and seven"
test2 = "subtract six from four"

print(nlp_calculator(test1))
# print(nlp_calculator(test2))
