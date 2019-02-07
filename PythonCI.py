try:
    x=int(input("Please enter number: "))
    if x < 0 or x > 100:
        raise ValueError("NUMBER must be between 0 and 100") 
except ValueError as e:
    print(e)
else:
    print("result is: ",x)     