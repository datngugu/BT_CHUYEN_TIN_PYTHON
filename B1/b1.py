import sys, math

giatrinhapvao = [int(i) for i in input('Nhap n, q: ').split()]
daysok = []
n = giatrinhapvao[0]
q = giatrinhapvao[1]

if 2 <= n <= 10**6 and q <= 10**6 and len(giatrinhapvao) == 2:
    for i in range(1, q + 1):
        l = int(input('Nhap K: '))
        if 2 <= l <= n:
            daysok.append(l)
        else:
            print('Nhap loi')
else:
    print('Nhap loi')
    sys.exit()

def kt_so_nguyen_to(so):
    for z in range(2, int(so ** 0.5) + 1):
        if so % z == 0:
            return False
    else:
        return True
        

for y in daysok:
    dem = 0
    for j in range(2, n + 1):
        maxUngt = 0
        for n in range(2, j + 1):
            if j % n == 0:
                if kt_so_nguyen_to(n) and n > maxUngt:
                    maxUngt = n
        if maxUngt <= y:
            dem += 1
    print(dem)