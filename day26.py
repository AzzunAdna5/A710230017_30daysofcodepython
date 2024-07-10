class Makanan():  # Mengubah class Kucing menjadi Makanan
    def __init__(self, jenis, kalori):
        self.jenis = jenis
        self.kalori = kalori


class Pemilik():  # Mengubah class Pemilik
    def __init__(self, nama, alamat, makanan):
        self.nama = nama
        self.alamat = alamat
        self.makanan = makanan
    
    def tampil(self):
        print(f"Halo, aku {self.nama} berasal dari {self.alamat}")
        print(f"Makanan kesukaanku adalah {self.makanan.jenis} dengan kalori {self.makanan.kalori} kkal")


makanan_arif = Makanan(
    jenis="Sushi",
    kalori=500
)

arif = Pemilik(
    nama="Arif",
    alamat="Solo",
    makanan=makanan_arif
)

arif.tampil()
