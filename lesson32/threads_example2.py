import time
import concurrent.futures


def sleepy_func(name):
    print(f"we`re enetring {name} function")
    time.sleep(3)
    print(f"we`re exiting {name} function? hope you`re happy now")

with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
    executor.map(sleepy_func, [1,2,3,4,5,6,7])
