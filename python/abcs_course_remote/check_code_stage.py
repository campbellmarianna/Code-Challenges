# def atoi(str):
#     '''Converts a string into an integar'''
#     # Remove whitespace at the start and end of the string
#     str = str.strip()
#     # Base case - check for invalid string
#     if str == '':
#         return 0
#     optional_sign = ''
#     result = ''
#     for char in str:
#         # Take an optional initial plus or minus sign
#         if str.index(char) == 0:
#             if char == '-' or char == '+':
#                 optional_sign = char
#                 result += char
#                 continue
#             # Check if first non-whitespace char in str is  invalid integral number
#             elif char.isnumeric() is False:
#                 return 0
#         # Take numerical digits and interprets as numerical values
#         if char.isnumeric():
            # result = result.__str__()
            # char = char.__str__()
            # result = int(result + char)
#     # Check if the result is within the 32 bit range
#     binary_representation = '{:032b}'.format(result)
#     if len(binary_representation) > 32:
#         if optional_sign == '-':
#             return -2 ** 31
#         else:
#             return 2 ** 31
#     return result


def myAtoi(str: str) -> int:
    '''Converts a string into an integar'''
    a = str
    # Remove whitespace at the start and end of the string
    a = a.strip()
    # Base case - check for invalid string
    if a == '':
        return 0
    optional_sign = ''
    result = 0
    for char in a:
        # Take an optional initial plus or minus sign
        if a.index(char) == 0:
            if char == '-' or char == '+':
                optional_sign = char
                result += char
                continue
            # Check if first non-whitespace char in str is  invalid integral number
            elif char.isnumeric() is False:
                return 0
        # Take numerical digits and interpretsas numerical values
        if char.isnumeric():
            result = result.__str__()
            char = char.__str__()
            result = int(result + char)
        else: 
            break;
    # Check if the result is within the 32 bit range
    # print("Result type:" type(result))
    binary_representation = '{:032b}'.format(result)
    if len(binary_representation) > 32:
        if optional_sign == '-':
            return -2 ** 31
        else:
            return 2 ** 31
    return result


str = "3.14159"
val = myAtoi(str)
print(val)
print(type(val))
