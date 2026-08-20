# %%
import pandas as pd
# %%
dataset_original = pd.read_csv('data/Clean CA Historic Fire Perimeters 1950 to 2025.csv')
dataset = dataset_original.copy()
# %%
# cleaning data section

# cleaning whitespaces
dataset.columns = dataset.columns.str.strip().str.lower().str.replace(' ', '_')
print(dataset.tail(20))
# %%
# dropping important empty columns
dataset = dataset.dropna(subset=['alarm_date', 'containment_date'])
print(dataset.tail(20))
# %%
# Checking to make sure copy worked
print(dataset_original.tail(20))
# %%
# Checking for errors
dataset.info()
# %%
# converting datatimes
# error = coerce means that if there is an error, it will convert to Not a Time
dataset['alarm_date'] = pd.to_datetime(dataset['alarm_date'], errors='coerce')
dataset['containment_date'] = pd.to_datetime(dataset['containment_date'], errors='coerce')
# %%
# renaming year column
dataset = dataset.rename(columns={'year_': 'year'})
print(dataset.head(20))
# %%
# replace NaN in fire_name with "Unnamed fire"
dataset['fire_name'] = dataset['fire_name'].fillna('UNNAMED FIRE')
print(dataset.tail(20))

# %%
# containment is before alarm
invalid_dates = dataset[dataset['containment_date'] < dataset['alarm_date']]
print(f"Invalid containment rows remaining: {len(invalid_dates)}") 

valid_dates_table = dataset['containment_date'] >= dataset['alarm_date']
dataset = dataset[valid_dates_table]

invalid_remaining = dataset[dataset['containment_date'] < dataset['alarm_date']]
print(f"Invalid containment rows remaining: {len(invalid_remaining)}") 

dataset = dataset.reset_index(drop=True)

# %%
# no acres burned
invalid_acres = dataset[dataset['gis_calculated_acres'] <= 0]
print(f"Found {len(invalid_acres)} rows with 0 or negative acres burned.")


# %%
# drop duplicate rows
dataset = dataset.drop_duplicates()

dataset = dataset.reset_index(drop=True)

# %%
# new dataset of the last 25 years
fire_data_2000_2025 = dataset[(dataset['year'] >= 2000) & (dataset['year'] <= 2025)].copy()
fire_data_2000_2025 = fire_data_2000_2025.reset_index(drop=True)
print("Min year:", fire_data_2000_2025['year'].min())
print("Max year:", fire_data_2000_2025['year'].max())
print(fire_data_2000_2025.tail(20))

# %%
print(fire_data_2000_2025.tail(20))
# Save the new clean dataset fire_data_2000_2025
fire_data_2000_2025.to_csv('data/clean_fire_data_2000_to_2025.csv', index=False)
# %%
