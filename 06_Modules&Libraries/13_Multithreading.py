import threading
import time

def task(name, delay):
    print(f"Task {name} started")
    time.sleep(delay)  # Some task with a delay
    print(f"Task {name} finished after {delay} seconds")

#creating new threads that will run task function with arguments as mentioned
thread1 = threading.Thread(target=task, args=("A", 2))
thread2 = threading.Thread(target=task, args=("B", 3))
thread3 = threading.Thread(target=task, args=("C", 1))

#to start the execution of threads
thread1.start()
thread2.start()
thread3.start()

#to ensure that the main program waits for each thread to finish
thread1.join()
thread2.join()
thread3.join()

print("All tasks completed.")