from collections import OrderedDict
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#update damages to decimal form :
def update_damages(lst):
    updated_lst = []
    for damage in lst:
        if damage[-1] == "M":
            updated_lst.append(float(damage[:-1]) * pow(10,6))
        elif damage[-1] == "B":
            updated_lst.append(float(damage[:-1]) * pow(10,9))
        else:
            updated_lst.append(damage)
    return updated_lst

damages_updated = update_damages(damages)

# create hurricane dictionary:
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = OrderedDict()
    values = {'Name': 1, 'Month': 2, 'Year': 3, 'Max Sustained Wind': 4, 'Areas Affected': 5, 'Damage': 6, 'Deaths': 7}
    for x in range(len(names)):
        hurricanes[names[x]] = {"Name": names[x],
                                "Month": months[x],
                                "Year": years[x],
                                "Max Sustained Wind": max_sustained_winds[x],
                                "Areas Affected": areas_affected[x],
                                "Damage": damages[x],
                                "Deaths": deaths[x]}
    return hurricanes

new_dict = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)

# hurricanes sorted by year:
def hurricane_per_year(dict, years):
    hurricanes_year = {}
    for year in years:
        hurricanes_year[year] = []

    for name,values in dict.items():
        if dict[name]["Year"] in hurricanes_year:
            hurricanes_year[dict[name]["Year"]].append(dict[name])
    return hurricanes_year

hurricanes_by_year = hurricane_per_year(new_dict, years)

# number of times affected areas:
def num_times_affected(new_dict):
    areas_affected = {}
    string = ""
    for name in new_dict:
        for area in new_dict[name]["Areas Affected"]:
            string += area + ","
            areas_affected[area] = string.count(area)
    return areas_affected


areas_affected = num_times_affected(new_dict)

# most affected area
def most_affected_area(areas_affected):
    max_time_affected = sorted(areas_affected.values())
    most_affected_areas = ""
    for area in areas_affected.items():
        if area[1] == max_time_affected[-1]:
            most_affected_areas += area[0] + ","
    return "The most hurricane-affected area(s) are: {} which have been affected by a hurricane {} times.".format(str(most_affected_areas), max_time_affected[-1])

most_affected_area = most_affected_area(areas_affected)

# most deaths in hurricane:
def most_deaths(dict):
    most_deaths = 0
    name_country = ""
    for name in dict:
        if dict[name]["Deaths"] > most_deaths:
            most_deaths = dict[name]["Deaths"]
            name_country = dict[name]["Name"]
    return "The deadliest hurricane happened in {} and killed {} people.".format(name_country, most_deaths)

most_deaths = most_deaths(new_dict)

# hurricanes sorted by mortality scale:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def hurricanes_by_rating(mortality_scale):
    hurricanes_by_rating = {}
    for rating in range(6):
        hurricanes_by_rating[rating] = []
    for name in new_dict:
        if new_dict[name]["Deaths"] == 0:
            hurricanes_by_rating[0].append(new_dict[name])
        elif new_dict[name]["Deaths"] <= 100:
            hurricanes_by_rating[1].append(new_dict[name])
        elif new_dict[name]["Deaths"] <= 500:
            hurricanes_by_rating[2].append(new_dict[name])
        elif new_dict[name]["Deaths"] <= 1000:
            hurricanes_by_rating[3].append(new_dict[name])
        elif new_dict[name]["Deaths"] <= 10000:
            hurricanes_by_rating[4].append(new_dict[name])
        else:
            hurricanes_by_rating[5].append(new_dict[name])
    return hurricanes_by_rating

hurricanes_by_rating = hurricanes_by_rating(mortality_scale)

# hurricane that caused the most damage:
def greatest_damage(dict):
    greatest_damage = 0
    greatest_damage_country = ""
    for name in dict:
        if dict[name]["Damage"] == "Damages not recorded":
            continue
        if dict[name]["Damage"] > greatest_damage:
            greatest_damage = dict[name]["Damage"]
            greatest_damage_country = dict[name]["Name"]
    return "{} suffered {} dollars of damage-The largest amount of any hurricane.".format(greatest_damage_country, greatest_damage)

most_damage = greatest_damage(new_dict)

# hurricanes sorted by damage scale:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def sort_by_damage(damage_scale, new_dict):
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for name in new_dict:
        if new_dict[name]["Damage"] == 0:
            hurricanes_by_damage[0].append(new_dict[name])
        elif new_dict[name]["Damage"] <= 100000000:
            hurricanes_by_damage[1].append(new_dict[name])
        elif new_dict[name]["Damage"] <= 1000000000:
            hurricanes_by_damage[2].append(new_dict[name])
        elif new_dict[name]["Damage"] <= 10000000000:
            hurricanes_by_damage[3].append(new_dict[name])
        elif new_dict[name]["Damage"] <= 50000000000:
            hurricanes_by_damage[4].append(new_dict[name])
        else:
            hurricanes_by_damage[5].append(new_dict[name])
    return hurricanes_by_damage

hurricanes_sorted_by_damage = sort_by_damage(damage_scale, new_dict)
