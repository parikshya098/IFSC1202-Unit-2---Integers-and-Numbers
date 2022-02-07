original_number = int(input("Enter a 3 digit number: "))

reverse = 0
while original_number > 0:
    rem = original_number % 10                 
    reverse = reverse * 10 + rem              
    original_number //= 10           
    
print("Reverse of digits : {}".format(reverse))