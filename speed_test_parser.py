import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

import json
import os
PATH_TO_DATA = "C:/Files/Programming/Python/noise-algorithm-tests/test_data/"

def import_data_merged():
    merged_data = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]

    # Loops through files
    for data_file in os.listdir(PATH_TO_DATA):
        data = json.load(open(PATH_TO_DATA + data_file, "r")) # Data of one file

        # Loops through data and appends it to merged_data
        for (func, m_func) in zip(data, merged_data):
            for (time_intveral, m_ti) in zip(func, m_func):
                for test in time_intveral:
                    m_ti.append(test)

    return merged_data

def parse_data(raw_data):
    pln_2D, pln_3D, spx_2D, spx_3D = [[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]
    func_types = [pln_2D, pln_3D, spx_2D, spx_3D]

    for (data, func) in zip(raw_data, func_types):
        for (time_interval, func_ti) in zip(data, func):
            temp = [[], []] # [raw time data, raw exec data]
            for test in time_interval:
                temp[0].append(test[1])
                temp[1].append(test[0])

            # [time mean, exec mean, exec/time mean, standard error]
            func_ti.append(np.mean(temp[0]))  # Mean of time
            func_ti.append(np.mean(temp[1]))  # Mean of exec's
            func_ti.append(func_ti[1] / func_ti[0]) # Mean of exec's over time
            func_ti.append(np.std(temp[0]) / np.sqrt(len(temp[0]))) # Standard error

    return [pln_2D, pln_3D, spx_2D, spx_3D]

# TODO: Fix trendline

if __name__ == '__main__':
    func_types = parse_data(import_data_merged()) # Imports and parses all raw data in PATH_TO_DATA
    colours = ["red", "orange", "blue", "cyan"]
    markers = ["o", "^", "o", "^"]

    fig = plt.figure(1)

    # Function data
    for (func, colour, marker) in zip(func_types, colours, markers):
        graph = plt.gca()
        for func_ti in func:
            graph.loglog(func_ti[0], func_ti[1], color=colour, marker=marker) # Exec's over time
        # graph.set_yscale("log")
        # graph.set_xscale("log")

    # Trendline
    for func in func_types:
        time_data = [func[0][0], func[1][0], func[2][0], func[3][0]]
        exec_data = [func[0][1], func[1][1], func[2][1], func[3][1]]

        z = np.polyfit(time_data, exec_data, 1)
        p = np.polyval(z, time_data)
        print(p)
        plt.loglog(time_data, p)

    # Legend configuration
    legend_elements = [mpl.lines.Line2D([0], [0], marker="o", color="red", label="Perlin 2D", markersize=7, linewidth=0),
                    mpl.lines.Line2D([0], [0], marker="^", color="orange", label="Perlin 3D", markersize=7, linewidth=0),
                    mpl.lines.Line2D([0], [0], marker="o", color="blue", label="Simplex 2D", markersize=7, linewidth=0),
                    mpl.lines.Line2D([0], [0], marker="^", color="cyan", label="Simplex 3D", markersize=7, linewidth=0)]

    plt.legend(handles=legend_elements)

    # Graph configuration
    plt.title("Executions over Time", fontsize="16")
    plt.xlabel("Time (Nanoseconds)", fontsize="13")
    plt.ylabel("Executions", fontsize="13")
    plt.savefig("figure_1.svg")
    plt.grid()
    plt.show()

    # Bargraph (uses data from one second time length)
    fig = plt.figure(2)

    # Times are converted from nanosecond to second
    plt.bar(["Perlin 2D"], [func_types[0][3][2] * 10**9], color ="red", width = 0.4)
    plt.bar(["Perlin 3D"], [func_types[1][3][2] * 10**9], color ="orange", width = 0.4)
    plt.bar(["Simplex 2D"], [func_types[2][3][2] * 10**9], color ="blue", width = 0.4)
    plt.bar(["Simplex 3D"], [func_types[3][3][2] * 10**9], color ="cyan", width = 0.4)

    # Graph configuration
    plt.title("Execution times of Algorithms", fontsize="16")
    plt.ylabel("Executions per Second", fontsize="13")
    plt.savefig("figure_2.svg")
    plt.show()
