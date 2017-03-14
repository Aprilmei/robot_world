import time
import matplotlib.pyplot as plt
from world2.stack_array import *

running_times = []

# Increase size of n in increments. 
for n in range (0, 1000, 10):
    s = stack(1000)
    # Add n elements to the set.


    start = time.time()
    for i in range(n):
        s.pushing(i)
    s.find_element(999)
    for i in range(n):
        s.poping()
    
    # Insert operation you want to test here
    end = time.time()

    run_time = end - start
    print(n, run_time)
    running_times.append(run_time)
# Plot the running times
plt.plot(running_times, 'bx')
plt.xlabel('Size of N (x 1000)')
plt.ylabel('Time')
plt.show()
plt.ion()
