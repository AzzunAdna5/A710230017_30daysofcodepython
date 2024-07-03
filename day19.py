# Membuka file untuk menulis ('w')
fileku = open("buah.txt", "w")

# Menulis baris-baris teks ke dalam file
fileku.write('Apel\n')
fileku.write('Mangga\n')
fileku.write('Jambu')

# Menutup file setelah selesai menulis
fileku.close()

# Membuka file untuk membaca ('r')
bacafileku = open("buah.txt", "r")

# Membaca seluruh isi file dan mencetaknya
print(bacafileku.read())

# Menutup file setelah selesai membaca
bacafileku.close()
