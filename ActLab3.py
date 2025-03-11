def check_number(num):
    
    try:
        num = int(num)
        if num % 2 == 0:
            return f"{num} is an Even number."
        else:
            return f"{num} is an Odd number."
    except ValueError:
        return "Invalid input: Please enter an integer."

num_str = input("Enter an integer: ")

result = check_number(num_str)
print(result)