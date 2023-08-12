#!/usr/local/bin/python3
# Python package dependencies
import os
import requests
import json
import pandas as pd
import time

def get_results_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'results.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

api_key = 'LWDtVhiq.T0N0jWcjMhSWHExPtdd1xVhRYjtvF5c6'

headers = {
    'X-API-Key': f'{api_key}',    
    'Content-Type': 'application/json'
}
 # For the asynchronous API, we set our parameters and request the report
query_params = {
    "state_or_territory":"VA", # Use an upper-case two digit code for the state or territory you intend to query
    "start":"2021-06-01", # Start date of the results (inclusive)
    "end":"2021-06-30", # End date of the results (inclusive). Please notethat you cannot request more than 35 days of data at a time
    # Dates are midnight to midnight, so 2021-06-01 to 2021-06-02 is one day ofdata, for 2021-06-01
    "format":"csv", # Currently supports csv and ndjson formats
    "date_column":"date_compiled", # Or "date_acquired"
}

# Requests the report from the Data Warehouse.
report_request_response = requests.post('https://api.nlxresearchhub.org/api/job_reports/',
 headers=headers, data=json.dumps(query_params))
 # wait for the report to complete and query the API until the report is complete
# Sleep for 10 seconds between requests to avoid rate limitations
not_done = True
while not_done:
    print("Sleeping for 10 seconds to wait for report")
    time.sleep(10)
    report_request_json = report_request_response.json()
    report_status_url = report_request_json['data'][0]['url']
    report_status_response = requests.get(report_status_url,headers=headers)
    report_status_json = report_status_response.json()
    if report_status_json['data']:
        if report_status_json['data'][0]['status'] == 'done':
           not_done = False
    else:
        print("Report Status: ", report_status_json['data'][0]['status'])

# output will contain the signed AWS S3 url that we download to a Pandas dataframe below
print("Report is done. Downloading...")
report_output_df = pd.read_csv(report_status_json['data'][0]['resource']['link'])
print("Download completed.")
 # Choose where you want your downloaded file to be saved: #
report_output_df.to_csv(get_results_file_path())
 