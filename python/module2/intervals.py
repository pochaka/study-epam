from sys import argv

if len(argv) < 2:
    print("Передайте параметр!")
elif (int(argv[1]) > -15 and int(argv[1]) <= 12)  \
    or (int(argv[1]) > 14 and int(argv[1]) < 17)  \
    or int(argv[1]) >= 19:
    print("True")
else:
    print(False)