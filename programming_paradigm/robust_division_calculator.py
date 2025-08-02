

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        division = numerator/denominator
        
    except ZeroDivisionError as e:
        if denominator == 0:
            print("Error: Cannot divide by zero.")
        
    except ValueError as e:
        print("Non numeric input.Please enter valid numbers.")
    else:
            return f"The result of the division is {division}"
        
        
    

