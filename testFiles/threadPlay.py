import time
import random
import multiprocessing
import threading

def generate_random_numbers():
    # Generate random numbers
    for i in range(1000):
        num = random.randint(0, 1000000)

def run_threads(num_threads):
    # Create and start threads
    threads = []
    start_time = time.time()
    for i in range(num_threads):
        t = threading.Thread(target=generate_random_numbers)
        threads.append(t)
        t.start()

    # Wait for threads to finish
    for t in threads:
        t.join()

    end_time = time.time()

    return end_time - start_time

def run_processes(num_processes):
    # Create and start processes
    processes = []
    start_time = time.time()
    for i in range(num_processes):
        p = multiprocessing.Process(target=generate_random_numbers)
        processes.append(p)
        p.start()

    # Wait for processes to finish
    for p in processes:
        p.join()

    end_time = time.time()

    return end_time - start_time

if __name__ == '__main__':
    # Test with different numbers of threads and processes
    for num_threads in [1, 2, 4, 8, 16, 32]:
        print(f"Testing with {num_threads} threads and processes...")
        time_taken_threads = run_threads(num_threads)
        time_taken_processes = run_processes(num_threads)
        print(f"Time taken with threads: {time_taken_threads:.3f} seconds")
        print(f"Time taken with processes: {time_taken_processes:.3f} seconds\n")
