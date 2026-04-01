def y(x):
    if x <= 996:
        if x == 0:
            return 0
        else:
            return y(x-1) + x
    else:
        return x * (x-1)/2
from time import perf_counter
total_time = 0
x = 100000
for z in range(x):
    start_time = perf_counter()
    y(997)
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    total_time += elapsed_time
    print(z)
average_time = total_time/x
print(average_time)