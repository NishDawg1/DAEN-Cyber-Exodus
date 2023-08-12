import pandas as pd
import os
import matplotlib.pyplot as plt

def get_results_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'Cyber_data_new.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

data = pd.read_csv(get_results_file_path())

grouped_data = data.groupby('Title')[['Remote', 'Hybrid']].sum()

# Step 4: Get the top 5 job titles for remote and hybrid jobs
top_5_remote = grouped_data.nlargest(5, 'Remote')
top_5_hybrid = grouped_data.nlargest(4, 'Hybrid')

job_titles_remote = top_5_remote.index
job_titles_hybrid = top_5_hybrid.index
remote_count = top_5_remote['Remote']
hybrid_count = top_5_hybrid['Hybrid']

bar_positions_remote = range(len(job_titles_remote))
bar_positions_hybrid = range(len(job_titles_hybrid))
bar_width = 0.35

bar_positions = range(len(job_titles_remote) + len(job_titles_hybrid))
bar_width = 0.4

# Increase the size of the figure
plt.figure(figsize=(12, 10))

# Adjust the bar width and position to increase space between bars
plt.bar(bar_positions[:len(job_titles_remote)], remote_count, width=bar_width, label='Remote', color='#006400')
plt.bar(bar_positions[len(job_titles_remote):], hybrid_count, width=bar_width, label='Hybrid',color='#FFDB58')

# Set x-tick positions and labels
plt.xticks(bar_positions, list(job_titles_remote) + list(job_titles_hybrid), rotation=15, ha='right')

plt.xlabel('Job Title')
plt.ylabel('Count')
plt.title('Top 5 Job Titles for Remote and Hybrid Jobs')
plt.legend()

plt.tight_layout()
plt.show()
