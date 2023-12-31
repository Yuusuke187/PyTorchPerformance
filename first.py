import torch
import time
import asyncio

start_time = time.time()

# main program -find sum to first 1 million numbers
sum_x = 0
for i in range(1000000):
    sum_x += i
    
# wait for 3 seconds
time.sleep(3)
print('Sum of first 1 million numbers is:', sum_x)

end_time = time.time()

execution_time = end_time - start_time
print('Execution time: ', execution_time, ' seconds')

async def first_million_sum():
    sum_x = 0
    for i in range(1000000):
        sum_x += i
    return sum_x

asyncio.run(first_million_sum())
