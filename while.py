number = int(input("Please enter a number between 100 and 500 "))
while number < 100 or number > 500:
    print("Please enter the correct number:")
    number = int(input("Please enter a number between 100 and 500 "))
else:
    print("Given number is correct", number)