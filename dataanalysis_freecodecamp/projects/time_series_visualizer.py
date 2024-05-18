import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#importing data
data=pd.read_csv(
    'dataanalysis_freecodecamp/projects/data/fcc-forum-pageviews.csv',
    index_col=0,
    parse_dates=True
)

#cleaning the data
data=data[
    (data['value'] > data['value'].quantile(0.025))&
    (data['value'] < data['value'].quantile(0.975))
]


#lets plot the lineplot between date and page views.
fig,ax=plt.subplots(figsize=(18,6))
ax.plot(data.index,data['value'],color='red')
ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
ax.set_xlabel('Date')
ax.set_ylabel('Page Views')

fig.savefig('dataanalysis_freecodecamp/projects/plots/time_series_visualizer_lineplot.jpg')

#Now lets plot the monthly barplot
#we can use pd.series.dt.year to acess only the year part of the dataframe
df_bar=data.reset_index()
df_bar['Year']=[d.year for d in df_bar.date]
df_bar['Months']=[ d.month for d in df_bar.date]
df_bar.drop(columns=['date'],inplace=True)
df_bar=df_bar.groupby(['Year','Months'],as_index=False).mean()
df_bar=df_bar.pivot(index='Year',columns='Months',values='value')
month_map={
    1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
    7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'           
}

df_bar.columns=df_bar.columns.map(month_map)


fig=df_bar.plot(kind='bar',figsize=(12,9),xlabel="Years",ylabel="Average Page Views")
fig=fig.figure
fig.savefig('dataanalysis_freecodecamp/projects/plots/time_series_visualize_monthlybarplot.jpg')

#Now lets create a Year-wise Box Plot (Trend) and Month-wise Box Plot (Seasonality).
df_box = data.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]
df_box.drop(columns=['date'],inplace=True)

print(df_box.dtypes)
#drawing box plot using seaborn
fig, axes=plt.subplots(nrows=1,ncols=2,figsize=(20,9))

#year wise plot
sns.boxplot(x=df_box['year'],y=df_box['value'],ax=axes[0])
axes[0].set_title('Year-wise Box Plot (Trend)')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Page Views')

# monthly plot
sns.boxplot(data=df_box,x='month',y='value',ax=axes[1],order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
axes[1].set_title('Month-wise Box Plot (Seasonality)')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Page Views')


fig.savefig('dataanalysis_freecodecamp/projects/plots/time_series_visualize_boxplot.jpg')



