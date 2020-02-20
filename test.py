import sys

# print(sys.argv)

if sys.argv[1] == 'create':
    print("Your Project Created")
elif sys.argv[1] == 'serve':
    print("Your Project serve")
else:
    print("Command not found")


a = int(input("Enter a :"))
b = int(input("Enter b :"))
result = a+b

print("Result is :",result)
