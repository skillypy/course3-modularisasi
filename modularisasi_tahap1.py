"""
Menghitung luas Segitiga
Luas Segitiga = alsa * tinggi / 2
"""
print('Menghitung luas segitiga 1')
alas = 10
tinggi = 6
luas = alas * tinggi / 2
print(f"Luas Segitiga dengan alas={alas} dan tinggi={tinggi} adalah={luas}")

print('\nMenghitung luas segitiga 2')
alas = 10
tinggi = 6
luas = alas * tinggi / 2
print(f"Luas Segitiga dengan alas={alas} dan tinggi={tinggi} adalah={luas}")

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 100
tinggi = 2
print(f"\nMenghitung luas segitiga={hitung_luas_segitiga(10,6)}")
print(f"Menghitung luas segitiga={hitung_luas_segitiga(20,2)}")
print(f"Dengan Fungsi,menghitung luas segitiga dengan alas={alas} dan tinggi={tinggi} adalah {hitung_luas_segitiga(alas,tinggi)}")


