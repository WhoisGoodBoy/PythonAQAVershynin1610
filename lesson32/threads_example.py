import time
import concurrent.futures


def sleepy_func(name):
    print(f"we`re enetring {name} function")
    time.sleep(3)
    print(f"we`re exiting {name} function? hope you`re happy now")

with concurrent.futures.ThreadPoolExecutor(max_workers=700000) as executor:
    executor.map(sleepy_func, range(700000))
