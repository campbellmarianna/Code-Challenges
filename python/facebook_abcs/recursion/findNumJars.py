'''
Prompt:
You got a lot of candy from trick-or-treating this Halloween and would like to store them safely in candy jars. Each jar can store at most C candies and you got plenty of jars. To distribute the candies, your plan is to divide the N candies in half, forming two smaller piles, then continue dividing each of the small piles in half until we get piles that can fit in the jars. Find how many jars you will need.

This strategy may not give you the least number of jars. Also note that when you divide an odd number pile in half, one of them will have one more than the other.

Input Format

Two lines with integers N and C

Constraints

1 < C < N < 10,000

Output Format

Numbers of jars you end up using with the given strategy

Sample Input 0
11
3

Sample Output 0
4

Explanation 0

First you divide 11 to 5 and 6. They are still too big. Split 5 -> 2, 3 Split 6 -> 3, 3 Each of them can now fit in the given jars, so we need four.

Sample Input 1
8
1

Sample Output 1
8

Explanation 1
If each jar can store only 1, then you need 8 jars

Sample Input 2
10
2

Sample Output 2
6

Explanation 2
10
5, 5
3, 2, 3, 2
2, 1, 2, 2, 1, 2
'''
def findNumJars_iterative(count, capacity):
  # In the case of capacity 1 each candy would fit in one jar
  if capacity == 1:
    return count
  div_count = 0
  while count > capacity:
    count /= 2
    div_count += 1
  return div_count * 2


# print(findNumJars_iterative(10, 2))


def findNumJars_recursive(count, capacity, div_count=0):
  # In the case of capacity 1 each candy would fit in one jar
  if capacity == 1:
    return count
  if count < capacity:
    result = div_count * 2
    return result
  else:
    return findNumJars_recursive(count/2, capacity, div_count + 1)


print(findNumJars_recursive(8, 1))
