from sys import argv
from math import sqrt

if len(argv) < 4:
    print("Недостаточно параметров!")
elif len(argv) > 4:
    print("Слишком много параметров!")
else:
    a = int(argv[1])
    b = int(argv[2])
    c = int(argv[3])
    p = (a + b + c)/2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)