# Load necessary libraries
library(readr)
library(here)


# Step 1: Read data from the CSV file, selecting only specific columns and reading them as factors
selected_columns <- c("Salary_med", "Weekly_commute", "Person_crime", "Prop_crime", "Experience_level", "Candidate")
current_directory <- dirname(rstudioapi::getSourceEditorContext()$path)

# Construct the file path relative to the current script
file_path <- file.path(current_directory, "Cyber_Data_new.csv")

data <- read_csv(file_path, col_select = selected_columns, col_types = cols(.default = "f"))

# Step 2: Create a correlation matrix
correlation_matrix <- cor(data)

# Print the correlation matrix
print(correlation_matrix)
