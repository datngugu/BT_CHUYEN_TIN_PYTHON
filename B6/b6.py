a = int(input("a: "))
b = int(input("b: "))

i = 1
dayso = []
tong = 0

while len(dayso) < b:
    for y in range(1, i+1):
        dayso.append(i)
    i += 1

i = a
while i <= b:
    tong += dayso[i - 1]
    i += 1

print(tong)