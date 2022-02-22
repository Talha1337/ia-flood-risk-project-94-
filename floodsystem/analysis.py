import numpy as np
import matplotlib as plt
from matplotlib import dates
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as pt
def polyfit(dates, levels, p):
    num2datelist = [plt.dates.date2num(date) for date in dates]
    x = np.array(num2datelist - num2datelist[0])
    y = np.array(levels)
    p_coeff = np.polyfit(x , y, p)
    poly = np.poly1d(p_coeff)
    return (poly, num2datelist[0])
def plot_water_level_with_fit(station, dates, levels, p):
    leveldata = fetch_measure_levels(station.measure_id, dates)
    num2datelist = []
    for x in leveldata[0]:
        num2datelist.append(plt.dates.date2num(x))
    x = np.array(num2datelist)
    y = leveldata[1]
    p_coeff = np.polyfit(x - x[0] , y, p)
    poly = np.poly1d(p_coeff)
    pt.plot(x, y)
    upperlimit = [levels[0] for x in range(len(num2datelist))]
    lowerlimit = [levels[1] for x in range(len(num2datelist))]
    pt.plot(x, upperlimit)
    pt.plot(x, lowerlimit)
    x1 = np.linspace(x[0], x[-1], 30)
    pt.plot(x1, poly(x1 - x[0]))
    pt.show()