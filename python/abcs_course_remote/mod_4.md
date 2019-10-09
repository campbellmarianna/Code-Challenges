## UMPIRE METHOD Review
Understand - clarify what the intereviewer is asking for
Match - Identify 
Plan
Implement
Review 
Evaluate

## Handy Python Tools for this week
- Lists
- List.append, list.pop, list.insert
- Sets & Set comprehensions
- Bitwise Operations & | ~ ^

Interviews
- 3 Types, most junior to least junior:
1. Can you code?
  - can this person take requirements and turn them into code 
2. Can you optimize (talking about how this solution works)
3. Can you design

Typical Interviews Expectations (ranked)
1. Understands the goals of the interviewe (litterally, ask!)
  - What are you actually looking for me to show you in this interview. or What are you testing for.
    - Do you want see code.
    - Do you want to see multiple solutions
    - Do you want 
2. Understands the problem
3. Wrestles with the problem
4. Discusses the problem
5. Creates a plan for the problem
6. Solves the problem
7. Tests the solution
8. Evauates the solution
9. Determines (and understands) improvements for the solution
10. Implements (and tests) the improvements
11. Solution is the most efficient solution

In Other Words...
- Functioning Solutions > Unfinished Solutions
  - Once you have a working solution then you and the other person can talk as people who have wrestled with the solution before.
- Working Solutions > Buggy Solutions
- Quickly Completed Solutions > Incomplete Optimized Solutions
BUT ...
- Optimized Solutions > Naive solutions

Speed matters- you can't optimize until you have something to optimize

Runtime Complexity
- How fast does the number of steps our program must take grow, in relation to the input?

Determining Runtime Complexity
1. Identify the input & determine which dimensions account for size
2. How many times do I interact with every element of the input?
  a. Count the loops
  b. Count the "hidden" loops
    - One line loops (secret complexity)
  c. Check your data structure access
3. How many times do I interact with data dependent on the input?
  a. Are there checks over filtered input data? How large might this be?
  b. Do I re-calculate anything? How often? What does that cost in execution time?
  c. As my space usage grows, does that cause any iteration size to grow?

**We do a number of operations based on given n**

Python lists are arrays in other languages
- In python lists are more flexiable meaning you can put elements with different types in the same list
  - ['hey', 1]

- In the number of steps increase in a predictable way - your input of n and do something 3 times to each element
  - that is a linear relationship

### How to analyze the runtime of your code
1. Look at operations that grow in respect to the input n
  - Ask yourself what line numbers cause our execution times to grow? Example for the single number problem: Lines 3, 4 ,and 5

#### Set
- something to make things a little easier
  - Like a list, but without duplicates
  - It is similar to a hashtable, a hashtable has key-value pairs 
  - A set is like a hashtable wether having keys and values a set just has keys and searching for a element is done in constant time, rather than looping over the entire array to find it 
  - Adding things to a set is constant time and removing things from a set is constant time

## When your preparing for internships interviews try to focus on the area that you want to go into for this next job or this next role
  - If you want to get into VR and graphics programming cool definitely check your bit manipulation skills

- The three solutions are three different appoaches for solving the problem

## Personal Narrative
- Tell me about yourself 
  - Signal things that you find exciting that are similar to the role that your working on
    - So if your interviewing at Microsoft and you want to work on the Xbox maybe your interested in Low Level Systems Programming and I have an audrio and I'm into these other things
    - Maybe you want to get a job at optimizing so your like I really have been reading a lot about distributed systems books lately and I've really been interested in how optimizing is ...
  - What your really trying to say is hey, I fit in at this group
    - That might mean you have to do a tiny bit of research to learn what the job is before you have two to three sentences really to say about yourself
    - So pick a company you might want to work at as a Software Engineer
    - What does that company do? Twitter
    - What role do I want to interview for? Software Engineer
    - 3 minutes Describe it where your whole career has been leading up to this job
    - youth move detroit I led cousoul meetings
    - product idea: poll to answer a question for a politican
    - buily reviewed by trucker so that trucker has a way to let their dispatcher know what is going on
    - I have experience with taking whiteboard ideas to market and creating a platform for others to heard and I want to continue these outcomes at twitter.
  