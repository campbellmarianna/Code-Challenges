
class Solution:
    def findComplement(self, num: int) -> int:
        bit_rep = bin(num)
        bit_rep = bit_rep[2:]
        new_bit_rep = ''
        for n in bit_rep:
            if n == '0':
                new_bit_rep += '1'
            else:
                new_bit_rep += '0'
        return int(new_bit_rep, base=2)


def findComplement(num: int) -> int:
        def flip(c):
            return '1' if (c == '0') else '0'
        bit_rep = bin(num)
        bit_rep = bit_rep[2:]
        new_bit_rep = ''
        for n in bit_rep:
            new_bit_rep += flip(n)
        return int(new_bit_rep, base=2)

# Credits:
# - https://www.geeksforgeeks.org/1s-2s-complement-binary-number/
