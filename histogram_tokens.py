
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import sys
import math
from matplotlib.ticker import FormatStrFormatter



def main():
    print(len(sys.argv))
    if len(sys.argv) < 2:
        exit("Please include filename.")
        
    filename = sys.argv[1]
    values = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.split(" ")
            values.append(parts[1])

    # print(values)
    # %matplotlib inline
    
    values = [value.split("\n")[0] for value in values]
    n = len(values)
    my_range = int(values[0]) - int(values[-1])
    num_intervals = math.ceil(math.sqrt(n))
    width_intervals = math.floor(my_range / num_intervals)
    data = np.array(values)
    my_bins = []
    for x in range(0, num_intervals):
        my_val = width_intervals * x
        my_bins.append(int(my_val))
    print(my_bins)
    
    width = 10
    fig, ax = plt.subplots()
    # counts, bins, patches = ax.hist(data, facecolor="blue", edgecolor="black")
    # plt.style.use('ggplot')
   
    # ax.set_xticks(bins)
    # ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
    # plt.legend()
    ax.hist(data, bins=np.arange(int(data[-1]), int(data[0]) + width, width), align="left", range=[0, 50], edgecolor="black")
    # bin_labels= ['{0:.2f}'.format(b) for b in my_bins]
    plt.xticks(my_bins[::10])
    # plt.tick_params(
    #     axis="x",
    #     which="minor",
    #     bottom=False,
    #     top=False,
    #     labelbottom=False
    # )
    plt.yticks(np.arange(0, 8000, 2000))
    
    
    plt.show()
    
    
    
if __name__ == "__main__":
    main()