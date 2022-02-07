a = int(input("Enter first two digit number : " ))
b = int(input("Enter second two digit number : "))

unit_digit_a = a % 10
tens_digit_a = (a - unit_digit_a) // 10

unit_digit_b = b % 10
tens_digit_b = (b - unit_digit_b) // 10

merged_number = tens_digit_a*1000 + tens_digit_b*100 + unit_digit_a*10 + unit_digit_b

print("Merged number : {}".format(merged_number))