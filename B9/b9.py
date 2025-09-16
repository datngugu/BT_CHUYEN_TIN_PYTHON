n = int(input('Nhap N: '))
k = int(input('Nhap K: '))

dayso = []
for i in range(1, n+1):
    dayso.append(int(input(f"So nguyen thu {i}: ")))

maxchuoi = 0

for i in range(0, n):
    chuoi = 1
    temp = i
    for j in range(i + 1, n):
        if dayso[j] >= dayso[temp] + k:
            temp = j
            chuoi += 1
    if chuoi > maxchuoi:
        maxchuoi = chuoi

print(maxchuoi)