'''
Exercism Problem:
Manage robot factory settings.

When robots come off the factory floor, they have no name.

The first time you boot them up, a random name is generated in the format of
two uppercase letters followed by three digits, such as RX837 or BC811.

Every once in a while we need to reset a robot to its factory settings, which
means that their name gets wiped. The next time you ask, it will respond with a new random name.

The names must be random: they should not follow a predictable sequence.
Random names means a risk of collisions. Your solution must ensure that every existing robot has a unique name.'''

import random
import string
uppercase_letters = string.ascii_uppercase


def generate_name():
    # generate two uppercase letter by random
    rand_index = generate_rand_index()
    rand_index_2 = generate_rand_index()
    first_part_name = uppercase_letters[rand_index] + uppercase_letters[rand_index_2]
    # generate 3 nums by random
    rand_num = generate_rand_index(9)
    rand_num_2 = generate_rand_index(9)
    rand_num_3 = generate_rand_index(9)
    # concatencate the letters and numbers
    second_part_name = str(rand_num) + str(rand_num_2) + str(rand_num_3)
    # return result
    return first_part_name + second_part_name

# helper for function that generates random name
def generate_rand_index(max=26):
    return random.randint(0, max - 1)

class Robot(object):
    # generate a new name the first time a rebot is booted up
    def __init__(self, name=None):
        self.name = generate_name()

    # the name of the robot gets wiped
    def reset(self):
        self.name = None
        # alter the random generatr so that is doesn't share same state
        random.seed('Robot not the same')
        self.__init__()

# execute code exactly as it is written not how you think it should work
if __name__ == '__main__':
    robot = Robot()
    print(robot.name)
    print(robot.reset())
    print(robot.name)
    # print(generate_name())
