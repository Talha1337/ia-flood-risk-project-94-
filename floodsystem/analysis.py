import numpy as np
import matplotlib as plt
from floodsystem.datafetcher import fetch_measure_levels
def polyfit(dates, levels, p):
    x = [plt.dates.date2num(dates)]
    p_coeff = np.polyfit((x - x[0]) , levels, p)
    poly = np.poly1d(p_coeff)
    plt.plot(x, levels)
    x1 = np.linspace(x[0], x[-1], 10)
    plt.plot(x1, poly(x1 - x[0]))
    plt.show()
def plot_water_level_with_fit(station, dates, levels, p):
    fetch_measure_levels(station, )
    x = [plt.dates.date2num(dates)]
    p_coeff = np.polyfit((x - x[0]) , levels, p)
    poly = np.poly1d(p_coeff)
    plt.plot(x, levels)
    x1 = np.linspace(x[0], x[-1], 10)
    plt.plot(x1, poly(x1 - x[0]))
    plt.show()