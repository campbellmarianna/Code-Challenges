# Time Complexity
## 0(2^N) - Exponential Time (continued)
- 0(2^N) denotes an alogorithm whose growth doubles with each additon to the input data set
- The growth curve of an 0(2^N) function is exponential - starting off very shallow, then rising meteorically

```
int Fibonacci(int number) {
  if (number <= 1) return number;
  return Fibonacci(number - 2) + Fibonacci(number - 1);
}
```

Fibonacci is a complicated algorithm that will be covered in more detail in later lessons

## 0(log n) - Logarithmic Time

Other Common]

1. Drop the Constants
2. Drop the Less Significant Terms

# Space Complexity
- iterator in loop is constant space
  - We allocate memory for a loop counter and function arguments, but those are still constant memory allocations. For example, it's either 4 bytes (32-bit) or 8 bytes (64-bit) to store integers.

## 0(n) - Linear Space
- when a new data structure is created with the same data as the input the memory has now grown linearlly to given imput

## Interview Tips & Tricks
1. The purpose of Big O is to express the worst case scenario for time and space usage
2. Linear search means a linear time complexity 0(n) in which the item is not found or is the last item is perhaps one of the most obvious tips.
3. Any time you see nested loops (for, while, etc.) you can expect some form of a polynomial time complexity i.e. a quadruple nested for loops probably means 0(n^4)

Remember: the most efficient solutions do NOT necessarily appear to be the most elegant - sometimes you need to get "dirty" with sorting, caching, and repetition

- When you 