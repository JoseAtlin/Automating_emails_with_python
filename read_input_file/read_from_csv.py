import pandas as pd


data = pd.read_csv('MOCK_DATA.csv')
names = data['first_name']
college_name = data['company_name']
sem_year = data['year']

for row in range(len(names)):
    name, college, year = names[row], college_name[row], sem_year[row]
    print(name, college, year)
