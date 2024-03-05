# Two-Year months - repeating the yearly array
months_two_year = months_yearly * 2  # Repeat for two years, or adjust according to your specific labeling

# Dynamic spend data for Two-Year forecast - manually entered based on the dynamic calculation provided
dynamic_two_year_original = [your_dynamic_two_year_original_values_here] * 2  # Repeat or adjust your dynamic values for two years
dynamic_two_year_reduced = [your_dynamic_two_year_reduced_values_here] * 2  # Repeat or adjust your dynamic values for two years

plt.figure(figsize=(12, 7))
plt.plot(months_two_year[:24], dynamic_two_year_original[:24], marker='o', linestyle='-', color='b', label='Original Spend')
plt.plot(months_two_year[:24], dynamic_two_year_reduced[:24], marker='x', linestyle='--', color='r', label='Reduced Spend')
plt.title("Two-Year Compute Spend Forecast (Dynamic)")
plt.xlabel("Time (Months)")
plt.ylabel("Compute Spend ($)")
plt.xticks(np.arange(0, 24, 3), months_two_year[:24:3], rotation=45)  # Show every 3rd month label for clarity
plt.legend()
plt.grid(True)
plt.show()
