class Dog:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def duduk(self):
        print(f"{self.nama} sekarang duduk")
    
    def berdiri(self):
        print(f"{self.nama} sekarang berdiri")

# Membuat objek my_dog dari kelas Dog
my_dog = Dog("Labrador", 6)

# Mengakses atribut nama dan umur dari objek my_dog
print(f"anjingku bernama {my_dog.nama}")
print(f"anjingku berumur {my_dog.umur} tahun")
