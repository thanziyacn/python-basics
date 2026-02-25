print("=== Simple Unit Converter ===")

print("1. Celsius to Fahrenheit")
print("2. Kilometers to Meters")
print("3. Volts to Millivolts")

choice = int(input("Choose option (1-3): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit:", round(f, 2))

elif choice == 2:
    km = float(input("Enter distance in Kilometers: "))
    meters = km * 1000
    print("Distance in Meters:", meters)

elif choice == 3:
    v = float(input("Enter voltage in Volts: "))
    mv = v * 1000
    print("Voltage in Millivolts:", mv)

else:
    print("Invalid choice!")