from pathlib import Path

import matplotlib.pyplot as plt


FIELD_CURRENT = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.33]
GENERATED_VOLTAGE = [182, 187, 192, 196, 200, 204, 207]
OUTPUT_FILE = Path(__file__).with_name("dc_shunt_generator_curve.png")


def validate_measurements(field_current, generated_voltage):
    """Validate paired field-current and generated-voltage measurements."""
    if len(field_current) != len(generated_voltage):
        raise ValueError("Field current and voltage lists must have the same length.")

    if len(field_current) < 2:
        raise ValueError("At least two measurements are required.")

    if any(current < 0 for current in field_current):
        raise ValueError("Field current values cannot be negative.")

    if any(voltage < 0 for voltage in generated_voltage):
        raise ValueError("Generated voltage values cannot be negative.")

    for previous, current in zip(field_current, field_current[1:]):
        if current <= previous:
            raise ValueError("Field current values must be in strictly increasing order.")


def estimate_voltage(field_current, generated_voltage, target_current):
    """Estimate voltage at a given field current using linear interpolation."""
    validate_measurements(field_current, generated_voltage)

    if not field_current[0] <= target_current <= field_current[-1]:
        raise ValueError(
            f"Target current must be between {field_current[0]} A and {field_current[-1]} A."
        )

    for index in range(1, len(field_current)):
        left_current = field_current[index - 1]
        right_current = field_current[index]

        if target_current <= right_current:
            left_voltage = generated_voltage[index - 1]
            right_voltage = generated_voltage[index]
            current_range = right_current - left_current
            voltage_range = right_voltage - left_voltage
            progress = (target_current - left_current) / current_range
            return left_voltage + (voltage_range * progress)

    return generated_voltage[-1]


def summarize_characteristic(field_current, generated_voltage):
    """Return the main numbers for the no-load characteristic curve."""
    validate_measurements(field_current, generated_voltage)

    voltage_gain = generated_voltage[-1] - generated_voltage[0]
    current_gain = field_current[-1] - field_current[0]

    return {
        "minimum_voltage": min(generated_voltage),
        "maximum_voltage": max(generated_voltage),
        "voltage_gain": voltage_gain,
        "average_slope": voltage_gain / current_gain,
    }


def plot_characteristic(field_current, generated_voltage, output_file=OUTPUT_FILE):
    """Create and save the no-load characteristic curve."""
    validate_measurements(field_current, generated_voltage)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        field_current,
        generated_voltage,
        marker="o",
        linestyle="-",
        color="tab:blue",
        label="No-load characteristic",
    )

    ax.set_xlabel("Field Current (If) [A]", fontsize=12)
    ax.set_ylabel("Generated Voltage (E) [V]", fontsize=12)
    ax.set_title("No-Load Characteristics of a DC Shunt Generator", fontsize=14)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_file, dpi=160)
    return output_file


def main():
    summary = summarize_characteristic(FIELD_CURRENT, GENERATED_VOLTAGE)
    estimated_voltage = estimate_voltage(FIELD_CURRENT, GENERATED_VOLTAGE, 0.25)
    output_file = plot_characteristic(FIELD_CURRENT, GENERATED_VOLTAGE)

    print("DC Shunt Generator No-Load Analysis")
    print(f"Minimum voltage: {summary['minimum_voltage']} V")
    print(f"Maximum voltage: {summary['maximum_voltage']} V")
    print(f"Voltage gain: {summary['voltage_gain']} V")
    print(f"Average slope: {summary['average_slope']:.2f} V/A")
    print(f"Estimated voltage at 0.25 A: {estimated_voltage:.2f} V")
    print(f"Chart saved to: {output_file}")


if __name__ == "__main__":
    main()



# summary = summarize_characteristic(FIELD_CURRENT, GENERATED_VOLTAGE)
# estimated_voltage = estimate_voltage(FIELD_CURRENT, GENERATED_VOLTAGE, 0.25)
# output_file = plot_characteristic(FIELD_CURRENT, GENERATED_VOLTAGE)
# print("DC Shunt Generator No-Load Analysis")
# print(f"Minimum voltage: {summary['minimum_voltage']} V")
# print(f"Maximum voltage: {summary['maximum_voltage']} V")

# class ProductsConfig(AppConfig):   


