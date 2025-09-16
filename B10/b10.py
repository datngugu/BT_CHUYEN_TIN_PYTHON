import math

n = int(input('So o vuong: '))
k = int(input('So o toi da: '))

nangluong = []
kq = 0

for v in range(1, n+1):
    nangluong.append(int(input('Nang luong o {}: '.format(str(v)))))

tmp = list(nangluong)
tmp.sort()
tmp = tmp[1:k]

tmp1 = 0
for i in range(1, n):
    if nangluong[i] in tmp:
        kq += math.fabs(nangluong[i] - nangluong[tmp1])
        tmp1 = i

print(kq)