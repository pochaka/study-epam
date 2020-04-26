from sys import argv

try:
    number = int(argv[1])
except ValueError:
    raise ValueError("Передайте параметр!")

if -15 < number <= 12 or 14 < number < 17 or number >= 19:
    print("True")
else:
    print("False")
