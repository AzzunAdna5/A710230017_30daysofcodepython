# Membaca dari file "buah.txt"
bacafileku = open("buah.txt", "r")
isi_buah = bacafileku.read()
bacafileku.close()

# Menulis ke dalam file "hewan.txt"
file_hewan = open("hewan.txt", "w")
file_hewan.write(isi_buah)
file_hewan.close()
