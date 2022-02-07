original_number = int(input("Enter a 3 digit number: "))

sum_of_digits = 0
while (original_number != 0):
    sum_of_digits = sum_of_digits + (original_number % 10)
    original_number = original_number//10 

print("Sum of digits : {}".format(sum_of_digits))
