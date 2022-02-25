import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
import matplotlib as plt
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as pt
import datetime
def plot_water_levels(station, dates, levels):
    x = fetch_measure_levels(station.measure_id, datetime.timedelta(days = dates))
    water_levels = x[1]
    time = x[0]
    upperlimit = [levels[0] for x in range(len(time))]
    lowerlimit = [levels[1] for x in range(len(time))]
    pt.plot(time, water_levels)
    pt.title(station.name)
    pt.xlabel('date')
    pt.ylabel('water level(m)')
    pt.xticks(rotation=45);
    pt.plot(time, lowerlimit)
    pt.plot(time, upperlimit)
    pt.tight_layout()
    pt.show()
    return True

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

