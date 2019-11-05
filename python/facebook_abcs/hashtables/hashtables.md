# Hash Tables
The other backbone of many important algorithms
- the key is the name of the person in an addres book 
- the array locations are based on the hash code of the key 
- the load factor is defined as n/m grows
- if the load factor gets too big makes it slower so we have to rehash 
- The efficiency of a hash table is based on the quality of the hash function
## Derived Data Structures
- A hash table is good data structure to represent a dictionary
- A trie - also called digital tree
- Hash Tables are used to create sets
- Hash tables are commonly ised to compare associative arrays

## During Interviews
- It is good to think of hash tables as a simple data structure that pairs keys to values
- Due to the possibility of collision, the worst case time complexity for lookup and insertion operation is actually 0(n); however, the average case is 0(1)
- Space complexity will always be o(n) where n is the number of keys
- Hash tables are considered unordered because keys are not guaranteed to be arranged by insertion order
- Explooiting the 0(1) insertion and loopup, hash tables are typically used in algorithms to cache  the results of a complex operations - this can easily lower the time complexity by an order i.e. 0(n^2) to 0(n) with the tradeoff of using additional memory
- Many languages such as PHP (keyed array), Python (dictionary), JavaScript(object), Perl (associate array), etc. already have some form of a hash table already built-in, so there's no need to re-invent the wheel - however, **keys are typically restricted to being (or coerced into) strings**