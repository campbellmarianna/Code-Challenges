# https://leetcode.com/problems/consecutive-numbers-sum/

Approach  # 1: Brute Force [Time Limit Exceeded]
Intuition and Algorithm

For each starting number, we scan forward until we meet or exceed the target N. If we meet it, then it represents one way to write N as a sum of consecutive numbers.

For example, if N = 6, and we scan forward from 1, we'll get 1 + 2 + 3 = 6 which contributes to the answer. If we scan forward from 2, we'll get 2 + 3 + 4 (the first time that the sum is >= N) which is too big.


class Solution(object):
    def consecutiveNumbersSum(self, N):
        ans = 0
        for start in xrange(1, N+1):
            target = N
            while target > 0:
                target -= start
                start += 1
            if target == 0:
                ans += 1
        return ans

# Time Complexity: O(N^2)O(N 
# 2
#  )