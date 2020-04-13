'''
You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.

Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean ↴ of all temps we've seen so far
get_mode()—returns a mode ↴ of all temps we've seen so far
Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.

get_mean() should return a float, but the rest of the getter methods can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..110.

If there is more than one mode, return any of the modes.

'''
# Create a class for tempertures and add 5 methods to get data on the temperature, then speed up all other methods over insert method
# no negatives
# get_mean() => float
# everthing else () => int
# no temps => None
# input => int

# Edge case
# empty temps list
# meant return
# handle negative values

# Suggested Improvements
# insert items in sorted order using BS # helpful resource: https://realpython.com/binary-search-python/

class TempTracker():
    def __init__(self): # take in list and add to temps
        self.temps = []


    def insert(self, item):
        '''Add item to temps list Big O Time: O(1)'''
        # check in the middle
        # if item == len(self.temps)//2:
        #     self.insert(len(self.temps)//2, item)
        # else:
        #     return self.insert()
        # before
        # after
        self.temps.append(item)

    def get_max(self):
        '''Returns the highest temp we've seen so far 
        Big O Time: O(n) because max function Big O Time is O(n)'''
        return max(self.temps)
    
    def get_min(self):
        '''Returns the lowest temp we've seen so far
        Big O Time: O(n) because min function Big O Time is O(n)'''
        return min(self.temps)
    
    def get_mean(self):
        '''Returns the mean of all temps we've seen so far Big O Time: O(n) assuming that every values has to be accessed to calculate the sum'''
        return float(sum(self.temps)//len(self.temps))

    def get_mode(self):
        '''
        Returns a mode of all temps we've seen so far
        Big O Time: O(n) n number of temperatures and Big O Space: 0(n - d) d duplicates in temps property 
        '''
        seen = dict()
        # look at each number
        for temp in self.temps:
            # keep track of how many times one has seen each number
            if temp not in seen:
                seen[temp] = 1
            else: # duplicate tempature
                seen[temp] += 1
        # return the number that is seen the most 
        max_temp = 0 # Doesn't work for negative temps
        max_occurances = 0
        for k,v in seen.items():
            if v > max_occurances:
                max_occurances = v
                max_temp = k
        return max_temp


if __name__ == '__main__':
    temp_tracker = TempTracker()
    temp_tracker.insert(80)
    print(temp_tracker.temps)  # [80]
    temp_tracker.insert(70)
    temp_tracker.insert(60)
    print(temp_tracker.get_max()) # 80
    print(temp_tracker.get_min() ) # 60
    print(temp_tracker.get_mean()) # [80, 70 , 60] = 370/5 = 70.0
    temp_tracker.insert(80)
    temp_tracker.insert(80)
    print(temp_tracker.get_mode()) # 80
    
