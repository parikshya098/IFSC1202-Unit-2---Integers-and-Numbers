original_number = int(input("Enter a number: "))
last_digit = original_number % 10
first_digit = (original_number - last_digit) // 10
swapped_number = (last_digit*10)+first_digit
print ("Swapped Number : {} ".format(swapped_number))