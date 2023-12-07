import subprocess
import concurrent.futures
import datetime
'''

print(datetime.datetime.now())
result = subprocess.run(['python', 'threads_example.py'], shell=True, capture_output=True, text=True)
print(result.stdout)

result2 = subprocess.run(['python', 'threads_example2.py'], shell=True, capture_output=True, text=True)
print(result2.stdout)
print(datetime.datetime.now())
'''

def threads_subprocess(name):
    print(f'were usiing{name} file rn')
    result = subprocess.run(['python', name], shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(f'were fifnished with{name} file rn')


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(threads_subprocess, ['threads_example.py', 'threads_example2.py'])
