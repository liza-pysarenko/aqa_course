# task_1

def convert_temperature():
    celsius = float(input("Enter the temperature in Celsius: "))

    fahrenheit = celsius * 9/5 + 32  # Temperature calculation in Fahrenheit

    kelvin = celsius + 273.15  # Temperature calculation in Kelvin

    print(f"The temperature in Fahrenheit: {fahrenheit} F")
    print(f"The temperature in Kelvin: {kelvin} K")

if __name__ == "__main__":
    convert_temperature()

# task_2

def total_mix_volume_temperature(v1, t1, v2, t2):
    mix_volume = v1 + v2
    mix_temperature = (v1 * t1 + v2 * t2) / mix_volume
    return mix_volume, mix_temperature

def main():
    v1 = float(input("Enter the volume of the first liquid (liters): "))
    t1 = float(input("Enter the temperature of the first liquid (degrees Celsius): "))
    v2 = float(input("Enter the volume of the second liquid (liters): "))
    t2 = float(input("Enter the temperature of the second liquid (degrees Celsius): "))

    mix_volume, mix_temperature = total_mix_volume_temperature(v1, t1, v2, t2)

    print(f"Total volume: {mix_volume} liters")
    print(f"Total temperature: {mix_temperature} degrees Celsius")

if __name__ == "__main__":
    main()

# task_3

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an arithmetic operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Division by zero is impossible!")
                return
            result = num1 / num2
        else:
            print("Incorrect operation.")
            return

        print(f"The result is {result}")
    except ValueError:
        print("Please enter the valid values.")

if __name__ == "__main__":
    calculator()
