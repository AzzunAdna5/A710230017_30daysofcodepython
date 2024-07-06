# Membuka file "jurusan.txt" dalam mode 'w' untuk menulis
with open("jurusan.txt", "w") as fileku:
    fileku.write('Biologi\n')
    fileku.write('PGSD\n')
    fileku.write('PTI\n')

# Menutup file setelah selesai menulis
# Tidak perlu baris kosong (6) setelah menutup file

# Membuka file "jurusan.txt" dalam mode 'a+' untuk menambahkan dan membaca
with open("jurusan.txt", 'a+') as f:
    f.write('Akuntansi\n')
    f.write('PAUD')

    # Mengatur kursor ke awal file untuk membaca
    f.seek(0)

    # Membaca dan mencetak isi file
    print(f.read())
