#!/usr/local/bin/python3

import os
import csv
import re
import pandas as pd


def get_input_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'Cyber_Data_new.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

def get_output_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'Cyber_Data_new- UNIQUE.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

def remove_duplicates(input_file, output_file):
    # Create a set to store unique rows
    unique_rows = set()

    # Open the input CSV file
    with open(input_file, 'r', newline='', encoding='mac_roman') as csvfile:
        reader = csv.reader(csvfile)

        # Skip the header row if present (optional)
        header = next(reader, None)

        # Iterate through the rows in the CSV file
        for row in reader:
            # Convert the row to a tuple so that it can be added to the set
            row_tuple = tuple(row)
            unique_rows.add(row_tuple)

    # Write the unique rows to the output CSV file
    with open(output_file, 'w', newline='', encoding='mac_roman') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row back (optional)
        if header:
            writer.writerow(header)

        # Write each unique row to the output file
        for row in unique_rows:
            writer.writerow(row)


remove_duplicates(get_input_file_path(), get_output_file_path())