n = int(input('n: '))
p = int(input('p: '))

dayso = []

for i in range(1, n + 1):
    dayso.append(int(input('Cac PT: ')))

maxi = 0

for j in range(0, len(dayso) - p + 1):
    tong = 0
    for z in range(j, j + p):
        tong += dayso[z]
    if tong > maxi:
        maxi = tong

print(maxi)