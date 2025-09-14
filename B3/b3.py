import sys

n = None
dayso = []

try:
    with open('.//b3.INP', 'r') as f:
        giatrinhap = [line.strip() for line in f.readlines()]
        n, dayso = int(giatrinhap[0]), [int(giatri) for giatri in giatrinhap[1].split(',')] 
        if not(1 <= n <= 10 ** 6 and (len(dayso) == n)):
            print('Nhap Loi')
            f.close()
            sys.exit()
        else:
            for a in dayso:
                if not(1 <= a <= 10 ** 18):
                    print('Nhap Loi')
                    f.close()
                    sys.exit()   
        f.close()
except FileNotFoundError:
    print('Khong tim thay file .INP')
    sys.exit()

count = 0

for x in dayso:
    dem = 1
    for y in range(2, x + 1):
        if x % y == 0:
            dem += 1
    if dem % 2 == 1:
        count += 1

with open('.//b3.OUT', 'w') as f:
    f.write(str(count))
    f.close()
