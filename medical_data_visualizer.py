#import data and assign it df
import pandas as pd
df = pd.read_csv('C:\\Users\\Guest1\\Desktop\\Scripts\\Free_Code_Camp\\medical_examination.csv')
df.head(5)

#Create overweight column 
df['BMI'] = df['weight']/((df['height']/100)**2)
df['Overweight'] = (df['BMI'] >25).astype(int)
df['Overweight']

#Normalize data
#Derived cholestorel
from decimal import Decimal
def derivedCol(cholesterol):
    if cholesterol > 1:
        number1 = 1
    else:
        number1 = 0
    return f"{number1:01.0f}"

df.insert(8, "Cholesterol", df.apply(lambda row : derivedCol(row["cholesterol"]), axis=1))

#Derived  glucose
def derivedCol_1(gluc):
    if gluc > 1:
        number1 = 1
    else:
        number1 = 0
    return f"{number1:01.0f}"

df.insert(10, "Glucose", df.apply(lambda row : derivedCol_1(row["gluc"]), axis=1))

#creating dataframe for catplot using pd.melt
df_cat = pd.melt(df, id_vars=['cardio'],value_vars = ['Cholesterol', 'Glucose', 'smoke', 'alco', 'active', 'Overweight'])
print(df_cat)

#categorical plot
import matplotlib.pyplot as plt
import seaborn as sns
df_cat['value'] = df_cat['value'].astype(str)
df_cat['cardio'] = df_cat['cardio'].astype(str)
sns.catplot(
    data = df_cat, kind = 'count',
    x= 'variable', 
    col='cardio',
    hue='value',
    errorbar=None,
    height=6,
    aspect=1.5,
)
plt.show()

#Filter data to the specified conditions
filter1_df = df[(df['ap_lo'] <= df['ap_hi'])]
Filter2_df = filter1_df[filter1_df['height'] >= (filter1_df['height'].quantile(0.025))]
Filter3_df = Filter2_df[Filter2_df['height']<=Filter2_df['height'].quantile(0.975)]
Filter4_df = Filter3_df[Filter3_df['weight']>=Filter3_df['weight'].quantile(0.025)]
Heat_df = Filter4_df[Filter4_df['weight'] <= Filter4_df['weight'].quantile(0.975)]
print(Heat_df)

#creating correlation matrix
corr = Heat_df.corr()
print(corr)

#creating correlation plot 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
mask = np.triu(corr)
plt.figure(figsize=(10, 8))
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt=".1f",
    linewidths=.5,
    cbar_kws={'shrink': 0.75}
)
plt.title('Correlation Matrix Heatmap', fontsize=16)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
