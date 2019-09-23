##Understandin recursion
To understand recursion you have to understand recursion
- The key aspect is to describe a problem or an object as the compisition of the same problem/object but will smaller input
- This is a very old idea that comes primarily from math. The foundational concept behind recusion is mathematical induction.
  - mathematical induction
- In the case of a recursive algorithm, to correctly describe it indictively you need two things:
  - A set of one or more base cases (simplest irreducible inputs).
  - An indictive step which is a description of a problem using the same problem definition but with simpler inputs.

### Recursive objects
Lists (linked list), Trees (binary tree), Graphs and more
- You can define an object by reusing its own definition. This is the cornerstone of most the data structures used in computer science.
- The beauty of this concept lies in the fact that you can describe something potentially infinite (in practice, as large as your available memory) with a very simple yet precise definition.
- Using the definition, you will be able to also describe a solution of a problem involving these objects elegantly and succinctly

### Recursive computations
Factorial - product of all the numbers from 1 through itself
  - Ex: 5! = 1 * 2 * 3 * 4 * 5 = 120
- Multiply all integers from x to 1:
    x! = x(x - 1)(x - 2)
- Equivalently: 
    x! = x * (x - 1) (Inductive step)
      0! = 1 (Base Case)
- The second equation corresponding to the base case of the recusion, which describes the solution for the smallest/simplest input of that problem
```
# Code Example
int Fact(int a) {
  if (a == 0) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
```

Limitations
- Recursion you need a stack extra 
- Do base first

