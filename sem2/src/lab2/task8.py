import threading

lock = threading.Lock()

def increment(shared):
    for _ in range(100000):
        with lock:
            shared["counter"] += 1

def run_threads():
    shared = {"counter": 0}
    threads = [threading.Thread(target=increment, args=(shared,)) for _ in range(10)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return shared["counter"]

if __name__ == "__main__":
    result = run_threads()
    print(f"Результат: {result}")
