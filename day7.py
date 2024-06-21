# Menulis ke dalam file "buah.txt"
fileku = open("buah.txt", "w")
fileku.write('Apel\n')
fileku.write('Mangga\n')
fileku.write('Jambu\n')  # Menambahkan '\n' agar setiap baris berada di baris yang berbeda
fileku.close()

# Membaca dari file "buah.txt" setelah penulisan
bacafileku = open("buah.txt", "r")
print(bacafileku.read())
bacafileku.close()  # Penting untuk selalu menutup file setelah selesai menggunakan
