import pandas as pd
from matplotlib import pyplot as plt

marvel=pd.read_csv('desktop/charcters_stats.csv')

marvel.head()

marvel.shape

marvel['Alignment'].value_counts()

marvel[marvel['Alignment']=='good']

good=marvel[marvel['Alignment']=='good']

good.head()

# Method to Sort Values For Specific Columns

good.sort_values(by=['Speed'],ascending=False).head()

good.sort_values(by=['Power'],ascending=False).head()

good_max_power_full=good[good['Power']==100]

good_max_power=good.sort_values(by=['Total'],ascending=False)

good_max_power.head()

plt.figure(figsize=(7,7))
plt.bar(list(good_max_power['Name'])[0:5],list(good_max_power['Total'])[0:5])
plt.show()

bad=marvel[marvel['Alignment']=='bad']

bad.head()

bad.sort_values(by='Speed',ascending=False).head()

bad.sort_values(by='Intelligence',ascending=False).head()

bad.sort_values(by='Total',ascending=False).head()