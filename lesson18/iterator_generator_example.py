'''numbers = [1,2,3,4,5]
numbers_iterator = iter(numbers)
print(numbers_iterator)
#for number in numbers_iterator:
#    print(number)
print(next(numbers_iterator))
print(next(numbers_iterator))
'''

a = []
def my_gen():
    counter = 0
    while counter <1000:
        counter = counter* counter
        a.append(counter)
        yield counter
        counter +=1


generator = my_gen()
for item in generator:
    print(item)