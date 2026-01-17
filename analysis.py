import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/accident_data.csv")

# Convert time column
data['Time'] = pd.to_datetime(data['Time'])
data['Hour'] = data['Time'].dt.hour

# Accidents by time of day
plt.figure()
sns.countplot(x='Hour', data=data)
plt.title("Accidents by Time of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.savefig("visuals/accidents_by_time.png")
plt.show()

# Accidents by weather condition
plt.figure()
sns.countplot(y='Weather', data=data, order=data['Weather'].value_counts().index)
plt.title("Accidents by Weather Condition")
plt.savefig("visuals/weather_conditions.png")
plt.show()

# Accident hotspots
plt.figure()
plt.scatter(data['Longitude'], data['Latitude'], alpha=0.3)
plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("visuals/accident_hotspots.png")
plt.show()