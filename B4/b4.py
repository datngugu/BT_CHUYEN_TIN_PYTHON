i = input('Nhap chuoi ki tu: ')

def so_lon_nhat(kitu):
    kituhieuchinh = list(set(kitu))
    kituhieuchinh.sort(reverse=True)
    return "".join(kituhieuchinh)

print(so_lon_nhat(i))