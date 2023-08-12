#!/usr/local/bin/python3

import os
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_file(file_path, custom_encoding):
    with open(file_path, 'r+', newline='', encoding=custom_encoding) as file:
        reader = csv.reader(file)
        data = list(reader)

    return data 

def get_input_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'Cyber_Data_new.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

df = pd.read_csv(get_input_file_path(), encoding='mac_roman')
selected_features = ['Salary_med', 'Weekly_commute', 'Person_crime', 'Prop_crime', 'Experience_level', 'Candidate']
df_selected = df[selected_features]

correlation_matrix = df_selected.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
