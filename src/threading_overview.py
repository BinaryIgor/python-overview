import time
import threading
import concurrent.futures


# because of the GIL, Python programs always run on a single core!
def some_function():
    print(f"About to sleep in a thread...{threading.current_thread().name}")
    time.sleep(1)
    print("Wake up!")
    return time.time()


thread = threading.Thread(target=some_function)
thread.start()
# wait for thread end
thread.join()

print("Thread finished, let's start the executor..")
print()

executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

futures = []
for i in range(10):
    r = executor.submit(some_function)
    futures.append(r)


results = [r.result() for r in futures]

print(f"Results: {results}")
