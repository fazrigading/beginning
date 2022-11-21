import os
# Dibuat oleh Gading Ketua Angkatan Informatika 2020
tambahan_gaji = [0,0,0]
list_diskon = [0,0,0]
bungkus = [0,0,0]
daftar_rasa = ["Coklat", "Strawberry", "Kacang"]

def cls(): 
    os.system("cls" if os.name == "nt" else "clear")

def hitung(rasa, level, gaji):
    while True:
        try: 
            if rasa == "Coklat": 
                banyak = int(input("Jumlah Bungkus Coklat: "))
            if rasa == "Strawberry": 
                banyak = int(input("Jumlah Bungkus Strawberry: "))
            if rasa == "Kacang": 
                banyak = int(input("Jumlah Bungkus Kacang: "))
            if banyak < 1: raise ValueError
        except ValueError: input("Mohon input nilai >= 0.")
        except: input("Mohon masukkan angka. Tekan Enter untuk lanjut...")
        else: break
    diskon = 0
    if rasa == "Coklat":
        if banyak > 5000 and banyak <= 6000:
            if level == 'A': diskon = 0.35
            elif level == 'B': diskon = 0.25
            elif level == 'C': diskon = 0.15
        elif banyak >= 4000 and banyak <= 5000:
            if level == 'A': diskon = 0.30
            elif level == 'B': diskon = 0.20
            elif level == 'C': diskon = 0.10
        elif banyak >= 3000 and banyak < 4000:
            if level == 'A': diskon = 0.25
            elif level == 'B': diskon = 0.15
            elif level == 'C': diskon = 0.5

    elif rasa == "Strawberry" or rasa == "Kacang":
        if banyak > 5000 and banyak <= 6000:
            if level == 'A': diskon = 0.40
            elif level == 'B': diskon = 0.30
            elif level == 'C': diskon = 0.20
        elif banyak >= 4000 and banyak <= 5000:
            if level == 'A': diskon = 0.30
            elif level == 'B': diskon = 0.20
            elif level == 'C': diskon = 0.10
        elif banyak >= 3000 and banyak < 4000:
            if level == 'A': diskon = 0.15
            elif level == 'B': diskon = 0.7
            elif level == 'C': diskon = 0.5
    indeks = 0 if rasa == "Coklat" else 1 if rasa == "Strawberry" else 2 if rasa == "Kacang" else 3
    bungkus[indeks] = banyak
    if banyak < 3000 and banyak > 6000:
        tambahan_gaji[indeks] = gaji
        list_diskon[indeks] = 0
    else:
        tambahan_gaji[indeks] = gaji * diskon
        list_diskon[indeks] = diskon

def menu():
    cls()
    print("======================================================")
    print(" SELAMAT DATANG DI KALKULATOR PEGAWAI BUNGKUS PERMEN  ")
    print("======================================================")
    nama = str(input("Input Nama: "))
    while True:
        level = str(input("Level Anda: "))
        if len(level) == 1 and level == "A" or level == "B" or level == "C":
            break
        else: 
            input("Mohon masukkan A, B, atau C.")
    gaji = 7000 if level == 'A' else 5000 if level == 'B' else 3000 if level == 'C' else 0
    while True:
        cls()
        print("=========================================")
        print("Nama :", nama)
        print("Level:", level)
        print("Status:\nCoklat:\t\t Strawberry:\t Kacang:")
        print(bungkus[0], "\t\t", bungkus[1], "\t\t", bungkus[2])
        print("Menu:")
        print("[1] Coklat\n[2] Strawberry\n[3] Kacang\n[0] Selesai")
        print("=========================================")
        try: 
            pilih_rasa = int(input("Pilih Rasa: "))
            if pilih_rasa < 0 or pilih_rasa > 3: raise ValueError
        except: input("Mohon masukkan angka.")
        else:
            if pilih_rasa == 0: break
            rasa = daftar_rasa[pilih_rasa-1] 
            hitung(rasa, level, gaji)
    n = 1
    for i in bungkus:
        if i == 0: n += 1
    if n == 4: exit(0)
    cls()
    print("=========================================")
    print("Nama Karyawan  :", nama)
    print("Level Karyawan :", level)
    print("=========================================")
    print("Rasa\t\tBungkus\tDiskon\tTambahan Gaji")
    for i in range(3):
        if i == 1:
            print("{}\t{}\t{}%\tRp{}".format(
                daftar_rasa[i], bungkus[i], int(list_diskon[i]*100), int(tambahan_gaji[i])))
        else:
            print("{}\t\t{}\t{}%\tRp{}".format(
                daftar_rasa[i], bungkus[i], int(list_diskon[i]*100), int(tambahan_gaji[i])))
    for i in tambahan_gaji:
        gaji += i
    print("\nTotal Gaji Karyawan Atas Nama {}: Rp{}".format(nama, int(gaji)))
    print("=========================================")
    input("Tekan Enter untuk keluar...")

menu()