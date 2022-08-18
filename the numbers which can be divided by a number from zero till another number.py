

number1=int(input('enter the first number:'))
number2=int(input('enter the second number:'))

print(number1,number2)

for number in range(number1+1):
    
    if number%number2==0:
        print(number)
