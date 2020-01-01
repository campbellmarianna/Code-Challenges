a_list = ["strings", 11, 33, True]

a_variable = "anything"

a_dict = {
  "a string": True,
  234: "anything",
  "stuff":"things",
  a_variable: a_variable
}

another_dict = dict()

for item in a_list:
  if item % 2 == 0:
    another_dict["even"]append(item)
  else:
    another_dict["odd"].append(item)

print(another_dict)