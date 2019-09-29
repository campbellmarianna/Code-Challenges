'''
Prompt:
Find the runtime of this function, where A is an array of integers, and n is the size of array A.

int foo(int A[], int n) {
  int j = 0;
  for(int i = 0; i < n; ++i) {
    while(j < n && A[i] < A[j]) {
      j++;
    }
  }
  return j;
}
In Python:

def foo(A, n):
  j = 0
  for i in range(0, n):
    while(j < n and A[i] < A[j]):
      j += 1
  return j

Input Format
Elements of the array each separated from the other by space, like so:
5 4 3 2 7 8
Constraints

None

Output Format

One of the following

O(log n)
O(n)
O(n log n)
O(n^2)
O(n^3)
O(2^n)
O(n^n)
'''


def foo(A, n):
  j = 0
  for i in range(0, n):
    while(j < n and A[i] < A[j]):
      j += 1
  return j

print(foo([5,4,3,2,7,8], 6))