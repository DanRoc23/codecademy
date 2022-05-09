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

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []
def updating_records(x):
  for damage in damages:
    if "M" in damage:
      n = float(damage.strip("M")) * conversion["M"]
      updated_damages.append(n)
    elif "B" in damage:
      n = float(damage.strip("B")) * conversion["B"]
      updated_damages.append(n)
    else:
      n = damage
      updated_damages.append(n)
  return updated_damages
# test function by updating damages
updating_records(damages)
#print(updated_damages)

# 2 
# Create a Table
def create_dictionary(names,months,years, max_sustained_winds, areas_affected, deaths):
  hurricanes = dict()
  num_hurricanes = len(names)
  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],"Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i],"Damage": updated_damages[i], "Deaths": deaths[i]}
  return hurricanes

# Create and view the hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths)
#print(hurricanes)

#other way to create a dictionary
def create_dictionary2(names,months,years, max_sustained_winds, areas_affected, deaths):
  hurricanes2 = {}
  for name in names:
    i = names.index(name)
    hurricanes2[name] = {"Name": name,"Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i],"Damage": updated_damages[i], "Deaths": deaths[i]}
  return hurricanes2

hurricanes2 = create_dictionary2(names, months, years, max_sustained_winds, areas_affected, deaths)

#print(hurricanes2)

# 3
# Organizing by Year
def by_year(hurricanes):
  hurricanes_by_year = dict()
  for cane in hurricanes:
    year = hurricanes[cane]["Year"]
    hurricane = hurricanes[cane]
    if year not in hurricanes_by_year:
      hurricanes_by_year[year] = [hurricane]
    else:
      hurricanes_by_year[year].append(hurricane)
  return hurricanes_by_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = by_year(hurricanes)
#print(hurricanes_by_year)

# 4
# Counting Damaged Areas
def counting_areas(counting_areas):
  affected_areas = dict()
  for areas in hurricanes:
    areas = hurricanes[areas]["Areas Affected"]
    for area in areas:
      if area not in affected_areas:
        affected_areas[area] = 1
      else:
        affected_areas[area] += 1
  return affected_areas

# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = counting_areas(hurricanes)
#print(affected_areas_count)

# 5 
# Calculating Maximum Hurricane Count

def most_affected(affected_areas_count):
  max_area = ""
  max_count = 0
  for area in affected_areas_count:
    if affected_areas_count[area] > max_count:
      max_area = area
      max_count += 1
  return max_area, max_count

# find most frequently affected area and the number of hurricanes involved in
most_affected_area = most_affected(affected_areas_count)
#print(most_affected_area)

#6
#Calculating the Deadliest Hurricane
def num_deaths(hurricanes):
  hurricane = ""
  death_count = 0
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] > death_count:
      hurricane = cane
      death_count = hurricanes[cane]["Deaths"]
  return hurricane, death_count

#find highest mortality hurricane and the number of deaths
deadliest_hurricane = num_deaths(hurricanes)
#print(deadliest_hurricane)

# 7
# Rating Hurricanes by Mortality
def mortality_rate(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  hurricanes_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for cane in hurricanes:
    num_of_deaths = hurricanes[cane]["Deaths"]
    if num_of_deaths > mortality_scale[0] and num_of_deaths <= mortality_scale[1]:
      hurricanes_mortality[1].append(hurricanes[cane])
    elif num_of_deaths > mortality_scale[1] and num_of_deaths <= mortality_scale[2]:
      hurricanes_mortality[2].append(hurricanes[cane])
    elif num_of_deaths > mortality_scale[2] and num_of_deaths <= mortality_scale[3]:
      hurricanes_mortality[3].append(hurricanes[cane])
    elif num_of_deaths > mortality_scale[3] and num_of_deaths <= mortality_scale[4]:
      hurricanes_mortality[4].append(hurricanes[cane])
    else:
      hurricanes_mortality[5].append(hurricanes[cane])
  return hurricanes_mortality


# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = mortality_rate(hurricanes)
#print(hurricanes_by_mortality[5])

# 8 Calculating Hurricane Maximum Damage
def maximum_damage(hurricanes):
  max_damage = ""
  max_count_damage = 0
  for cane in hurricanes:
    if hurricanes[cane]["Damage"] == "Damages not recorded":
      pass
    elif hurricanes[cane]["Damage"] > max_count_damage:
      max_damage = cane
      max_count_damage = hurricanes[cane]["Damage"]
  return max_damage, max_count_damage
  
# find highest damage inducing hurricane and its total cost
most_damage_hurricane = maximum_damage(hurricanes)
#print(most_damage_hurricane)

# 9
# Rating Hurricanes by Damage
def damage_rate(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for cane in hurricanes:
    damage = hurricanes[cane]["Damage"]
    if damage == "Damages not recorded":
      pass
    elif damage > damage_scale[0] and damage <= damage_scale[1]:
      hurricanes_damage[1].append(hurricanes[cane])
    elif damage > damage_scale[1] and damage <= damage_scale[2]:
      hurricanes_damage[2].append(hurricanes[cane])
    elif damage > damage_scale[2] and damage <= damage_scale[3]:
      hurricanes_damage[3].append(hurricanes[cane])
    elif damage > damage_scale[3] and damage <= damage_scale[4]:
      hurricanes_damage[4].append(hurricanes[cane])
    else:
      hurricanes_damage[5].append(hurricanes[cane])
  return hurricanes_damage
# categorize hurricanes in new dictionary with damage severity as key

hurricanes_by_damage = damage_rate(hurricanes)
#print(hurricanes_by_damage)
