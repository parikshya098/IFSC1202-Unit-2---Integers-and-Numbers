original_number = int(input("Enter a number: "))
last_digit = original_number % 10
first_digit = (original_number - last_digit) // 10
print("Ones digit : {} \nTens digit : {}".format(last_digit, first_digit))
