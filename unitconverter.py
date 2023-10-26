def temperature_converter():
    value = float(input("Enter the temperature value: "))
    source_unit = input("Enter the source unit (Celsius or Fahrenheit): ").lower()
    if source_unit == 'celsius':
        target_unit = 'fahrenheit'
        result = (value * 9/5) + 32
    elif source_unit == 'fahrenheit':
        target_unit = 'celsius'
        result = (value - 32) * (5/9)
    else:
        print("Invalid source unit! Please choose Celsius or Fahrenheit.")
        return
    print(f"{value} {source_unit} is equal to {round(result, 2)}      {target_unit}.")
temperature_converter()
