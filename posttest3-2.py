angka_awal = 1
output = 1
while True:
    try:
        inputan = int(input("Tampilkan angka sebanyak: ")) # NIM = 2009106031 + 10 = 41
    except:
        print("Mohon input angka.")
    else:
        while inputan >= angka_awal: # Ketika inputan melebihi angka_awal
            print(output) # Print sebuah angka output, kemudian
            output += 1 # Nilai output ditambah 1 dalam perulangan jika melebihi angka_awal.
            if output == 10: # Jika output mencapai nilai 10, 
                output -= 9 # maka output tersebut dikurangi 9, agar kembali ke angka 1 lagi.
            angka_awal += 1 # Angka awal akan ditambah 1.
        break