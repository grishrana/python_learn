import pandas as pd

 # Read data from file
df = pd.read_csv('projects/data/adult.data.csv')
NO_OF_ROWS, NO_OF_COLUMNS = df.shape
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df['race'].value_counts()

    # What is the average age of men?
mask_male=df['sex']=='Male'
male_count=df[mask_male].shape[0]
sum_age_male=df[mask_male]['age'].sum()
average_age_men = round(sum_age_male/male_count,1)

    # What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round((df[df['education-num']==13].shape[0]/NO_OF_ROWS)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
mask_rich=df['salary']=='>50K'
higher_education = df['education-num'].isin([13,14,16])
lower_education = ~higher_education

    # percentage with salary >50K
higher_education_rich = round((df[(higher_education)&(mask_rich)].shape[0]/df[higher_education].shape[0])*100,1)
lower_education_rich = round((df[(lower_education)&(mask_rich)].shape[0]/df[lower_education].shape[0])*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = df['hours-per-week']==df['hours-per-week'].min()

rich_percentage = round((df[(num_min_workers)&(mask_rich)].shape[0]/df[num_min_workers].shape[0])*100,1)

    # What country has the highest percentage of people that earn >50K?
earnings_of_country=df['native-country'].value_counts()
earnings_of_country=earnings_of_country.to_frame()
earnings_of_country['no_rich']=df[mask_rich]['native-country'].value_counts()
earnings_of_country['perc_of_rich']=(earnings_of_country['no_rich']/earnings_of_country['count'])*100
earnings_of_country.sort_values(by='perc_of_rich',ascending=False,inplace=True)

highest_earning_country =earnings_of_country['perc_of_rich'].idxmax()
highest_earning_country_percentage = round(earnings_of_country['perc_of_rich'].iloc[0],1)

    # Identify the most popular occupation for those who earn >50K in India.
mask_india=df['native-country']=='India'

top_IN_occupation = (df[mask_india]['occupation'].value_counts()).idxmax()


print("Number of each race:\n", race_count) 
print("Average age of men:", average_age_men)
print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
print(f"Min work time: {min_work_hours} hours/week")
print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
print("Country with highest percentage of rich:", highest_earning_country)
print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
print("Top occupations in India:", top_IN_occupation)