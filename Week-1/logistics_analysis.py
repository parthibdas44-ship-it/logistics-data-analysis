import pandas as pd

# Load logistics data
# df = pd.read_csv("data/logistics_data.csv")

# Example:
# print(df.head())
# print(df.info())
# print(df.describe())

# Calculate logistics KPIs

def calculate_kpis(df):
    late_rate = (df["Delivery_Status"] == "Late").mean() * 100
    average_delivery_time = df["Delivery_Time_Hours"].mean()

    print("Late Delivery Rate:", late_rate)
    print("Average Delivery Time:", average_delivery_time)


# Predictive modelling will be added
# in later weeks of the project.
