from multiprocessing import Pool
import time

def cpu_intensive_task():
    num = 2
    while num < 10 ** 10:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
        num += 1
num_cores = 10  # You can adjust this number
pool = Pool(processes=num_cores)

# Start CPU-intensive tasks on all cores
results = []
for _ in range(num_cores):
    results.append(pool.apply_async(cpu_intensive_task))

for result in results:
    result.get()