# Print 0 to 10

# for(i=0; i < 11; i=i+1){
#     print(i)
# }

# Steps :
#  i = 0
#  condition i < 11,


# for i in range(0, 11):
#     print(i)

# Sum of digits of number
# Input - 1234 , Output - 10

# number = int(input("Enter Number : "))
# sum = 0
# # Logic
# while number > 0:
#     flag = number % 10  # flag = 4,3,2,1
#     sum = sum + flag  # sum = 4,7,9,10
#     number = int(number / 10)  # number = 123,12,1,0

# # Print !
# print(f'Sum = {sum}')


# Fibonnaci
# 0,1,1,2,3,5

# num1, num2 = 0, 1


# third_term = num1 + num2
# num1 = third_term
# num2 = num1


# Reversing the digits of number !
number = 1234
total = 0
while number > 0:
    d = number % 10
    total = total*10 + d
    print(total)
    number = int(number/10)
