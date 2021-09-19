for i in range(1, 21, 2):
    print(i, end=' ')
print()

##a

for i in range(0, 110, 10):
    print(i, end=' ')
print()

##b

for i in range(0, 20, 1):
    print(i*-1+20, end=' ')
print()

##c
stars = float(input("Enter Number of Stars: "))

for i in range(0, int(stars)):
    print('*', end=' ')
print()

##d

stars2 = float(input("Enter Number of Stars: "))
for i in range(0, int(stars2)):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
print()