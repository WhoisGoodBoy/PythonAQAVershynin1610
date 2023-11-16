from argparse import ArgumentParser



parser = ArgumentParser()
parser.add_argument('--a', help='first argument', default=5)
parser.add_argument('--b', help='second argument', default=10)

arguments = parser.parse_args()
arguments_adequate = {key: float(value) for key, value in arguments.__dict__.items()}
print(f'{arguments_adequate["a"]} + {arguments_adequate["b"]} = {arguments_adequate["a"] + arguments_adequate["b"]}')
'''
cd to directory with file, like cd lesson26
python argparse_example.py --a=80 --b=70
python argparse_example.py
python argparse_example.py --help

'''
