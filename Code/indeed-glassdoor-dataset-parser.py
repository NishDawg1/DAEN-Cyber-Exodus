#!/usr/local/bin/python3

import os
import csv
import re

def read_file(file_path, custom_encoding):
    with open(file_path, 'r+', newline='', encoding=custom_encoding) as file:
        reader = csv.reader(file)
        data = list(reader)

    return data 

def extract_relevant_information_glassdoor(data):
    headers = data[0]
    title_column_index = headers.index('Title')
    location_column_index = headers.index('Location1')
    salary_column_index = headers.index('Salary2')

    output_rows = []
    header_row = ['Title', 'Location', 'Salary', 'Is Remote', 'Is Hybrid', 'Source']
    output_rows.append(header_row)

    for i, row in enumerate(data):
        if i == 0:
            continue
        else:
            title_val = row[title_column_index]
            location = get_location(row[location_column_index])

            if not is_dmv(location):
                continue

            is_remote = get_remote(row[title_column_index])
            is_hybrid = get_hybrid(row[title_column_index])
            salary = get_salary_glassdoor(row[salary_column_index])

            if len(salary) == 0:
                continue
            
            new_row = [title_val, location, salary, is_remote, is_hybrid, 'glassdoor']
            output_rows.append(new_row)
    
    return output_rows

def is_dmv(location):
    if len(location) == 0:
        return True
    
    parts = location.split(",")
    if len(parts) == 2:
        state = parts[1].strip()
        if state == 'DC' or state == 'MD' or state == 'VA':
            return True
    
    return False

def extract_relevant_information_indeed(data):
    headers = data[0]
    title_column_index = headers.index('Title')
    company_column_index = headers.index('Company')
    salary_column_index = headers.index('Salary1')

    output_rows = []
    header_row = ['Title', 'Location', 'Salary', 'Is Remote', 'Is Hybrid', 'Source']
    output_rows.append(header_row)
    
    for i, row in enumerate(data):
        if i == 0:
            continue
        else:
            title_val = row[title_column_index]
            location = get_location(row[company_column_index])
            
            if not is_dmv(location):
                continue

            is_remote = get_remote(row[company_column_index])
            is_hybrid = get_hybrid(row[company_column_index])
            salary = get_salary_indeed(row[salary_column_index])

            if len(salary) == 0:
                continue

            new_row = [title_val, location, salary, is_remote, is_hybrid, 'Indeed']
            output_rows.append(new_row)
    
    return output_rows

def get_location(val):
    # Extract city and state using regular expressions
    # Remote in New York, NY 12345
    pattern1 = r'in\s+(.+),\s+([A-Za-z]{2})(?:\s+(\d{5}))?$'

    # Herndon,Va
    pattern2 = r"^(.*?),\s+([A-Z]{2})$"
    # Remote in Arizona
    pattern3 = r"Remote in\s+([A-Za-z]+)"
    # Boston,MA abcdefg
    pattern4 = r"^(.*?),\s*([A-Z]{2})"
    # Hybrid remote in Chicago, IL


    match1 = re.search(pattern1, val)
    match2 = re.search(pattern2, val)
    match3 = re.search(pattern3, val)
    match4 = re.search(pattern4, val)

    if match1:
        city = match1.group(1)
        state = match1.group(2)
        result = city + ', ' + state
        return result
    elif match2:
        city = match2.group(1)
        state = match2.group(2)
        result = city + ', ' + state
        return result
    elif match3:
        return match3.group(1)
    elif match4:
        city = match4.group(1)
        state = match4.group(2)
        result = city + ', ' + state 
        return result
    else:
        return ""

def get_remote(val):
    remote_str = 'Remote'
    if remote_str.lower() in val.lower():
        return 'Yes'
    else:
        return 'No'

def get_hybrid(val):
    hybrid_str = 'Hybrid'
    if hybrid_str.lower() in val.lower():
        return 'Yes'
    else:
        return 'No'
    
def get_salary_glassdoor(salary_string):
    if 'hour' in salary_string.lower():
        return extract_salary_range(salary_string, 40*52)
    else:
        return extract_salary_range(salary_string, 1)

def get_salary_indeed(salary_string):
    if 'year' in salary_string:  # Salary represented as a range in thousands
        return extract_salary_range(salary_string, 1)
    elif 'hour' in salary_string:  # Salary represented as an hourly rate
        return extract_salary_range(salary_string, 40*52)
    elif 'month' in salary_string: # Salary represented as monthly rate
        return extract_salary_range(salary_string, 12)
    return ""

def extract_salary_range(string, multiplier):
    # $100k - $150k format
    pattern1 = r'\$([\d\.]+)K - \$([\d\.]+)K'
    # $100000 - $150000 format
    pattern2 = r'\$([\d.,]+)\s*-\s*\$([\d.,]+)'
    # $100000 format
    pattern3 = r'\$([\d,]+)'
    # $180K format
    pattern4 = r'\$([\d.,]+)K'

    match1 = re.search(pattern1, string)
    match2 = re.search(pattern2, string)
    match3 = re.search(pattern3, string)
    match4 = re.search(pattern4, string)

    if match1:
        lower_bound = float(match1.group(1)) * 1000 * multiplier
        upper_bound = float(match1.group(2)) * 1000 * multiplier
        return str(lower_bound) + '-' + str(upper_bound)
    elif match2:
        lower_bound = float(match2.group(1).replace(',', '')) * multiplier
        upper_bound = float(match2.group(2).replace(',', '')) * multiplier
        return str(lower_bound) + '-' + str(upper_bound)
    elif match4:
        salary = float(match4.group(1).replace(',', '')) * 1000 * multiplier
        return str(salary)
    elif match3:
        salary = float(match3.group(1).replace(',', '')) * multiplier
        return str(salary)
    else:
        return ""

def get_indeed_input_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'INDEED listin 1 JUL.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

def get_glassdoor_input_file_path():
    file_name = 'V2_GlassdoorCyber security Jobs in Washington, DC, July 2023.csv'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    return file_path


def get_output_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'INDEED-GLASSDOOR-MERGED.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

def remove_bom(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
        content = file.read()

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        file.write(content)

def parse_indeed_data():
    file_path = get_indeed_input_file_path()
    custom_encoding = 'mac_roman'

    contents = read_file(file_path, custom_encoding)
    return extract_relevant_information_indeed(contents)

def parse_glassdoor_data():
    file_path = get_glassdoor_input_file_path()
    remove_bom(file_path)
    custom_encoding = 'mac_roman'

    contents = read_file(file_path, custom_encoding)
    return extract_relevant_information_glassdoor(contents)

def merge_results(indeed_data, glassdoor_data):
    indeed_data = parse_indeed_data()
    glassdoor_data = parse_glassdoor_data()

    for i, row in enumerate(glassdoor_data):
        if i == 0: # exclude headers 
            continue
        else:
            indeed_data.append(row)
    
    return indeed_data

def write_output(data):
    with open(get_output_file_path(), 'w', newline='', encoding="mac_roman") as file:
        writer = csv.writer(file)
        writer.writerows(data)

indeed_data = parse_indeed_data()
glassdoor_data = parse_glassdoor_data()
merged_data = merge_results(indeed_data, glassdoor_data)

write_output(merged_data)

