import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files = glob.glob('states*.csv')

df_list = [pd.read_csv(filename) for filename in files]
us_census = pd.concat(df_list)

#print(us_census.columns)
#print(us_census.dtypes)
#print(us_census.head())

us_census['Income'] = us_census.Income.str[1:]
us_census.Income = pd.to_numeric(us_census.Income)

genders = us_census.GenderPop.str.split('_')
us_census['Men'] = genders.str.get(0)
us_census['Women'] = genders.str.get(1)

us_census.Men = us_census.Men.str[:-1]
us_census.Women = us_census.Women.str[:-1]
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = pd.to_numeric(us_census.Women)

plt.scatter(us_census.Women, us_census.Income)
plt.show()

us_census = us_census.fillna(value={'Women': us_census.TotalPop - us_census.Men})

#print(us_census[['Women', 'State']])

duplicated = us_census.duplicated(subset=['Income'])
#print(duplicated.value_counts())
us_census = us_census.drop_duplicates(subset=['Income'])
#print(us_census.duplicated(subset=['Income']).value_counts())

plt.scatter(us_census.Women, us_census.Income, color=['blue','green'])
plt.show()
plt.cla()


#print(us_census.head(2))
#print(us_census.columns)

us_census.Hispanic = us_census.Hispanic.str[:-1]
us_census.Hispanic = pd.to_numeric(us_census.Hispanic)
us_census.White = us_census.White.str[:-1]
us_census.White = pd.to_numeric(us_census.White)
us_census.Black = us_census.Black.str[:-1]
us_census.Black = pd.to_numeric(us_census.Black)
us_census.Native = us_census.Native.str[:-1]
us_census.Native = pd.to_numeric(us_census.Native)
us_census.Asian = us_census.Asian.str[:-1]
us_census.Asian = pd.to_numeric(us_census.Asian)
us_census.Pacific = us_census.Pacific.str[:-1]
us_census.Pacific = pd.to_numeric(us_census.Pacific)

us_census = us_census.fillna(value={'Hispanic': us_census.Hispanic.mean(), 'White': us_census.White.mean(), 'White': us_census.White.mean(), 'Black': us_census.Black.mean(), 'Native': us_census.Native.mean(), 'Asian': us_census.Asian.mean(), 'Pacific': us_census.Pacific.mean()})

plt.hist(us_census.Hispanic, color= ['Pink'])
plt.title('Hispanic')
plt.show()
plt.cla()

plt.hist(us_census['White'], color=['Black'])
plt.title('White')
plt.show()
plt.cla()

plt.hist(us_census.Black, color=['Yellow'])
plt.title('Black')
plt.show()
plt.cla()

plt.hist(us_census.Native)
plt.title('Native')
plt.show()
plt.cla()

plt.hist(us_census.Pacific, color=['Brown'])
plt.title('Pacific')
plt.show()
plt.cla()

plt.hist(us_census.Asian, color=['Green'])
plt.title('Asian')
plt.show()
plt.cla()
