from json import *
from matrexClass import *

with open('testCase.json', 'r') as f:
    test_cases = load(f)




print('Addition\n')
for item in test_cases['addition_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    matrex2 = Matrex(item['input_b'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected'], col=item['cols'], row=item['rows'])
    if expected.is_equal(matrex1.add(matrex2)):
        print("succsess")
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        break
print(' ')




print('Subtraction\n')
for item in test_cases['subtraction_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    matrex2 = Matrex(item['input_b'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected'], col=item['cols'], row=item['rows'])
    if expected.is_equal(matrex1.subtract(matrex2)):
        print("succsess")
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        break
print(' ')


print('Scalar\n')
for item in test_cases['scalar_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected'], col=item['cols'], row=item['rows'])
    if expected.is_equal(matrex1.scalar_multiply(item['scalar'])):
        print('succsess')
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        break
print('')

print('Transpose\n')
for item in test_cases['transpose_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected'], col=item['expected_cols'], row=item['expected_rows'])
    expected_rows = item['expected_rows']
    expected_cols = item['expected_cols']
    result = matrex1.transpose()
    if expected.is_equal(result) and expected_rows == result.row and expected_cols == result.col:
        print('succsess')
        continue
    else:
        print(f'FAIL: failed on {item['name']}\nexpected rows = {expected_rows}, result = {result.row}\n expected cols = {expected_cols}, result = {result.col}\nexpected matrex = \n{expected.data}, \nresult matrex = \n{result.data}')
        break


print('')
print('Copy\n')
for item in test_cases['copy_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected_data'], col=item['expected_cols'], row=item['expected_rows'])
    if expected.is_equal(matrex1):
        print('succsess')
        continue
    else:
        print(f'FAIL\n failed on {item['name']}')
        break


print('')
print("Is square\n")
for item in test_cases['square_tests']:
    matrex1 = Matrex(item['input_a'], row=item['rows'], col=item['cols'])
    if matrex1.is_square() == item['expected']:
        print('succsess')
    else:
        print(f'FAIL\n failed on {item['name']}')
        break

print('\nShape\n')
for item in test_cases['shape_tests']:
    matrex1 = Matrex(item['input_a'], item['rows'], item['cols'])
    expected = item['expected']
    if list(matrex1.shape()) == expected:
        print('succsess')
    else:
        print(f'Fail\nfailed on {item['name']}')
        break
