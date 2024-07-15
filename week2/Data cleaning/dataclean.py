import numpy as np
import pandas as pd
import csv

files = ["playstore_apps.csv", "playstore_reviews.csv"]

for i in files:
    data = pd.read_csv(i)
    #1
    cleaned_data = data.drop_duplicates()
    #2
    cleaned_data = cleaned_data.dropna()
    cleaned_data_array = cleaned_data.to_numpy()
    # Save cleaned DataFrame to a new CSV file with UTF-8 encoding
    cleaned_data.to_csv(i, index=False, encoding='utf-8')

df = pd.read_csv('playstore_apps.csv')

# Replace 'W' in 'Android Ver' column with an empty string
df['Android Ver'] = df['Android Ver'].str.replace('W', '')

# Save the updated DataFrame back to a CSV file
df.to_csv('playstore_apps.csv', index=False)
