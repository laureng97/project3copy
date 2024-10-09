import pandas as pd

# Load Excel files
capitals_df = pd.read_csv("capital_cities.csv")
emissions_df = pd.read_csv('greenhouse_emission.csv')
surface_temps_df = pd.read_csv('annual_surface_temps.csv')
global_data_df = pd.read_csv('global_data.csv')

# Combine the data

# Table 1: Merge Capitals and Emissions (no dropping yet)
table1 = pd.merge(capitals_df, emissions_df, on='country', how='inner')

# Table 2: Merge Surface Temps and Global Data (no dropping yet)
table2 = pd.merge(surface_temps_df, global_data_df, on='country', how='inner')

# Display the tables before dropping missing values
print("Table 1 (Capitals and Emissions) before dropping missing values:")
print(table1.head())  # or display the full table with print(table1)

print("\nTable 2 (Surface Temps and Global Data) before dropping missing values:")
print(table2.head())  # or display the full table with print(table2)

# Optionally, check for missing values
print("\nMissing values in Table 1:")
print(table1.isna().sum())  # Shows number of missing values per column

print("\nMissing values in Table 2:")
print(table2.isna().sum())  # Shows number of missing values per column

# After inspecting, you can clean the tables by dropping missing values (if necessary)
# table1_cleaned = table1.dropna()
# table2_cleaned = table2.dropna()
