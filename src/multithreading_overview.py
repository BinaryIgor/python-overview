import time
import threading
import concurrent.futures


# because of the GIL, Python programs are always run on a single core!

def some_function():
    print(f"About to sleep in a thread...{threading.current_thread().name}")
    time.sleep(1)
    print("Wake up!")
    return time.time()


thread = threading.Thread(target=some_function)
thread.start()
# wait for thread end
thread.join()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = []
    for i in range(10):
        r = executor.submit(some_function)
        results.append(r)


results = [r.result() for r in results]

print(f"Results: {results}")
