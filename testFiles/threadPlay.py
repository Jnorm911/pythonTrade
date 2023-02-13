import threading
import time

# Shared flag to control the threads
stop_flag = False

def worker1():
    while not stop_flag:
        print("Worker 1 is running")
        time.sleep(1)

def worker2():
    while not stop_flag:
        print("Worker 2 is running")
        time.sleep(2)

def worker3():
    while not stop_flag:
        print("Worker 3 is running")
        time.sleep(3)

def quitThreads():
    global stop_flag
    while not stop_flag:
        execute = input("Press Q to quit: ")
        if execute == "q":
            print("goodbye")
            stop_flag = True
            thread1.join()
            thread2.join()
            thread3.join()

# Start the threads
thread1 = threading.Thread(target=worker1)
thread2 = threading.Thread(target=worker2)
thread3 = threading.Thread(target=worker3)
thread4 = threading.Thread(target=quitThreads)
thread1.start()
thread2.start()
thread3.start()
thread4.start()

