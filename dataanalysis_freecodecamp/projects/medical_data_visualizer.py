import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




#reading the data medical_examination.csv
df=pd.read_csv(
    'dataanalysis_freecodecamp/projects/data/medical_examination.csv',
    index_col=0
)

df=df.rename(columns={'sex':'gender'})
#storing the no_of_columns
NO_OF_ROWS, NO_OF_COLUMNS = df.shape

#calculating bmi and realizing if the paitent is overweight of not 1 if overweight(BMI>25) and 0 if not overweight
BMI=df['weight']/((df['height']/100)**2)
df['overweight']=BMI.apply(lambda x : 1 if x>25 else 0)


#Normalizing the data 0 is always good and 1 is always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol']=df['cholesterol'].apply(lambda x: 0 if x==1 else 1)
df['gluc']=df['gluc'].apply(lambda x: 0 if x==1 else 1)

df_cat=df.melt(id_vars='cardio', value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
df_cat['total']=0

#Counting the values of different variable when Cardio=0/1 and Value 0/1
# value_count(['active','alco','cholesterol','gluc','overweight','smoke'])
variable_list=['cholesterol','gluc','smoke','alco','active','overweight']
for variables in variable_list:
    for cardio in range(2):
        for variable_val in range(2):
            df_cat.loc[((df_cat['cardio']==cardio) & (df_cat['variable']==variables) & (df_cat['value']==variable_val)),"total"]=df_cat[(df_cat['cardio']==cardio) & (df_cat['variable']==variables) & (df_cat['value']==variable_val)].shape[0]


#rremoving duplicate values
df_cat.drop_duplicates(inplace=True)


#Plotting the bar graph of df_cleaned using catplot() and saving it as medical_data_visiualizer_cat.png
fig=sns.catplot(data=df_cat,x='variable',y='total',kind='bar',hue='value',col='cardio')
fig.savefig('dataanalysis_freecodecamp/projects/plots/medical_data_visualizer_cat.png')

#Now let's find out the correlation of different variables with each other and visualize the correlation using heat map.

#dropping values which have higher dialostic Blood pressure than Systolic Blood Pressure
df.drop(list(df[df['ap_lo']>df['ap_hi']].index),inplace=True)

#dropping vlaues which have height less than 2.5 percentile.
df.drop(list(df[df['height']<df['height'].quantile(0.025)].index),inplace=True)

#dropping values which have height more than 97.5 percentile.
df.drop(list(df[df['height']>df['height'].quantile(0.975)].index),inplace=True)

#similar operation as height for weight
df.drop(list(df[df['weight']<df['weight'].quantile(0.025)].index),inplace=True)
df.drop(list(df[df['weight']>df['weight'].quantile(0.975)].index),inplace=True)

df_heat=df.reset_index()

#finding the pearson correlation between the different variables in the df_heat dataframe in 
corr=df_heat.corr()

#using heatmap() to plot the correlation matrix and saving the plot as medical_data_visualizer_heatmap.png in plots folder
mask=corr.where(~(np.triu(np.ones(corr.shape)).astype(bool)))
fig,axe=plt.subplots(figsize=(10,10))
sns.heatmap(data=mask,fmt='.1f',annot=True,ax=axe,linewidths=0.5,vmax=0.3,square=True,center=0,cbar_kws={'shrink':0.5})
fig.savefig('dataanalysis_freecodecamp/projects/plots/medical_data_visualizer_heatmap.png')