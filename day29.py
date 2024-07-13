# Deklarasi dictionaries
lantai = {'lobby': 1, 'kantor': 2, 'kantin': 3, 'parkir': 'rooftop'}

# Akses dictionaries
lantai['parkir'] = 'basement'

# Menambah elemen
lantai['labkom'] = 4

# Hapus elemen berdasar key menggunakan pop
lantai.pop('lobby')

# Hapus semua elemen
lantai.clear()

print(lantai)  # Output: {}
