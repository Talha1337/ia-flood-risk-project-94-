from floodsystem.utils import sorted_by_key
def stations_level_over_threshold(stations, tol):
    list_of_over_threshold = []
    for station in stations:
        name_and_relative_water = []
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
            name_and_relative_water.append(station.name)
            name_and_relative_water.append(station.relative_water_level())
            list_of_over_threshold.append(tuple(name_and_relative_water))
    return list_of_over_threshold
def stations_highest_rel_level(stations, N):
    station_list = stations_level_over_threshold(stations, -50)
    station_leaderboard = sorted_by_key(station_list, 1, reverse=True)
    small_station_list = station_leaderboard[0:N]
    return small_station_list
def stations_level_over_threshold_noname(stations, tol):
    list_of_over_threshold = []
    for station in stations:
        name_and_relative_water = []
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
            name_and_relative_water.append(station)
            name_and_relative_water.append(station.relative_water_level())
            list_of_over_threshold.append(tuple(name_and_relative_water))
    return list_of_over_threshold
def stations_highest_rel_level_noname(stations, N):
    station_list = stations_level_over_threshold_noname(stations, -50)
    station_leaderboard = sorted_by_key(station_list, 1, reverse=True)
    small_station_list = station_leaderboard[0:N]
    return small_station_list