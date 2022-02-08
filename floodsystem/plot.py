import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
import datetime
def plot_water_levels(station, dates, levels):
    x = fetch_measure_levels(station.measure_id, datetime.timedelta(days = dates))
    water_levels = x[1]
    time = x[0]
    upperlimit = [levels[0] for x in range(len(time))]
    lowerlimit = [levels[1] for x in range(len(time))]
    plt.plot(time, water_levels)
    plt.title(station.name)
    plt.xlabel('date')
    plt.ylabel('water level(m)')
    plt.xticks(rotation=45);
    plt.plot(time, lowerlimit)
    plt.plot(time, upperlimit)
    plt.show()
    plt.tight_layout()

