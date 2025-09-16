n = 0
dayso = []

with open(".//b8.INP", 'r') as f:
    lines = f.readlines()
    n,dayso = int(lines[0].strip()), [int(giatrinhap) for giatrinhap in lines[1].split()]
    f.close()

maxUCLN = 0

for i in range(0, n):
    ucln = 0
    for j in range(i + 1, n):
        a = dayso[i]
        b = dayso[j]
        while not(a == b):
            if a > b:
                a -= b
            else:
                b -= a
        ucln = a
        if ucln > maxUCLN:
            maxUCLN = ucln

with open(".//b8.OUT", 'w') as f:
    f.write(str(maxUCLN))
    f.close()