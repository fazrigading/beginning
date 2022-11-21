import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def tambah(a,b):
    return a+b
def kurang(a,b):
    return a-b
def kali(a,b):
    return a*b
def bagi(a,b):
    return a/b
def pangkat(a,b):
    return a**b
def konfirmasi():
    while True:
        konfirmasi = str(input("Apakah anda ingin mengulang? (y/n): "))
        if konfirmasi == "n":
            print("Terima kasih.")
            exit(1)
        elif konfirmasi == "y":
            print()
            break
        else:
            print("Input salah.")
clear()
print("""==============================================
Selamat Datang di Kalkulator Dasar!
Program ini dibuat oleh: Kelompok 17
Informatika '20 Universitas Mulawarman
==============================================
Operator:
1. + (Tambah)
2. - (Kurang)
3. * (Kali)
4. / (Bagi)
5. ^ (Pangkat)
==============================================""")
while True:
    try: 
        a = float(input("Angka pertama: "))
        p = str(input("Operator: "))
        b = float(input("Angka kedua: "))
    except:
        print("Nilai harus angka atau desimal.\n")
    else:
        if p == "+":
            print(a, p, b, "=", tambah(a,b))
            konfirmasi()
        elif p == "-":
            print(a, p, b, "=", kurang(a,b))
            konfirmasi()
        elif p == "*":
            print(a, p, b, "=", kali(a,b))
            konfirmasi()
        elif p == "/":
            print(a, p, b, "=", bagi(a,b))
            konfirmasi()
        elif p == "^":
            print(a, p, b, "=", pangkat(a,b))
            konfirmasi()
        else:
            print("Operator tidak tersedia.\n")