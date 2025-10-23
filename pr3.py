def check_temperature(temp_celsius):
    if temp_celsius < 15:
        status = "Cold"
    elif 15 <= temp_celsius <= 30:
        status = "Normal"
    else:
        status = "Hot"
    print(f"Temperature: {temp_celsius}°C")
    print(f"Status: {status}")



