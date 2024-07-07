class Kucing():
    def __init__(self, ras, umur):
        self.ras = ras
        self.umur = umur

class Pemilik():
    def __init__(self, nama, alamat, kucing):
        self.nama = nama
        self.alamat = alamat
        self.kucing = kucing

    def perkenalan(self):
        print(f"Hai, saya {self.nama} dari {self.alamat}")
        print(f"Kucing saya adalah kucing {self.kucing.ras} dan berumur {self.kucing.umur} bulan")

# Membuat objek kucing untuk pemilik Budi
budi = Pemilik(
    nama = "Budi",
    alamat = "Jakarta",
    kucing = Kucing(
        ras = "Anggora",
        umur = 5
    )
)

# Memanggil metode perkenalan milik objek budi
budi.perkenalan()
