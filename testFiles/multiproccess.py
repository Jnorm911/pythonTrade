import multiprocessing
import time

def func1(stop_event):
    while not stop_event.is_set():
        print("Function 1 running...")
        # Do some work here
        time.sleep(1)
    print("Function 1 stopped.")

def func2(stop_event):
    while not stop_event.is_set():
        print("Function 2 running...")
        # Do some work here
        time.sleep(2)
    print("Function 2 stopped.")

if __name__ == '__main__':
    # Create a shared event object
    stop_event = multiprocessing.Event()

    # Create processes for each function
    p1 = multiprocessing.Process(target=func1, args=(stop_event,))
    p2 = multiprocessing.Process(target=func2, args=(stop_event,))

    # Start both processes
    p1.start()
    p2.start()

    # Run a loop to wait for user input to stop the processes
    while True:
        user_input = input("Press 'q' to quit: ")
        if user_input == 'q':
            stop_event.set()
            break

    # Wait for both processes to finish
    p1.join()
    p2.join()

    print("Both functions completed.")