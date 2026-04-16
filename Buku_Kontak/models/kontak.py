class Kontak:
    def __init__(self,nama,nomor_telepon):
        self.__nama = nama
        self.__nomor_telepon = nomor_telepon
        self.set_nama(nama)
        self.set_nomor_telepon(nomor_telepon)
        
    def tampilkan_info(self):
        return f"Nama: {self.__nama}, Nomor: {self.__nomor_telepon}"
    
    def get_nama(self):
        return self.__nama
    
    def get_nomor_telepon(self):
        return self.__nomor_telepon
    
    def set_nama(self,nama_baru):
        if len(nama_baru) >= 0:
            self.__nama = nama_baru
            print(f"Nama {nama_baru} berhasil diperbarui")
        else:
            print("Nama terlalu pendek minimal 1")
        print(("=="*20))

    def set_nomor_telepon(self,nomor_baru):
        if len(nomor_baru) >= 10:
            self.__nomor_telepon = nomor_baru
            print(f"Nomor {nomor_baru} berhasil diperbarui")
        else:
            print("Nomor terlalu pendek minimal 10 digit")
        print(("=="*20))

