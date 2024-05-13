# Lib: https://pypi.org/project/noise/ | Github: https://github.com/caseman/noise/tree/master
import random
import time
from time import perf_counter_ns
from noise import pnoise2, pnoise3, snoise2, snoise3
import json

def export(raw_tr):
    filename = "noise_results_" + time.strftime("%Y.%m.%d_%H.%M.%S", time.gmtime()) + ".txt"
    f = open(filename, "w")
    f.write(json.dumps(raw_tr))
    f.close()


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
    return [execs, perf_counter_ns() - time_start] # Num of excecutions per microsecond

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

            test.append(test_speed(f, 0.001)) # 1 Millisecond
            test.append(test_speed(f, 0.01))  # 1 Centisecond
            test.append(test_speed(f, 0.1))   # 1 Decisecond
            test.append(test_speed(f, 1))     # 1 Second

            test_batch.append(test)
        raw_test_results.append(test_batch)

    export(raw_test_results)