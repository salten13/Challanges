numbers = []
for x in range(2000,3201):
    numbers.append(x)
    if x % 7 == 0 and x % 5 != 0:
        print(x, end=',')
print('\n')
