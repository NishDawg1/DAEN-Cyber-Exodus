#!/usr/local/bin/python3

import os
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def get_input_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'Cyber_Exodus_Data_Final.csv'
    file_path = os.path.join(current_dir, file_name)
    return file_path

data = pd.read_csv(get_input_file_path())

selected_features = ["Weekly_commute","Person_crime","Prop_crime","Work_env","Experience_level","Salary_med"]

X = data[selected_features]
y = data["Candidate"]  # Use the target column as the dependent variable

# Splitting the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


rf_model = RandomForestClassifier()


param_grid = {
    'n_estimators': [50, 100, 150],  # different numbers of estimators (trees)
    'random_state': [42, 123, 456]   # different random state values
}

# Performing grid search with 5-fold cross-validation
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Getting the best hyperparameters from grid search
best_n_estimators = grid_search.best_params_['n_estimators']
best_random_state = grid_search.best_params_['random_state']

# Initializing the Random Forest classifier with the best hyperparameters
best_rf_model = RandomForestClassifier(n_estimators=best_n_estimators, random_state=best_random_state)

# Fitting the best model to the training data
best_rf_model.fit(X_train, y_train)

# predictions on the test data
y_pred = best_rf_model.predict(X_test)

# Evaluating the best model's performance
accuracy = accuracy_score(y_test, y_pred)
print("Best model accuracy:", accuracy)


