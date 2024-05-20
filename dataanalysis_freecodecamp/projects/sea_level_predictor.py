import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

    # Read data from file
data=pd.read_csv('dataanalysis_freecodecamp/projects/data/epa-sea-level.csv',index_col=0)

    # Create scatter plot
fig, axes=plt.subplots(figsize=(12,6))
axes.scatter(data.index,data['CSIRO Adjusted Sea Level'])    

    # Create first line of best fit
calc_beginning = linregress(data.index,data['CSIRO Adjusted Sea Level'])
x_val1=list(data.index)+list(range(2014,2051))
y_val1=[(calc_beginning.slope*x)+calc_beginning.intercept for x in x_val1]
axes.plot(x_val1,y_val1,'r')

    # Create second line of best fit
calc_2000=linregress(data.index[data.index>=2000],data[data.index>=2000]['CSIRO Adjusted Sea Level'])
x_val2=list(data.index[data.index>=2000])+list(range(2014,2051))
y_val2=[(calc_2000.slope*x)+calc_2000.intercept for x in x_val2]
axes.plot(x_val2,y_val2,'g')
    # Add labels and title
axes.set(
        xticks=list(range(1850,2100,25)),title="Rise in Sea Level",
        xlabel="Year",ylabel="Sea Level (inches)"         
)

    
    # Save plot and return data for testing (DO NOT MODIFY)
plt.savefig('/home/daidon/GrishRana/python_learn/dataanalysis_freecodecamp/projects/plots/test_sea_level_plot.png')
