print("2. Time Converter:")
print(" - Ask user for seconds")
print(" - Convert to hours, minutes, and remaining seconds")
print(" - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()
print("2. Time Converter:")
print(" - Ask user for seconds")
print(" - Convert to hours, minutes, and remaining seconds")
print(" - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

seconds = int(input("Enter seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"{seconds} seconds = {hours} hour(s), {minutes} minute(s), {remaining_seconds} second(s)")