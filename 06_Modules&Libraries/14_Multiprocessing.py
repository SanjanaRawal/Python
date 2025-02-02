import multiprocessing

def square(n):
    result = n * n
    print(f"Square of {n} is {result}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    processes = []

    for i in numbers:
        #new process for each number
        process = multiprocessing.Process(target=square, args=(i,))
        processes.append(process)
        process.start()

    for j in processes:
        j.join()

    print("All tasks completed.")