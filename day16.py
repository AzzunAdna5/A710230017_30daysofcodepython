truk = ('hino', 3000, 2.5, 130)

# Menyimpan nilai-nilai dari tuple `truk` ke dalam variabel terpisah
merk, cc, berat, top_speed = truk

# Mencetak nilai dari tuple `truk` menggunakan indeks
print(truk[0])   # Output: hino

# Mencetak potongan tuple `truk`
print(truk[:2])  # Output: ('hino', 3000)
print(truk[2:])  # Output: (2.5, 130)

# Mencari indeks dari nilai 3000 dalam tuple `truk`
print(truk.index(3000))  # Output: 1

# Memeriksa keanggotaan nilai 2.5 dalam tuple `truk`
print(2.5 in truk)  # Output: True

# Mencetak kalimat dengan memformat string
print('truk {} memiliki berat {} ton, kapasitas {} cc dan top speed {} km/jam'.format(merk, berat, cc, top_speed))
