import math

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    if 0 in numbers[1:]:
        return "Cannot divide by zero!"
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

def square_root(number):
    return math.sqrt(number)

# Display options
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")

choice = input("Enter choice (1/2/3/4/5): ")

if choice in ('1', '2', '3', '4'):
    num_count = int(input("Enter the number of values: "))
    numbers = []
    for i in range(num_count):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    if choice == '1':
        print("Result:", add(numbers))
    elif choice == '2':
        print("Result:", subtract(numbers))
    elif choice == '3':
        print("Result:", multiply(numbers))
    elif choice == '4':
        print("Result:", divide(numbers))
elif choice == '5':
    num = float(input("Enter a number: "))
    print("Square root:", square_root(num))
else:
    print("Invalid input")
