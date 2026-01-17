Example: Creating a user-defined function that converts centimeters to inches (using `return`)
# Function to convert centimeters to inches
def cm_to_inches(cm):
    inches = cm / 2.54    # 1 inch = 2.54 cm
    return inches         # Return the result to the caller

# --- Examples of using the function ---
length_cm = 100
length_inches = cm_to_inches(length_cm)

print(f"{length_cm} cm is equal to {length_inches:.2f} inches")
# Output: 100 cm is equal to 39.37 inches

# You can also use it directly:
print("5 cm =", cm_to_inches(5), "inches")
# Output: 5 cm = 1.968503937007874 inches

# Another example with more precision control:
print(f"30.48 cm is exactly {cm_to_inches(30.48):.4f} inches")
# Output: 30.48 cm is exactly 12.0000 inches
Quick explanation for beginners:
	•	def starts the function definition
	•	cm_to_inches is the function name (choose clear, descriptive names!)
	•	(cm) is the parameter — the value passed into the function
	•	return sends the calculated result back to where the function was called
	•	You can store the returned value in a variable or use it directly in print()
Feel free to try different centimeter values and see the magic happen! 🚀
