'''
Prompt:
You are in charge of a server that needs to run some submitted tasks on a first-come, first-served basis. Each day, you can dedicate the server to run these tasks for at most T minutes. Given the time each task takes, you want to know how many of them will be finished today.

Consider the following example:

Assume T = 180 and the tasks take 

45, 30, 55, 20, 80 and 20 minutes(in the order that they are submitted). Then, only four tasks can be completed. The first four tasks can be completed because they take 150 minutes, but not the first five, because they take 230 minutes which is greater than 180. Notice that although there is enough time to perform the sixth task(which takes 20 minutes) after completing the fourth task, you cannot do that because the fifth task is not done yet.


Input
The input consists of a two lines.

The first line contains two integers n and T.
1 ≤ n ≤ 50 is the number of tasks
1 ≤ T ≤ 500 is the total amount of execution time available.

The second line contains n positive integers, separated by spaces, smaller than 100, indicating how long each task takes in order they are submitted(the same order they must be evaluated in).
1 < n < 100 - the input looks like this:
n n n n n

Output
Display(by printing) the number of tasks that can be completed in T minutes on a first-come, first-served basis.


Sample Input 1
6 180
45 30 55 20 80 20

Can I do this task 180 >= 45? Yes
180 - 45
Task completed 1
Can I do anoter task 135 >= 30? Yes
130 - 35
Task completed 2
Can I do anoter task 105 >= 55? Yes
105 - 55
Task completed 3
Can I do anoter task 50 >= 20? Yes
50 - 20
Task completed 4
Can I do anoter task 30 >= 80? No
Completed tasks is 4

Sample Output 1
4


Sample Input 2
10 60
20 7 10 8 10 27 2 3 10 5 #5

Sample Output 2
5
'''
def server_time_check(task_config, task_times):
    '''
    Return the estimated number of completed tasks given a list of 
    task times each task will take and the total execution time the server has available.
    '''
    n, T = task_config.split()
    T = int(T)
    n = int(n)
    t_times = []
    t_times = task_times.split()
    tasks_completed_counter = 0
    # Evaluate each task time to see if it can be excuted by the server
    for task_time in t_times:
        task_time = int(task_time)
        # Check if there is enough execution time to do the task
        if T >= task_time: 
            T -= task_time
            tasks_completed_counter += 1
        else:
            break
    print(tasks_completed_counter)

## Please do not change the code below this line
## These lines are how the tests interact with the code

# task_config = input(
#     "Please input the number of tasks, and the maximum total execution time:")
# task_times = input(
#     "Please input the execution times of each task, seperated with a space:")

# server_time_check(task_config, task_times)


server_time_check("10 60", "20 7 10 8 10 27 2 3 10 5")
