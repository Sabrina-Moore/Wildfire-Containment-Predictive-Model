# %%
import pandas as pd
import numpy as np
# makes line charts, scatter plots, histograms
import matplotlib.pyplot as plt
# visualizes charts
import seaborn as sns


# %%
# import dataset
dataset = pd.read_csv('data/clean_fire_data_2000_to_2025.csv')
print(dataset.head(5))
print(dataset.tail(5))

# %%
# are date columns actaully datetime?
dataset.info()
dataset['alarm_date'] = pd.to_datetime(dataset['alarm_date'])
dataset['containment_date'] = pd.to_datetime(dataset['containment_date'])

# %%
# starting visualization 
