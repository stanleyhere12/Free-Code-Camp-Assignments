import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sum

df = pd.read_csv('C:\\Users\\Guest1\\Desktop\\Scripts\\Free_Code_Camp\\epa-sea-level.csv')
result = sum.linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
x = np.arange(df['Year'].min(), 2051)
y = (result.slope * x)+ result.intercept
fig, axis = plt.subplots()
axis.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
axis.plot(x,y,color = 'red')
axis.set_xlabel('Year',loc='center')
axis.set_ylabel('Sea Level (inches)')
plt.show()
plt.savefig('Sea_Level_plot1.png')

new_df = df[df['Year'] >= 2000]
result2 = sum.linregress(new_df['Year'],new_df['CSIRO Adjusted Sea Level'])
x = np.arange(new_df['Year'].min(),2051)
y = (result2.slope*x) + result2.intercept
fig, axis = plt.subplots()
axis.scatter(new_df['Year'],new_df['CSIRO Adjusted Sea Level'])
axis.plot(x,y,color = 'red')
axis.set_xlabel('Year',loc='center')
axis.set_ylabel('Sea Level (inches)')
plt.show()
plt.savefig('Sea_Level_plot2.png')