from json import *
from matrexClass import *

with open('testCase.json', 'r') as f:
    test_cases = load(f)




print('Addition\n')
for item in test_cases['addition_tests']:
    matrex1 = Matrex(item['input_a'], item['cols'], item['rows'])
    matrex2 = Matrex(item['input_b'], item['cols'], item['rows'])
    expected = Matrex(item['expected'], item['cols'], item['rows'])
    if expected.is_equal(matrex1.add(matrex2)):
        print("succsess")
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        break
print(' ')




print('Subtraction\n')
for item in test_cases['subtraction_tests']:
    matrex1 = Matrex(item['input_a'], item['cols'], item['rows'])
    matrex2 = Matrex(item['input_b'], item['cols'], item['rows'])
    expected = Matrex(item['expected'], item['cols'], item['rows'])
    if expected.is_equal(matrex1.subtract(matrex2)):
        print("succsess")
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        break
print(' ')


print('Scalar\n')
for item in test_cases['scalar_tests']:
    matrex1 = Matrex(item['input_a'], item['cols'], item['rows'])
    expected = Matrex(item['expected'], item['cols'], item['rows'])
    if expected.is_equal(matrex1.scalar_multiply(item['scalar'])):
        print('succsess')
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        break