# Strings and Arrays Prework
The simplest data structure
- Arrays represent collections of object of the same type.
- Typically implemented as a single contiguous memory block that stores these elements sequentially.
  - Single contiguous memory block
      - One data element after another is stored in a block
        - At a contigous address
      - Fixed length
      - A  way of organizing a program in memory


  - Sequential - one after the other 
- Each element on an array is accessed by using an index Usually [0, size-1].
- **Accessing elements in an array is a very fast operation.**
- **Array is great for storing information when all of it are the same type.**

- Pros:
  - Almost all programming languages support 
  - Reading/writing and 0(1) operation
- Limitations:
    - arrays  are not a dynamic data structure
    - To add a new element in a full array you need to copy the old array with extra capacity which is an expensive 0(n) operation
- Common uses
  - As a support data struutre: 
    - Used to implement lists, stacks, queues, heaps.
    - C++ standard library `std::vector<T>` which is dynamic array and `std::deque<T>` which is an efficient double ended queue.
  - To efficiently perform computations on all elements in parallel. In distributed systems this is called a map operation.
  
    ```python
    '''
    Square elements in an array

    Example of a map operation
    '''
    # We're squring every element and then sorting the squared value in the same location
    def square_elements(a):
      for i in range(0, len(a))
        a[i] = a[i] * a[i];
        
    square_elements(6)
    ```

  - **Aggregation**, perform a computation on an array that yields a single result (like summing all elements). In distributed systems, this is called a **reduce** operation.
  - To sort or select elements
