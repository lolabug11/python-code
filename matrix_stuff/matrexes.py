from json import *
from matrexClass import *

with open('matrix_stuff/testCase.json', 'r') as f:
    test_cases = load(f)




print('Addition\n')
for item in test_cases['addition_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    matrex2 = Matrex(item['input_b'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected'], col=item['cols'], row=item['rows'])
    if expected.is_equal(matrex1.add(matrex2)):
        print("success")
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        
print(' ')




print('Subtraction\n')
for item in test_cases['subtraction_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    matrex2 = Matrex(item['input_b'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected'], col=item['cols'], row=item['rows'])
    if expected.is_equal(matrex1.subtract(matrex2)):
        print("success")
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        
print(' ')


print('Scalar\n')
for item in test_cases['scalar_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected'], col=item['cols'], row=item['rows'])
    if expected.is_equal(matrex1.scalar_multiply(item['scalar'])):
        print('success')
        continue
    else:
        print(f'FAIL: failed on {item['name']}')
        
print('')

print('Transpose\n')
for item in test_cases['transpose_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected'], col=item['expected_cols'], row=item['expected_rows'])
    expected_rows = item['expected_rows']
    expected_cols = item['expected_cols']
    result = matrex1.transpose()
    if expected.is_equal(result) and expected_rows == result.row and expected_cols == result.col:
        print('success')
        continue
    else:
        print(f'FAIL: failed on {item['name']}\nexpected rows = {expected_rows}, result = {result.row}\n expected cols = {expected_cols}, result = {result.col}\nexpected matrex = \n{expected.data}, \nresult matrex = \n{result.data}')
        


print('')
print('Copy\n')
for item in test_cases['copy_tests']:
    matrex1 = Matrex(item['input_a'], col=item['cols'], row=item['rows'])
    expected = Matrex(item['expected_data'], col=item['expected_cols'], row=item['expected_rows'])
    if expected.is_equal(matrex1):
        print('success')
        continue
    else:
        print(f'FAIL\n failed on {item['name']}')
        


print('')
print("Is square\n")
for item in test_cases['square_tests']:
    matrex1 = Matrex(item['input_a'], row=item['rows'], col=item['cols'])
    if matrex1.is_square() == item['expected']:
        print('success')
    else:
        print(f'FAIL\n failed on {item['name']}')
        

print('\nShape\n')
for item in test_cases['shape_tests']:
    matrex1 = Matrex(item['input_a'], item['rows'], item['cols'])
    expected = item['expected']
    if list(matrex1.shape()) == expected:
        print('success')
    else:
        print(f'Fail\nfailed on {item['name']}')
        


print('\nZero matrex\n')
for item in test_cases['zero_matrix_tests']:
    matrex1 = Matrex.zero_matrex(item['rows'],item['cols'])
    expected = Matrex(item['expected_data'], item['rows'], item['cols'])
    if matrex1.is_equal(expected):
        print('success')
    else:
        print(f'FAIL:\nfailed on {item['name']}')


print('\n Multiplication\n')
for item in test_cases['multiplication_tests']:
    matrex1 = Matrex(item['input_a'], item['rows_a'], item['cols_a'])
    matrex2 = Matrex(item['input_b'], item['rows_b'], item['cols_b'])
    expected = Matrex(item['expected'], item['expected_rows'], item['expected_cols'])
    matrex3 = matrex1.multiply(matrex2)
    if matrex3.is_equal(expected):
        print('success')
    else:
        print(f'Fail:\nfailed on {item['name']}')











