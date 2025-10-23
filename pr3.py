def check_temperature(temp_celsius):
    if temp_celsius < 15:
        status = "Cold"
    elif 15 <= temp_celsius <= 30:
        status = "Normal"
    else:
        status = "Hot"
    print(f"Temperature: {temp_celsius}°C")
    print(f"Status: {status}")





def check_temperature(temp_celsius):
    if temp_celsius < 15:
        status = "Cold"
    elif 15 <= temp_celsius <= 30:
        status = "Normal"
    else:
        status = "Hot"

    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"Temperature: {temp_celsius}°C")
    print(f"Status: {status}")
    print(f"Temperature in Fahrenheit: {temp_fahrenheit:.1f}°F")

check_temperature(35)