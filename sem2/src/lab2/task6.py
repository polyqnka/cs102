import threading
import time


def print_message(message, delay):
    time.sleep(delay)
    print(f"{message} (задержка {delay} сек.)")


def run_sequential():
    print("Последовательный запуск:")
    start = time.time()

    print_message("Первое сообщение", 2)
    print_message("Второе сообщение", 2)
    print_message("Третье сообщение", 2)

    print(f"Общее время: {time.time() - start:.2f} сек.\n")


def run_with_threads():
    print("Параллельный запуск через потоки:")
    start = time.time()

    threads = []
    messages = ["Первое сообщение", "Второе сообщение", "Третье сообщение"]

    for msg in messages:
        thread = threading.Thread(target=print_message, args=(msg, 2))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Общее время: {time.time() - start:.2f} сек.\n")


if __name__ == "__main__":
    run_sequential()
    run_with_threads()
