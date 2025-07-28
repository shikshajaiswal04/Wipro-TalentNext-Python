'''
EXERCISES
'''

#Q1. Write a program to check if a given number is Positive, Negative or Zero.
num = int(input())
if num==0:
    print("The number is zero")
elif num>0:
    print("Positive no")
elif num<0:
    print("Negative no")
else:
    print("Invalid Input")

#Q2. Write a program to check if a given number is odd or even.
num = int(input())
if num%2==0:
    print("Even")
else:
    print("Odd")

#Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
num1=int(input())
num2=int(input())

if num1%10==num2%10:
    print("True")
else:
    print("False")
    
#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(11):
    print(i,end=" ")

#Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(24,57,2):
    print(i)

#Q6. Write a program to check if a given number is prime or not.
num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

#Q7. Write a program to print prime numbers between 10 and 99.
for num in range(10, 100): 
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):  
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num, end=' ')


#Q8. Write a program to print the sum of all the digits of a given number.
num = int(input("Enter a number: "))
sum_of_digits = 0

num = abs(num)

while num > 0:
    digit = num % 10           
    sum_of_digits += digit     
    num = num // 10            

print("Sum of digits:", sum_of_digits)

#Q9. Write a program to reverse a given number and print.
num = int(input("Enter a number: "))
reversed_num = 0

is_negative = num < 0
num = abs(num)  

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if is_negative:
    reversed_num = -reversed_num

print("Reversed number:", reversed_num)

#Q10. Write a program to find if the given number is palindrom or not.
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original_num == reversed_num:
    print(original_num, "is a palindrome number")
else:
    print(original_num, "is not a palindrome number")