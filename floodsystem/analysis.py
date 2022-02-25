import numpy as np
import matplotlib as plt
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as pt
import datetime
def polyfit(dates, levels, p):
    x_raw = plt.dates.date2num(dates) #convert dates to numbers, creates list of numbers from list of datetime objects
    x = np.array(x_raw - x_raw[0]) #Creates array for x values, x[0] = 0, starts from there and continues.
    y = np.array(levels) #creates array for y values that are associated to the x values.
    p_coeff = np.polyfit(x, y, p) #Creates least squares polynomial fit for the x and y values, with order p polynomial.
    poly = np.poly1d(p_coeff) #forms a poly1d object from the list of coefficients provided from the p_coeff variable.
    return (poly, x_raw[0]) #returns the poly1d object and the amount by which the dates axis was shifted. 

def plot_water_level_with_fit(station, dates, levels, p):
    leveldata = fetch_measure_levels(station.measure_id, datetime.timedelta(days = dates)) #fetches measure levels over the past two days for a station.
    num2datelist = [] #initialise empty list for number to date.
    for x in leveldata[0]:
        num2datelist.append(plt.dates.date2num(x)) #for each date from leveldata output, append the number conversion into this list (creates x coords)
    x = np.array(num2datelist - num2datelist[-1]) #x coords creates from the lsit of dates.
    y = leveldata[1] #y coords creates from list of levels from the stations.
    p_coeff = np.polyfit(x, y, p) # least squares polynomial fit from x - x[0] and y, degree p.
    poly = np.poly1d(p_coeff) #converted to poly1d object.
    pt.plot(x, y) #plot x against y.
    upperlimit = [levels[1] for x in range(len(num2datelist))] #form x coordinates constant line for upper end of typical range.
    lowerlimit = [levels[0] for x in range(len(num2datelist))] #form y coordinates constant line for upper end of typical range.
    pt.plot(x, upperlimit) #plot upper line
    pt.plot(x, lowerlimit) #plot lower line
    x1 = np.linspace(x[0], x[-1], 30) #form uniform range of x values which can be applied to the poly1d object.
    pt.plot(x1, poly(x1)) # plot polynomial.
    pt.show() #show overall plot. 
    return True