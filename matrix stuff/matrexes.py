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
print('')

print('Transpose\n')
for item in test_cases['transpose_tests']:
    matrex1 = Matrex(item['input_a'], item['cols'], item['rows'])
    expected = Matrex(item['expected'], item['expected_cols'], item['expected_rows'])
    expected_rows = item['expected_rows']
    expected_cols = item['expected_cols']
    result = matrex1.transpose()
    if expected.is_equal(result) and expected_rows == result.row and expected_cols == result.col:
        print('succsess')
        continue
    else:
        print(f'FAIL: failed on {item['name']}\nexpected rows = {expected_rows}, result = {result.row}\n expected cols = {expected_cols}, result = {result.col}\nexpected matrex = \n{expected.data}, \nresult matrex = \n{result.data}')
        break