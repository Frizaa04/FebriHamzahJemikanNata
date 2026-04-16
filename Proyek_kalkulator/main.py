from bangun_datar.Lingkaran import lingkaran
from bangun_datar.Persegi import persegi

def jalankan_program():
    print("=== Menghitung Luas Bangun Datar(Versi Modular) ===")

    lingkaran_a = lingkaran(7)
    luas_lingkaran = lingkaran_a.hitung_luas()
    print(f"Luas lingkaran dengan ukuran adalah {luas_lingkaran}")

    persegi_b = persegi(5)
    luas_persegi = persegi_b.hitung_luas()
    print(f'Luas Persegi dengan ukuran adalah {luas_persegi}')

if __name__ == "__main__":
    jalankan_program()