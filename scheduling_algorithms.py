import os                   # os will help to use system commands
import time                 # we will use time.sleep function to simulate working of processes
import copy

print("============  Practical 3 (Shortest Job First Scheduling Algorithm and Priority Scheduling Algorithm Visualisation ============")

n = int(input("Enter number of Processes: "))       # n will store total number of processes

proc = []                                           #proc list will store details of all the processes

for i in range(n):
    b_time = float(input("Enter Burst time for Process No {} (in milliseconds): ".format(i+1)))
    p = int(input("Enter Priority of Process No {} (lower makes process more preferable): ".format(i+1)))
    l = []                              #we will make a list for each process and append them to proc list
    l.append(i+1);
    l.append(b_time);
    l.append(p)
    proc.append(l)
    
os.system('clear')                      # clear the terminal for better output

print("============ Shortest Job First Scheduling Algorithm ============\n\n")
time.sleep(2)

sort_time = copy.deepcopy(proc)                    #sort_time is a copy of original proc list, which will be sorted on the basis of their burst times

sort_time.sort(key = lambda x:x[1]) #sorting based of second element of each sub list i.e. burt time

for i in range(n):                  # this loop will simulatw wroking of the processes
    print("Processing Process No {}".format(sort_time[i][0]))
    time.sleep(sort_time[i][1]/1000)
    print("Done\n\n")
    
avg = sort_time[0][1]
for i in range(1, n):
    sort_time[i][1] = sort_time[i-1][1] + sort_time[i][1]
    avg = avg + sort_time[i][1]

avg = avg / n                   # avg will have average of waiting + burst time of all the processes

print("============ Summary of Shortest Job First Scheduling Algorithm============\n")

for i in range(n):
    print("Process No {} took {} milliseconds (waiting time + burst time)".format(sort_time[i][0], sort_time[i][1]))
    
print("\n\nAverage time taken by each process was: {}".format(avg))

wait = input("Press Enter to continue")         # this will pause the program until user press ENTER
os.system('clear')

print("============ Priority Based Scheduling Algorithm ============\n\n")
time.sleep(2)

sort_prior = copy.deepcopy(proc)              #sort_prior is the copy of original proc list which would be sorted based on priority of the process

sort_prior.sort(key = lambda x:x[2]) #sorting based on second element of sublist i.e.  priority

for i in range(n):
    print("Processing Process No {}".format(sort_prior[i][0]))
    time.sleep(sort_prior[i][1]/1000)
    print("Done\n\n")
    
avg = sort_prior[0][1]
for i in range(1, n):
    sort_prior[i][1] = sort_prior[i-1][1] + sort_prior[i][1]
    avg = avg + sort_prior[i][1]

avg = avg / n

print("============ Summary of Priority Based Scheduling Algorithm============\n")

for i in range(n):
    print("Process No {} took {} milliseconds (waiting time + burst time)".format(sort_prior[i][0], sort_prior[i][1]))
    
print("\n\nAverage time taken by each process was: {}".format(avg))