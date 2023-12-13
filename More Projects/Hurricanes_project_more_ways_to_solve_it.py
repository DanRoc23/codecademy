# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East Coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

from collections import defaultdict
import operator
# 1
# Update Recorded Damages (function1)
def updating_damages(damages):
  updated_damages = []
  conversion = {"M": 1000000, "B": 1000000000}
  for damage in damages:
    if damage[-1] in conversion:
       x = conversion.get(damage[-1])
       y = float(damage[:-1])
       new_damage = x * y
       updated_damages.append(new_damage)
    else:
      updated_damages.append(damage)
  return updated_damages

# Update Recorded Damages (function1)
def updating_damages2(damages):
  updated_damages2 = []
  for damage in damages:
    if damage == 'Damages not recorded':
      updated_damages2.append(damage)
    if damage.find("M") != -1:
      updated_damages2.append(float(damage[0:damage.find("M")]) * 1000000)
    if damage.find('B') != -1:
      updated_damages2.append(float(damage[0:damage.find("B")]) * 1000000000)
  return updated_damages2


# test function by updating damages
updated_damages = updating_damages(damages)
print(updated_damages)
updated_damages2 = updating_damages2(damages)
print(updated_damages2)

# 2 
# Create a Table
def making_hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  new_dictionary = {}
  for name in range(len(names)):
    new_dictionary[names[name]] = {"Name": names[name], "Month": months[name], "Year": years[name], "Max Sustained Wind": max_sustained_winds[name], "Areas Affected": areas_affected[name], "Damage": updated_damages[name], "Deaths": deaths[name]}
  return new_dictionary

# Create and view the hurricanes dictionary
hurricanes_dict = making_hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes_dict)

# 3
# Organizing by Year
def hurricanes_per_year(hurricanes_dict):
  hurricanes_by_year = {}
  for cane in hurricanes_dict:
    if hurricanes_dict [cane] ["Year"] not in hurricanes_by_year:
      hurricanes_by_year[hurricanes_dict [cane] ["Year"]] = [hurricanes_dict[cane]]
      #it is important to add [] because if i don´t do that, it says that a dict can be append
    else:
      hurricanes_by_year[hurricanes_dict [cane] ["Year"]].append(hurricanes_dict[cane])
  return hurricanes_by_year
  
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = hurricanes_per_year(hurricanes_dict)
print(hurricanes_by_year[1932])

# 4
# Counting Damaged Areas (option1)
def counting_damaged_areas (hurricanes_dict):
  areas_damages_count = {}
  for cane in hurricanes_dict:
    for area in hurricanes_dict [cane]["Areas Affected"]:
      if area not in areas_damages_count:
        areas_damages_count[area] = 1
      else:
        areas_damages_count[area] += 1
  return areas_damages_count

#Counting Daamges Areas (option2)
def counting_damaged_areas2 (hurricanes_dict):
  areas_damages_count = defaultdict(int)
  for cane in hurricanes_dict:
    for area in hurricanes_dict [cane]["Areas Affected"]:
      if area not in areas_damages_count:
        areas_damages_count[area] += 1
  return areas_damages_count

#Counting Daamges Areas (option3)
def counting_damaged_areas3 (hurricanes_dict):
  areas_counted = defaultdict(int)
  for cane in hurricanes_dict:
    for area in hurricanes_dict.get(cane).get('Areas Affected'):
      areas_counted[area] += 1
  return dict(areas_counted.items())

# create dictionary of areas to store the number of hurricanes involved in
areas_affected_count = counting_damaged_areas (hurricanes_dict)
print(areas_affected_count)
areas_affected_count2 = counting_damaged_areas2 (hurricanes_dict)
print(areas_affected_count2)
areas_affected_count3 = counting_damaged_areas3 (hurricanes_dict)
print(areas_affected_count3)

# 5 
# Calculating Maximum Hurricane Count (opción1)
def maximum_hurricane_count(areas_affected_count):
  max_key = max(areas_affected_count, key=areas_affected_count.get)
  max_num = max(areas_affected_count.values())
  return max_key, max_num

# Calculating Maximum Hurricane Count (opción2)
def maximum_hurricane_count2 (areas_affected_counts):
  max_key = max(areas_affected_counts.items(),key=operator.itemgetter(1))
  return max_key

# Calculating Maximum Hurricane Count (opción3)
def maximum_hurricane_count3 (areas_affected_counts):
  max_key = max(areas_affected_counts, key= lambda key: areas_affected_counts[key])
  max_value = max(areas_affected_counts.values())
  return max_key, max_value

# Calculating Maximum Hurricane Count (opción4)
def maximum_hurricane_count4 (areas_affected_counts):
  most_frequently_affected_area4 = [(key, value) for value, key in areas_affected_count.items()]
  x = max(most_frequently_affected_area4)
  w = x[0]
  y = x[-1]
  new_area = (y, w)
  return new_area

# Calculating Maximum Hurricane Count (opción5)
def maximum_hurricane_count5(areas_affected_counts):
  v=list(areas_affected_counts.values()) 
  k=list(areas_affected_counts.keys()) 
  return k[v.index(max(v))], max(v)

# Calculating Maximum Hurricane Count (opción6)
def maximum_hurricane_count6(areas_affected_counts):
  max_area = "Central America"
  max_area_count = 0
  for area in areas_affected_counts:
    if areas_affected_counts[area] > max_area_count:
      max_area = area
      max_area_count = areas_affected_counts[area]   
  return max_area, max_area_count


# find most frequently affected area and the number of hurricanes involved in
most_frequently_affected_area = maximum_hurricane_count(areas_affected_count)
print(most_frequently_affected_area)

most_frequently_affected_area2 = maximum_hurricane_count2(areas_affected_count)
print(most_frequently_affected_area2)

most_frequently_affected_area3 = maximum_hurricane_count3(areas_affected_count)
print(most_frequently_affected_area3)

most_frequently_affected_area4 = maximum_hurricane_count4(areas_affected_count)
print(most_frequently_affected_area4)

most_frequently_affected_area5 = maximum_hurricane_count4(areas_affected_count)
print(most_frequently_affected_area5)

most_frequently_affected_area6 = maximum_hurricane_count6(areas_affected_count)
print(most_frequently_affected_area6)

# 6
# Calculating the Deadliest Hurricane
#print(hurricanes_dict)
def greatest_numbers_of_deaths(hurricanes_dict):
  deaths = defaultdict(int)
  for cane in hurricanes_dict:
      max_death = hurricanes_dict.get(cane).get("Deaths")
      deaths[cane] += max_death
  
  max_key = max(deaths, key=deaths.get)
  max_num = max(deaths.values())
  return max_key, max_num

#opción2
def greatest_numbers_of_deaths2(hurricanes_dict):
  deaths = defaultdict(int)
  for cane in hurricanes_dict:
      max_death = hurricanes_dict.get(cane).get("Deaths")
      deaths[cane] += max_death
  max_key = max(deaths.items(), key=operator.itemgetter(1))
  return max_key

#opción3
def greatest_numbers_of_deaths3(hurricanes_dict):
  deaths = defaultdict(int)
  for cane in hurricanes_dict:
      max_death = hurricanes_dict.get(cane).get("Deaths")
      deaths[cane] += max_death
  max_key = max(deaths, key= lambda key: deaths[key])
  max_value = max(deaths.values())
  return max_key, max_value

#opción4
def greatest_numbers_of_deaths4(hurricanes_dict):
  deaths = defaultdict(int)
  for cane in hurricanes_dict:
      max_death = hurricanes_dict.get(cane).get("Deaths")
      deaths[cane] += max_death
  deadliest_hurricane = [(key, value) for value, key in deaths.items()]
  x = max(deadliest_hurricane)
  w = x[0]
  y = x[-1]
  new_area = (y, w)
  return new_area

#opción5
def greatest_numbers_of_deaths5(hurricanes_dict):
  deaths = defaultdict(int)
  for cane in hurricanes_dict:
      max_death = hurricanes_dict.get(cane).get("Deaths")
      deaths[cane] += max_death
  v=list(deaths.values()) 
  k=list(deaths.keys()) 
  return k[v.index(max(v))], max(v)

#opción6
def greatest_numbers_of_deaths6(hurricanes_dict):
  max_mortality_cane = 'Cuba I'
  max_mortality = 0
  for cane in hurricanes_dict:
    if hurricanes_dict[cane] ["Deaths"] > max_mortality:
      max_mortality_cane = cane
      max_mortality = hurricanes_dict[cane]["Deaths"]
  return max_mortality_cane, max_mortality


# find highest mortality hurricane and the number of deaths
deadliest_hurricane = greatest_numbers_of_deaths(hurricanes_dict)
print(deadliest_hurricane)

deadliest_hurricane2 = greatest_numbers_of_deaths2(hurricanes_dict)
print(deadliest_hurricane2)

deadliest_hurricane3 = greatest_numbers_of_deaths3(hurricanes_dict)
print(deadliest_hurricane3)

deadliest_hurricane4 = greatest_numbers_of_deaths4(hurricanes_dict)
print(deadliest_hurricane4)

deadliest_hurricane5 = greatest_numbers_of_deaths5(hurricanes_dict)
print(deadliest_hurricane5)

deadliest_hurricane6 = greatest_numbers_of_deaths6(hurricanes_dict)
print(deadliest_hurricane6)

# 7
# Rating Hurricanes by Mortality
def mortality_rating(hurricanes_dict):
  mortality_hurricanes = defaultdict(list)
  deaths = defaultdict(int)
  for cane in hurricanes_dict:
      max_death = hurricanes_dict.get(cane).get("Deaths")
      deaths[cane] += max_death
      mortality_dict = list(deaths.items())
  for key, value in mortality_dict:
    if value == 0:
      mortality_hurricanes[0].append(hurricanes_dict[key])
    elif 0 < value <= 100:
      mortality_hurricanes[1].append(hurricanes_dict[key])
    elif 100 < value <= 500:
      mortality_hurricanes[2].append(hurricanes_dict[key])
    elif 500 < value <= 1000:
      mortality_hurricanes[3].append(hurricanes_dict[key])
    elif 1000 < value <= 10000:
      mortality_hurricanes[4].append(hurricanes_dict[key])
    else:
      mortality_hurricanes[5].append(hurricanes_dict[key])
  return dict(sorted(mortality_hurricanes.items()))

# Rating Hurricanes by Mortality (opción2)
def mortality_rating2(hurricanes_dict):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  mortality_hurricanes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for cane in hurricanes_dict:
    num_deaths = hurricanes_dict[cane]["Deaths"]
    if num_deaths == mortality_scale[0]:
      mortality_hurricanes[0].append(hurricanes_dict[cane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      mortality_hurricanes[1].append(hurricanes_dict[cane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      mortality_hurricanes[2].append(hurricanes_dict[cane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      mortality_hurricanes[3].append(hurricanes_dict[cane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      mortality_hurricanes[4].append(hurricanes_dict[cane])
    else:
      mortality_hurricanes[5].append(hurricanes_dict[cane])
  return mortality_hurricanes
# categorize hurricanes in new dictionary with mortality severity as key
mortality_dict = mortality_rating(hurricanes_dict)
print(mortality_dict)

mortality_dict2 = mortality_rating2(hurricanes_dict)
print(mortality_dict2)

# 8 Calculating Hurricane Maximum Damage (opción 1)

def greatest_damage(hurricanes_dict):
  hurricanes_by_damage = defaultdict(int)
  for cane in hurricanes_dict:
    damage_cost = hurricanes_dict [cane] ["Damage"]
    if damage_cost == "Damages not recorded":
      pass
    else:
      hurricanes_by_damage[cane] += damage_cost
  max_key = max(hurricanes_by_damage.items(), key=operator.itemgetter(1))
  return max_key

# 8 Calculating Hurricane Maximum Damage (opción 2)
#print(hurricanes_dict)
def greatest_damage2(hurricanes_dict):
  hurricanes_by_damage = defaultdict(int)
  for cane in hurricanes_dict:
    damage_cost = hurricanes_dict [cane] ["Damage"]
    hurricanes_by_damage[cane] = damage_cost
  max_key = max(hurricanes_by_damage.keys(), key= lambda x: hurricanes_by_damage[x] if not isinstance(hurricanes_by_damage[x], str) else float("-inf"))
  max_value = max(hurricanes_by_damage.values(), key= lambda x: x if not isinstance(x, str) else float("-inf"))
  return max_key, max_value

# 8 Calculating Hurricane Maximum Damage (opción 3)
def greatest_damage3(hurricanes_dict):
  hurricanes_by_damage = defaultdict(int)
  for cane in hurricanes_dict:
    damage_cost = hurricanes_dict [cane] ["Damage"]
    if damage_cost == "Damages not recorded":
      pass
    else:
      hurricanes_by_damage[cane] += damage_cost
  most_damaging_hurricane= [(key, value) for value, key in hurricanes_by_damage.items()]
  x = max(most_damaging_hurricane)
  w = x[0]
  y = x[-1]
  damagest = (y, w)
  return damagest

#8 Calculating Hurricane Maximum Damage (opción 4)
def greatest_damage4(hurricanes_dict):
  hurricanes_by_damage = defaultdict(int)
  for cane in hurricanes_dict:
    damage_cost = hurricanes_dict [cane] ["Damage"]
    if damage_cost == "Damages not recorded":
      pass
    else:
      hurricanes_by_damage[cane] += damage_cost
  v=list(hurricanes_by_damage.values()) 
  k=list(hurricanes_by_damage.keys()) 
  return k[v.index(max(v))], max(v)

#8 Calculating Hurricane Maximum Damage (opción 5)
def greatest_damage5(hurricanes_dict):
  hurricanes_by_damage = defaultdict(int)
  for cane in hurricanes_dict:
    damage_cost = hurricanes_dict.get(cane).get("Damage")
    if damage_cost == "Damages not recorded":
      pass
    else:
      hurricanes_by_damage[cane] += damage_cost
  max_key = max(hurricanes_by_damage, key=hurricanes_by_damage.get)
  max_num = max(hurricanes_by_damage.values())
  return max_key, max_num

#8 Calculating Hurricane Maximum Damage (opción 6)
def greatest_damage6(hurricanes_dict):
  max_damage_cane = 'Cuba I'
  max_damage = 0
  for cane in hurricanes_dict:
    if hurricanes_dict[cane]["Damage"]== "Damages not recorded":
      pass
    elif hurricanes_dict[cane] ["Damage"] > max_damage:
      max_damage_cane = cane
      max_damage = hurricanes_dict[cane] ["Damage"]
  return max_damage_cane, max_damage

# find highest damage inducing hurricane and its total cost
greatest_damage_hurricane = greatest_damage(hurricanes_dict)
print(greatest_damage_hurricane)

greatest_damage_hurricane2 = greatest_damage2(hurricanes_dict)
print(greatest_damage_hurricane2)

greatest_damage_hurricane3 = greatest_damage3(hurricanes_dict)
print(greatest_damage_hurricane3)

greatest_damage_hurricane4 = greatest_damage4(hurricanes_dict)
print(greatest_damage_hurricane4)

greatest_damage_hurricane5 = greatest_damage5(hurricanes_dict)
print(greatest_damage_hurricane5)

greatest_damage_hurricane6 = greatest_damage6(hurricanes_dict)
print(greatest_damage_hurricane6)

# 9
# Rating Hurricanes by Damage(opción 1)
def damage_rating(hurricanes_dict):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  rated_hurricanes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], "Damages not recorded": []}
  for cane in hurricanes_dict:
    damage = hurricanes_dict[cane]["Damage"]
    if damage == "Damages not recorded":
      rated_hurricanes["Damages not recorded"].append(hurricanes_dict[cane])
    elif damage == damage_scale[0]:
      rated_hurricanes[0].append(hurricanes_dict[cane])
    elif damage > damage_scale[0] and damage <= damage_scale[1]:
      rated_hurricanes[1].append(hurricanes_dict[cane])
    elif damage > damage_scale[1] and damage <= damage_scale[2]:
      rated_hurricanes[2].append(hurricanes_dict[cane])
    elif damage > damage_scale[2] and damage <= damage_scale[3]:
      rated_hurricanes[3].append(hurricanes_dict[cane])
    elif damage > damage_scale[3] and damage <= damage_scale[4]:
     rated_hurricanes[4].append(hurricanes_dict[cane])
    else:
      rated_hurricanes[5].append(hurricanes_dict[cane])
  return rated_hurricanes

# Rating Hurricanes by Damage(opción 2)
def damage_rating2(hurricanes_dict):
  damaging_hurricanes = defaultdict(list)
  damages = defaultdict(int)
  for cane in hurricanes_dict:
      max_damage= hurricanes_dict.get(cane).get("Damage")
      if max_damage == "Damages not recorded":
        damaging_hurricanes["Damages not recorded"].append(hurricanes_dict[cane])
      else:
        damages[cane] += max_damage
  damages_dict = list(damages.items())
  for key, value in damages_dict:
    if value == 0:
      damaging_hurricanes[0].append(hurricanes_dict[key])
    elif 0 < value <= 100000000:
      damaging_hurricanes[1].append(hurricanes_dict[key])
    elif 100000000 < value <= 1000000000:
      damaging_hurricanes[2].append(hurricanes_dict[key])
    elif 1000000000< value <= 10000000000:
      damaging_hurricanes[3].append(hurricanes_dict[key])
    elif 10000000000 < value <= 50000000000:
      damaging_hurricanes[4].append(hurricanes_dict[key])
    else:
      damaging_hurricanes[5].append(hurricanes_dict[key])
  return dict(damaging_hurricanes.items())
# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage_severity = damage_rating(hurricanes_dict)
print(hurricanes_by_damage_severity)

hurricanes_by_damage_severity2 = damage_rating2(hurricanes_dict)
print(hurricanes_by_damage_severity2)
