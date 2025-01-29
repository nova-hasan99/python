import matplotlib.pyplot as plt

# Dummy data: Field Current (If) in Amperes and Generated Voltage (E) in Volts
field_current = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.33]
generated_voltage = [182, 187, 192, 196, 200, 204, 207]

# Plot the graph
plt.figure(figsize=(8,5))
plt.plot(field_current, generated_voltage, marker='o', linestyle='-', color='b', label='No-Load Characteristic')

# Labels and Title
plt.xlabel('Field Current (If) [A]', fontsize=12)
plt.ylabel('Generated Voltage (E) [V]', fontsize=12)
plt.title('No-Load Characteristics of a DC Shunt Generator', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
