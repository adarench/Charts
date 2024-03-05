# one year chart

import matplotlib.pyplot as plt
import numpy as np

# Yearly months
months_yearly = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Dynamic spend data for Yearly forecast - manually entered based on the dynamic calculation provided
dynamic_yearly_original = [your_dynamic_yearly_original_values_here]  # Replace with your dynamic_yearly_original values
dynamic_yearly_reduced = [your_dynamic_yearly_reduced_values_here]  # Replace with your dynamic_yearly_reduced values

plt.figure(figsize=(12, 7))
plt.plot(months_yearly, dynamic_yearly_original, marker='o', linestyle='-', color='b', label='Original Spend')
plt.plot(months_yearly, dynamic_yearly_reduced, marker='x', linestyle='--', color='r', label='Reduced Spend')
plt.title("Yearly Compute Spend Forecast (Dynamic)")
plt.xlabel("Time (Months)")
plt.ylabel("Compute Spend ($)")
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.legend()
plt.grid(True)
plt.show()
