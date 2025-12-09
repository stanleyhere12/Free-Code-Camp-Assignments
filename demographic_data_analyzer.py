import pandas as pd
df = pd.read_csv('C:\\Users\\Guest1\\Desktop\\Scripts\\Free_Code_Camp\\adult.data.csv') #double backshlash to escape the backlash character 
#1. How many people of each race are represented in this dataset
race = df['race'].value_counts()
print(race)

#2 What is the average age of men
Male = df[df['sex'] =='Male']
print(Male['age'].mean())

#3 Percentage of people with a Bachelor's Degree
Bachelors = ((df['education'] == 'Bachelors').sum())
Total = ((df['education']).count().sum())
Portion = (((Bachelors/Total)*100)).round(1)
print(f'{Portion}%')

#4 What is the percentage of people with advanced education who make more than 50k
Bachelors_above = ((df['education'] == 'Bachelors') & (df['salary']  == '>50K')).sum()
Masters_above = ((df['education'] == 'Masters') & (df['salary']  == '>50K')).sum()
Doctorate_above = ((df['education'] == 'Doctorate' )& (df['salary']  == '>50K')).sum()
Bachelors_below = ((df['education'] == 'Bachelors') & (df['salary']  == '<=50K')).sum()
Masters_below = ((df['education'] == 'Masters') & (df['salary']  == '<=50K')).sum()
Doctorate_below = ((df['education'] == 'Doctorate' )& (df['salary']  == '<=50K')).sum()
Above_50k = Bachelors_above + Masters_above + Doctorate_above
Below_50k = Bachelors_below + Masters_below +Doctorate_below
Portion_above = ((Above_50k/(Above_50k+Below_50k))*100).round(1)
print(f'{Portion_above}%')

#5 Percentage of people without advanced education who make more than 50k
advanced_educ_above = ((df['education'] != 'Bachelors')&(df['education'] != 'Masters')&(df['education'] != 'Doctorate')&(df['salary']  == '>50K')).sum()
advanced_educ_below = ((df['education'] != 'Bachelors')&(df['education'] != 'Masters')&(df['education'] != 'Doctorate')&(df['salary']  == '<=50K')).sum()
Portion2 = (((advanced_educ_above)/(advanced_educ_below+advanced_educ_above))*100).round(1)
print(f'{Portion2}%')

#6 Minimum number of hours a person works per week
df['hours-per-week'].min()

#7 Percentage number of people who work minimum hours and make more than 50k
max_salary =((df['hours-per-week'] == 1) & (df['salary'] == '>50K')).sum()
min_salary = ((df['hours-per-week'] == 1) & (df['salary'] == '<=50K')).sum()
Portion4 = ((max_salary/(min_salary+max_salary))*100).round(1)
print(f'{Portion4}%')

#8 country with most people above and the percentage
pd.crosstab(df['native-country'],(df['salary'] == '>50K')).sort_values(by = True,ascending = False)
USA_above = ((df['native-country'] == 'United-States') & (df['salary'] == '>50K')).sum()
USA_below = ((df['native-country'] == 'United-States') & (df['salary'] == '<=50K')).sum()
Portion5 = ((USA_above/(USA_above+USA_below))*100).round(1)
print(f'{Portion5}%')

#9 Most popular occupation for those who earn above 50k in India
India_above50k = df[(df['native-country']=='India') & (df['salary'] == '>50K')]
India_above50k['occupation'].value_counts()
