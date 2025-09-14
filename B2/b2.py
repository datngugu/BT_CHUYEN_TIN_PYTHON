import sys

vt_tho, vt_carot, buoc_moi_lan = None, None, None

try:
    with open(".\\b2.INP", 'r') as f:
        giatrinhap = [int(i) for i in f.read().split()]
        if len(giatrinhap) == 3 and 1 <= giatrinhap[0] <= giatrinhap[1] <= 10 ** 12 and 1 <= giatrinhap[2] <= 10 ** 3:
            vt_tho, vt_carot, buoc_moi_lan = giatrinhap
            f.close()
        else: 
            print('Nhap Loi')
            f.close()
            sys.exit()
except FileNotFoundError:
    print('File Khong Tim Thay')
    sys.exit()

dem = 0
while vt_carot > vt_tho:
    vt_tho += buoc_moi_lan
    dem += 1

with open('.\\b2.OUT', 'w') as f:
    f.write(str(dem))
    f.close()