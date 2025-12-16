import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy  as np
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick

df = pd.read_csv('C:\\Users\\Guest1\\Desktop\\Scripts\\Free_Code_Camp\\fcc-forum-pageviews.csv',parse_dates=["date"],index_col='date')
Clean_df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= (df['value'].quantile(0.975)))]
fig, axis = plt.subplots(figsize = (16,5))
axis.plot('value',data=Clean_df,color ='red')
axis.set_title(label='Daily freeCodeCamp Forum Page views 5/2026-12/2019',loc='center')
axis.set_xlabel(xlabel= 'Date')
axis.set_ylabel(ylabel= 'Page Views')
plt.show()
plt.savefig('Forum_PageViews.png')
df2 = pd.read_csv('C:\\Users\\Guest1\\Desktop\\Scripts\\Free_Code_Camp\\fcc-forum-pageviews.csv',parse_dates=["date"])
df2 =df2[(df2['value'] >= df2['value'].quantile(0.025)) & (df2['value'] <= (df2['value'].quantile(0.975)))]
def clean_data(df2):
    df2.insert(1, "Year_Month", df2.apply(lambda row : row["date"].strftime("%Y") + "-" + row["date"].strftime("%m"), axis=1))
    df2.insert(1, "Month", df2.apply(lambda row : row["date"].strftime("%B"), axis=1))
    df2.insert(1, "Year", df2.apply(lambda row : row["date"].strftime("%Y"), axis=1))
    df2 = df2.groupby(['Year', 'Month']).agg(value_mean=('value', 'mean')).reset_index()
    return df2

df2_clean = clean_data(df2.copy())
df2_clean['value_mean'] = round(df2_clean['value_mean'],0)
month_order = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]

df2_clean["Month"] = pd.Categorical(df2_clean["Month"], categories=month_order, ordered=True)

pivot_df = df2_clean.pivot(index="Year", columns="Month", values="value_mean").sort_index()

years = pivot_df.index
months = pivot_df.columns

x = np.arange(len(years))
bar_width = 0.06  

plt.figure(figsize=(14, 7))

for i, month in enumerate(months):
    plt.bar(
        x + i * bar_width,
        pivot_df[month],
        width=bar_width,
        label=month
    )

plt.xlabel("Years")
plt.ylabel("Average Page Views")
plt.title("Average Page Views per Month by Year")

plt.xticks(
    x + bar_width * (len(months) / 2),
    years
)

plt.legend(title="Months", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.show()
plt.savefig('Average_Page_Views.png')

def clean_data2(df2):
    df2.insert(1, "Year_Month", df2.apply(lambda row : row["date"].strftime("%Y") + "-" + row["date"].strftime("%m"), axis=1))
    df2.insert(1, "Month", df2.apply(lambda row : row["date"].strftime("%B"), axis=1))
    df2.insert(1, "Year", df2.apply(lambda row : row["date"].strftime("%Y"), axis=1))
    df2 = df2.groupby(['Year', 'Month']).agg(values=('value', 'sum')).reset_index()
    return df2

df3_clean = clean_data2(df2.copy())
df3_clean['values'] = round(df3_clean['values'],0)

df = df2_clean.copy()

df = df.rename(columns={'value_mean': 'Page_Views'})
df['Year'] = df['Year'].astype(str)

month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df['Month'] = pd.Categorical(
    df['Month'].str[:3],
    categories=month_order,
    ordered=True
)

y_min = 0
y_max = df['Page_Views'].max() * 1.1

fig, axes = plt.subplots(
    1, 2,
    figsize=(18, 8),
    gridspec_kw={'width_ratios': [1, 1.2]}
)

sns.boxplot(
    x='Year',
    y='Page_Views',
    data=df,
    hue= 'Year',
    palette='Set2',
    ax=axes[0],
    width=0.6,
    showfliers=True
)

axes[0].set_title('Year-wise Distribution of Monthly Page Views', fontsize=14)
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Monthly Page Views')
axes[0].set_ylim(y_min, y_max)
axes[0].yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
axes[0].grid(axis='y', linestyle='--', alpha=0.6)

sns.boxplot(
    x='Month',
    y='Page_Views',
    data=df,
    hue='Month',
    palette='Set2',
    ax=axes[1],
    width=0.6,
    showfliers=True
)

axes[1].set_title('Month-wise Distribution (Seasonality)', fontsize=14)
axes[1].set_xlabel('Month')
axes[1].set_ylabel('')
axes[1].set_ylim(y_min, y_max)
axes[1].yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
axes[1].grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout(pad=3)
plt.show()
plt.savefig('Box_plots.png')