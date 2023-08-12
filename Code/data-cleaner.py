#!/usr/local/bin/python3

import os
import csv

def read_file(file_path):
    with open(file_path, 'r+', newline='', encoding="ISO-8859-1") as file:
        reader = csv.reader(file)
        data = list(reader)

    return data

def add_median_salary_to_row(data, new_column_name):
    headers = data[0]

    # Add new column to the dataset
    if not new_column_name in headers:
        headers.append(new_column_name)
    
    # Read salary ranges and compute median salary
    salary_column_index = headers.index('Salary2')
    new_column_name_index = headers.index(new_column_name)

    for i, row in enumerate(data):
        if i == 0:
            continue # Skip header row
        row[new_column_name_index] = get_median_salary(row[salary_column_index])

    return data

def add_remote_hybrid(data):
    remote_str = 'Remote'
    hybrid_str = 'Hybrid'

    # Add 'Remote' and 'Hybrid' columns if not already present in the data set
    headers = data[0]
    if not remote_str in headers:
        headers.append(remote_str)
    if not hybrid_str in headers:
        headers.append(hybrid_str)

    title_column_index = headers.index('Title')
    remote_column_index = headers.index(remote_str)
    hybrid_column_index = headers.index(hybrid_str)

    for i, row in enumerate(data):
        if i == 0:
            continue
        else:
            # Information on whether role is remote/hybrid is in title string
            title = row[title_column_index]
            
            # check if title contains 'Remote' word
            if remote_str.lower() in title.lower():
        
               row.insert(remote_column_index, 'Yes')
            else:
               row.insert(remote_column_index, 'No')

            # Check if title contains 'Hybrid' word
            if hybrid_str.lower() in title.lower():
               row.insert(hybrid_column_index, 'Yes')
            else:
               row.insert(hybrid_column_index, 'No')
            
    return data

def get_median_salary(salary_string):
    if 'K' in salary_string:  # Salary represented as a range in thousands
        # Remove non-digit and non-decimal characters and non-hyphens
        salary_string = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '-', salary_string))
        
        # Split the string by the delimiter "-"
        salary_range = salary_string.split('-')
        
        # Extract the lower and upper bounds of the salary range
        if len(salary_range) == 2:
            lower_bound = float(salary_range[0]) * 1000
            upper_bound = float(salary_range[1]) * 1000
            return (lower_bound + upper_bound)/2

        elif len(salary_range) == 1:
            # Case where there's only a single salary value and not a range
            return float(salary_range[0]) * 1000

        
    elif 'Per Hour' in salary_string:  # Salary represented as an hourly rate
        # Remove non-digit and non-decimal characters
        salary_string = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '-', salary_string))        
        # Split the string by the delimiter "-"
        salary_range = salary_string.split('-')
        
        # Extract the lower and upper bounds of the hourly rate
        if len(salary_range) == 2:
            lower_bound = float(salary_range[0].rstrip('.'))*40*52
            upper_bound = float(salary_range[1].rstrip('.'))*40*52

            return (lower_bound + upper_bound)/2
        elif len(salary_range) == 1:
            # Case where there's only a single salary value and not a range
            return float(salary_range[0].rstrip('.'))*40*52

    return 0

def remove_empty_salaries(data):
    headers = data[0]
    salary_column_index = headers.index('Salary2')
    filtered_rows = []
    
    for row in data:
        if row[salary_column_index] != '':
            filtered_rows.append(row)

    return filtered_rows


def get_indeed_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'INDEED-listing-1-JUL.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

def get_glass_door_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'V2_GlassdoorCyber security Jobs in Washington, DC, July 2023.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

def remove_bom(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
        content = file.read()

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        file.write(content)
    

file_path = get_glass_door_file_path()
remove_bom(file_path)

contents = read_file(file_path)
filtered_rows = remove_empty_salaries(contents)

rows_with_median_annual_pay = add_median_salary_to_row(filtered_rows, "Median annual salary")
rows_with_hybrid_remote = add_remote_hybrid(rows_with_median_annual_pay)



with open(file_path, 'w', newline='', encoding="ISO-8859-1") as file:
    writer = csv.writer(file)
    writer.writerows(rows_with_hybrid_remote)

