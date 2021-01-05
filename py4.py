# List user input !

list_length = int(input("Enter list length : "))
number = []

for i in range(0, list_length):
    num = int(input("Enter Number : "))
    number.append(num)

print("Numbers : ", number)
