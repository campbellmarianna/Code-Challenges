x = 5
y = 10
z = 22
def checks(x, y, z):
    if x > y:
        print('x is greater than y')
    elif x == z:
        print('x is less than z')
    elif 5 == 2:
        print('5 is greater than 2')
    else:
        print('if and elif(s) never ran')


print(checks(x=5, y=10, z=22))

# Boolean Logic
# In Or statement if one statement is true we return True

# For Loops
# Built within Python - range()
# range(start, stop)

sum = 0
def loopPractice():
    # using range within list comprehension
    print([num for num in range(3, 31, 3)])
    # looping statement, execute a block of code on each item
    # for i in range(10): # i = 
    #     sum = sum + i
    #     print(sum)
    for i in range(5):
        print(i)
    print(range(0,5))
    a = ['mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])
    print(list(range(0, 20, 3)))

loopPractice()

# Modulo
    # What's left over after division
    # Capture remainder vale

def moduloPractice():
    print(3 % 7)
    print(10 % 2)
    print(17 % 2)

    num = 7
    if num % 2 == 0:
        print('Even!')
    else:
        print('Odd!')

moduloPractice()
