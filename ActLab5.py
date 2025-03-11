def classify_age(age):
   
    try:
        age = int(input("Please state your age: "))  
        if age < 0:
            print("Invalid age. Please enter a positive number.")
        elif age <= 12:
            print("You are a Child.")
        elif age <= 19:
            print("You are a Teen.")
        elif age <= 34:
            print("You are an Adult.")
        elif age >= 65:
            print("You are a Senior.")
        else: 
            print("Unexpected age value.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


classify_age(0)