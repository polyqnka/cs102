import threading
import time

def print_with_delay():
    time.sleep(2)
    print("Это строка, выведенная с задержкой.")

def run_thread():
    thread = threading.Thread(target=print_with_delay)
    thread.start()
    thread.join()  # Ждем завершения потока
    print("Поток завершен.")
