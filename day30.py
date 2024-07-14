# Open "jurusan.txt" in write mode ('w')
with open("jurusan.txt", "w") as fileku:
    # Write initial lines
    fileku.write('Biologi\n')
    fileku.write('PGSD\n')
    fileku.write('PTI\n')

# File is automatically closed after the 'with' block

# Open "jurusan.txt" in append mode ('a+')
with open("jurusan.txt", 'a+') as f:
    # Append additional lines
    f.write('Akuntansi\n')
    f.write('PAUD')

# File is automatically closed after the 'with' block

# Open "jurusan.txt" in read mode ('r')
with open("jurusan.txt", 'r') as baca:
    # Read and print the entire content
    print(baca.read())
