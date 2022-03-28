import multiprocessing
from multiprocessing import Pool, TimeoutError
import queue

calls_queue = []

def waste_time(s: int):
    time.sleep(s)
    print(f'{s} seconds later')

def add_to_queue(runtime: int):
    try:
        calls_queue.append(runtime)
    except KeyboardInterrupt:
        print('calls added\n')

def execute_processes(calls_queue):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        p = [executor.submit(waste_time, sec) for call in calls_queue]

        for p in concurrent.futures.as_completed(results):
            print(p.result())

if __name__ == '__main__':
    
    for s in range(10):
        add_to_queue(s)
    
    execute_processes(calls_queue)