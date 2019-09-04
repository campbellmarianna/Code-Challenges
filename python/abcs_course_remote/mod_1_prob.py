n = 10

1 - N/A

2 - prime

3 - prime

4 - not prime

5 - prime

6 - not prime

7 - prime
    
8 - not prime

9 - not prime

10 - not prime

------------------------------Go through steps you take to make the decision-------------------------------

n is 10

1 doesn't count

2 is prime
go to the next number 
is 3 divisible by 2? no
3 is prime 
go to the next number 
is 4 divisible by 2? yes
4 is not prime 
go to the next number
is 5 divisible by 2? no 
is 5 divisible by 3? no
is 5 divisible by 4? no
5 is prime
go to the next number
is 6 divisible by 2? yes 
6 is not prime
is 7 divisible by 2? no
is 7 divisible by 3? no
is 7 divisible by 4? no
is 7 divisible by 5? no
is 7 divisible by 6? no
7 is not prime

--Identify Structures ---------
given an input number
for every number under the input number check to see if the number is prime
    if it is, mark it as prime
    if it isn't, mark it as not prime
return the count of the prime numbers

is the input number prime
given an input number
for every number under the input number (except 1)
    check to is if the input number can be divided by the other number
    if it can't, move on to the next number
    if it can, the number is not prime
