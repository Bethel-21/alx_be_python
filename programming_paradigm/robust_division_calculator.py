

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        division = numerator/denominator
        
    except ZeroDivisionError as e:
        if denominator == 0:
            print("Error: Cannot divide by zero.")
        
    except ValueError as e:
        print("Error: Please enter numeric values only.")
    else:
            print(f"The result of the division is {division}")
        
        
    

