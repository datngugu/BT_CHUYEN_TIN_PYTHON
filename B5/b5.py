s = ''

with open('.//b5.INP', 'r') as f:
    s = f.read()
    f.close()

dem = 0

for i in range(1, len(s) + 1):
    tmp = 0
    chuoihc = ''
    for j in range(i, len(s) + 1):
        tmp += int(s[j-1])
        chuoihc += s[j-1]
        if tmp % 3 == 0 and int(chuoihc) % 97 == 0: 
            dem += 1

with open('.//b5.OUT', 'w') as f:
    f.write(str(dem))
    f.close()
