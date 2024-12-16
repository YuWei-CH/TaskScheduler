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

cpu_intensive_task()