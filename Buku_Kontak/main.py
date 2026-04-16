from models.kontak import Kontak

if __name__ == "__main__":
    daftar_kontak = []

    kontak1 = Kontak("Febri","082277874003")
    kontak2 = Kontak("Cihuy","081264734980")
    kontak3 = Kontak("Yu zhong","082397797555")

    daftar_kontak.append(kontak1)
    daftar_kontak.append(kontak2)
    daftar_kontak.append(kontak3)

    print("Daftar Kontak Saya\n",'='*40)
    for kontak in daftar_kontak:
        print(kontak.tampilkan_info())
