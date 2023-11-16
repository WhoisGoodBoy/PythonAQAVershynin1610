import math
import random
from functools import reduce
'''def func_name():
    pass

#lambda arg_1, arg_2,...arg_n:expression

double = lambda x:x*2

print(double(5))
print(double(10))
print(double(15))

def func_double(x):
    return x*2

def to_cube(x):
    return x*x*x

lambda_to_cube = lambda x:x*x*x

print(lambda_to_cube(3))
print(to_cube(3))


lambda_multiple_three_numbers = lambda a,b,c:a*b*c

print(lambda_multiple_three_numbers(2,3,5))

lambda_with_no_args = lambda:15/3
print(lambda_with_no_args())

sqrt_x = lambda x:math.sqrt(x)

lambda_list = [
    lambda x:x*2,
    lambda x:x*3,
    lambda x:x*4
]
for el in lambda_list:
    print(el(5))

lambda_tuple = (
    lambda x:x*2,
    lambda x:x*3,
    lambda x:x*4
)

for el in lambda_tuple:
    print(el('qwerty'))


areas_dict = {
    'circle':lambda r: math.pi*r*r,
    'rectangle':lambda a,b:a*b,
    'square':lambda a:a*a
}

print(areas_dict['circle'](20))
print(areas_dict['rectangle'](3,6))
print(areas_dict['square'](100))
'''
#filter

list_a = [1,2,3,4,5,6,7,8,9,10]

filtered_list = list(filter(lambda x: x%2==0, list_a))
print(filtered_list)
filtered_list_nonpair = list(filter(lambda x: x%2!=0, list_a))
print(filtered_list_nonpair)

#map
double_list = list(map(lambda x:x*2, list_a))
double_list_2 = []
for element in list_a:
    double_list_2.append(element*2)
print(double_list)
print(double_list_2)
a = tuple(map(lambda x:x*2, list_a))

summ = reduce(lambda x,y:x+y, list_a)
print(summ)
list_b = [90,50,40,20,30]
min_el = reduce(lambda x,y:x if(x<y) else y, list_b)
print(min_el)


