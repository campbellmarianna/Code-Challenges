def server_time_check(task_config, task_times):
    '''
    Return the estimated number of completed tasks given a list of 
    task times each task will take and the total execution time the server has available.
    '''
    infile = open("server/server-01.in", "r")

    lines = infile.readlines()
    # print("First line:", lines[0])
    # print("Second line:", lines[1])
    n, T = lines[0].split()
    T = int(T)
    n = int(n)
    t_times = []
    t_times = lines[1].split()
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
    return tasks_completed_counter

## Please do not change the code below this line
## These lines are how the tests interact with the code

# task_config = input(
#     "Please input the number of tasks, and the maximum total execution time:")
# task_times = input(
#     "Please input the execution times of each task, seperated with a space:")

# server_time_check(task_config, task_times)


server_time_check("10 60", "20 7 10 8 10 27 2 3 10 5")
