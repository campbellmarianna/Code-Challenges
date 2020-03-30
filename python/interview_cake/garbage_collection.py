# Gabage Collection
# What is that?
# after using memory for a program before the program finishes empty variables so there is no extra unneccesary memory being used
# automatically frees up memory that the program isn't using anymore 

def get_min(nums):
    '''Big O Time: 0(N log N), Big O Space: 0(n)'''
    # Note: this is *not* the fastest way to get the min!
    nums_sorted = sorted(nums)
    return nums_sorted[0]


my_nums = [5, 3, 1, 4, 6]
print(get_min(my_nums))

# Manual Memory Management
# Some languages, like C, don't have a garbage collector. SO we need to manually free up any memory we've allocated once we're done with it:
// make a string that can hold 15 characters
// including the terminating null byte ('\0')
str = malloc(15);

// ... do some stuff with it ...

// we're done. free that memory!
free(str);

# Garbage collector stragies:
# - tracing garbage collection (carefully figure out what things in memory we might still be using or need later on and free everything else)
# - reference count ( have an object keep track of the number of things that reference it, free anything with a reference count of zero)