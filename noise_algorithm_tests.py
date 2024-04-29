# Lib: https://pypi.org/project/noise/ | Github: https://github.com/caseman/noise/tree/master
import random
import time
from time import perf_counter_ns
from noise import pnoise2, pnoise3, snoise2, snoise3

def export(raw_tr):
    unformated_tr = average(raw_tr)
    test_results = format_tr(unformated_tr)

    filename = "noise_results_" + time.strftime("%H.%M.%S_%d.%m.%Y", time.gmtime()) + ".txt"
    f = open(filename, "w")
    f.write(test_results)
    f.close()

def average(raw_tr):
    tr_averages = []

    # Parses data into num of executions per microsecond
    for func_tests in raw_tr:
        temp_average = [0, 0, 0, 0, 0] # Milli, deci, centi, second, total
        
        # Sums values in all test_batches for each speed and total average
        for test_batch in func_tests:
            temp_average[0] += test_batch[0] # Millisecond test
            temp_average[1] += test_batch[1] # Decisecond test
            temp_average[2] += test_batch[2] # Centisecond test
            temp_average[3] += test_batch[3] # Second test
            temp_average[4] += sum(test_batch) / 4

        # Averages values in temp_average
        for value in range(len(temp_average)):
            temp_average[value] = temp_average[value] / len(func_tests)

        tr_averages.append(temp_average) 

    return tr_averages

def format_tr(test_results):
    output = "Order of averages: Milli, Deci, Centi, Second, Total"

    output += "\nPerlin2D: \n" + ", ".join(str(x) for x in test_results[0])
    output += "\nPerlin3D: \n" + ", ".join(str(x) for x in test_results[1])
    output += "\nSimplex2D: \n" + ", ".join(str(x) for x in test_results[2])
    output += "\nSimplex3D: \n" + ", ".join(str(x) for x in test_results[3])

    return output


# Random permuation arrays with 8193 elements each, used as inputs for noise algorithms, programatically generated
X_COORDS = [i for i in range(8193)]
Y_COORDS = [i for i in range(8193)]
Z_COORDS = [i for i in range(8193)]

# run_time argument is in seconds
def test_speed(func, run_time):
    execs = 0 # Num of excecutions
    
    # Converts run time to nanoseconds because process_time_ns() works with nanoseconds
    run_time = run_time * 10**9

    time_start = perf_counter_ns()
    while perf_counter_ns() < time_start + run_time:
        # The bitwise & operator prevents accessing a number past the array length
        func(X_COORDS[execs & 8192], Y_COORDS[execs & 8192], Z_COORDS[execs & 8192])
        execs += 1
    return (execs / (perf_counter_ns() - time_start)) * 10**3 # Num of excecutions per microsecond

# Noise algorithms
def perlin_2D(x, y, _z): pnoise2(x, y)
def perlin_3D(x, y, z): pnoise3(x, y, z)
def simplex_2D(x, y, _z): snoise2(x, y)
def simplex_3D(x, y, z): snoise3(x, y, z)

functions = [perlin_2D, perlin_3D, simplex_2D, simplex_3D]

if __name__ == '__main__':
    # Procedurally suffles coord const arrays
    random.Random(0).shuffle(X_COORDS)
    random.Random(1).shuffle(Y_COORDS)
    random.Random(2).shuffle(Z_COORDS)

    # Contains run times for all algorithms
    raw_test_results = []

    for f in functions:
        # Contains run times for one algorithm
        test_batch = []

        for n in range(100):
            test = []

            test.append(test_speed(f, 0.001)) # 1 Milisecond
            test.append(test_speed(f, 0.01))  # 1 Centisecond
            test.append(test_speed(f, 0.1))   # 1 Decisecond
            test.append(test_speed(f, 1))     # 1 Second

            test_batch.append(test)
        raw_test_results.append(test_batch)

    export(raw_test_results)
