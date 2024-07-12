1. class Car:
2. def __init__(self, merk, model, tahun):
3. self.merk = merk
4. self.model = model
5. self.tahun = tahun
6. self.odometer = 0
7.
8. def keterangan(self):
9. print(f"Mobil baru saya {self.merk} {self.model} tahun
{self.tahun} kilometernya masih {self.odometer}")
10.
11.mobil_baru = Car('Honda','City',2021)
12.mobil_baru.keterangan()