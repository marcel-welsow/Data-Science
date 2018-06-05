import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/dsm-beuth-edl-demodata-dirty.csv')

# set id NaN values to -1
data['id'] = data['id'].fillna(0)

# correct data types in csv
if data['id'].dtype != int:
   data['id'] = data['id'].astype(int)

# set full name NaN values to empty string
data['full_name'] = data['full_name'].fillna(0)

if data['full_name'].dtype != object:
   data['full_name'].astype(object)

# set first names NaN values to empty string
data['first_name'] = data['first_name'].fillna(0)

if data['first_name'].dtype != object:
   data['first_name'].astype(object)

# set last names NaN values to empty string
data['last_name'] = data['last_name'].fillna(0)

if data['last_name'].dtype != object:
   data['last_name'].astype(object)

# set email NaN values to empty string
data['email'] = data['email'].fillna(0)

if data['email'].dtype != object:
   data['email'].astype(object)

# set gender NaN values to empty string
data['gender'] = data['gender'].fillna(0)

if data['gender'].dtype != object:
   data['gender'].astype(object)

# set age NaN values to empty string
data['age'] = data['age'].fillna(0)
data['age'] = data['age'].replace('old', 0)

if data['age'].dtype != int:
    data['age'] = data['age'].astype(int)

# remove duplicates
data = data.loc[data['first_name'].duplicated() == False]
data = data.drop(data[data.full_name == 0].index)

newindex = 1

for index, row in data.iterrows():
    data.loc[index, 'id'] = newindex
    newindex = newindex+1

    if (row['age'] < 0):
       data.loc[index, 'age'] = 0

data = data.reset_index(drop=True)

print (data)