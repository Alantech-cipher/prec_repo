import numpy as np

# Simulate temperature data for 30 days (in Celsius)
np.random.seed(10)  # for reproducibility
temperatures = np.random.normal(loc=28, scale=5, size=30)  # mean=28, std=5

# Round the temperatures to 2 decimal places
temperatures = np.round(temperatures, 2)

# Print all temperature values
print("Daily Temperatures (°C):")
print(temperatures)

# Calculate statistics
average_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
std_temp = np.std(temperatures)
hot_days = np.sum(temperatures > 30)

# Print results
print("\n--- Weather Summary ---")
print(f"Average Temperature: {average_temp:.2f}°C")
print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")
print(f"Standard Deviation: {std_temp:.2f}")
print(f"Number of Hot Days (>30°C): {hot_days}")
