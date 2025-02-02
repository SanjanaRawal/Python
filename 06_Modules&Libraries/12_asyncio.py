import asyncio
#for performing tasks from 2 or more different functions simultaneously

async def timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time left: {i} seconds") #time left each sec
        await asyncio.sleep(1)
    print("Countdown finished!")

async def task_with_updates():
    print("Task with updates started...")
    await asyncio.sleep(2)
    for i in range(3):
        print(f"Update {i+1}: Task is still running...")
        await asyncio.sleep(1)
    print("Task with updates completed!")

async def main():
    countdown = timer(5)
    updates = task_with_updates()

    await asyncio.gather(countdown, updates) #ensures both task run at same time without blocking each other

asyncio.run(main()) #start the funcs 