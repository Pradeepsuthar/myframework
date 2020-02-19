import sys

# print(sys.argv)

if sys.argv[1] == 'create':
    print("Your Project Created")
elif sys.argv[1] == 'serve':
    print("Your Project serve")
else:
    print("Command not found")
