import math
import os
import time
from math import sqrt

show_menu1 = True
show_menu2 = True
show_choice1 = True
show_choice2 = True

# Definisikan Variabel
garis = "=============================================="
menu1 = "Menu Utama: \n1. Persegi \n2. Persegi Panjang \n3. Segitiga \n4. Lingkaran \n5. Jajaran Genjang \n6. Belah Ketupat \n7. Layang-Layang \n8. Trapesium \n9. Tentang \n0. Keluar"
menu2 = "1. Luas \n2. Keliling \n9. Kembali \n0. Keluar"
salah = "Input salah!"
nilaierror = "Nilai harus berupa angka atau desimal dengan titik."

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Input Konfirmasi untuk Menu 1
def konfirmasi1():
    select1 = input("Menu [9] / Keluar [0]\t: ")
    if select1 == '9':
        pass
    elif select1 == '0':
        bye()
    else:
        print(salah)
        konfirmasi1()

# Input Konfirmasi untuk Menu 2
def konfirmasi2():
    select2 = input("Kembali [9] / Keluar [0]: ")
    if select2 == '9':
        pass
    elif select2 == '0':
        bye()
    else:
        print(salah)
        konfirmasi2()

# Fungsi saat keluar
def bye():
    bye = "\nSampai jumpa! Semoga harimu menyenangkan ;)\n"
    print(bye)
    exit()
# Output Selamat Datang
clear()
print(garis)
print("Selamat datang di Kalkulator Bangun Datar v1.0 \nProgram ini dibuat oleh @fazrigading")
print(garis)
time.sleep(2.75)

# Loop ini berguna untuk kembali ke Menu 1
while show_menu1 == True:
    clear()
    print(garis)
    print(menu1)
    print(garis)
    while show_choice1 == True:
        choice1 = input("Masukkan pilihan [0-9]\t: ")
        # Pilihan 1 - Persegi
        if choice1 == '1':
            print("\nLuas = s x s | Keliling = 4 x s")
            s = float(input("\nMasukkan nilai sisi\t: "))
            luas = s**2
            keliling = 4*s
            square = [luas, keliling]
            # Output Hasil Perhitungan pada Rumus Persegi
            print("\nPersegi: Luas = {} | Keliling = {}\n".format(square[0], square[1]))
            # Konfirmasi
            konfirmasi1()
            break

        # Pilihan 2 - Persegi Panjang
        elif choice1 == '2':
            print("\nLuas = p x l | Keliling = 2 x (p + l)")
            p = float(input("\nMasukkan nilai panjang\t: "))
            l = float(input("Masukkan nilai lebar\t: "))
            # Rumus Persegi Panjang
            luas = p*l
            keliling = 2*(p+l)
            rectangle = [luas, keliling]
            # Output Hasil Perhitungan pada Rumus Persegi Panjang
            print("\nPersegi Panjang: Luas = {} | Keliling = {}\n".format(rectangle[0], rectangle[1]))
            # Konfirmasi
            konfirmasi1()
            break

        # Pilihan 3 - Segitiga
        elif choice1 == '3':
            # Loop ini berfungsi untuk kembali ke Menu 2
            while show_menu2 == True:
                clear()
                print(garis)
                print("Segitiga:")
                print(menu2)
                print(garis)
                choice2 = input("Masukkan pilihan [0-9]\t: ")
                # Luas Segitiga
                if choice2 == '1':
                    print("\nLuas Segitiga = (a.t)/2")
                    a = float(input("\nMasukkan nilai alas\t: "))
                    t = float(input("Masukkan nilai tinggi\t: "))
                    # Rumus Luas Segitiga
                    luas = 0.5 * a * t
                    print("\nLuas Segitiga = {}\n".format(luas))
                    # Konfirmasi
                    konfirmasi2()
                # Keliling Segitiga
                elif choice2 == '2':
                    print("\nKeliling Segitiga = a + b + c")
                    a = float(input("\nMasukkan nilai a\t: "))
                    b = float(input("Masukkan nilai b\t: "))
                    c = float(input("Masukkan nilai c\t: "))
                    keliling = a + b + c
                    print("\nKeliling Segitiga = {}\n".format(keliling))
                    # Konfirmasi
                    konfirmasi2()
                # Kembali ke Menu Awal
                elif choice2 == '9':
                    break
                # Keluar
                elif choice2 == '0':
                    bye()
                # Input selain angka
                else:
                    print(salah)
                    choice2

        # Pilihan 4 - Lingkaran
        elif choice1 == '4':
            print("\nLingkaran: Luas = pi x r x r | Keliling = 2 x pi x r")
            r = float(input("\nMasukkan nilai ruas\t: "))
            # Rumus Luas Lingkaran
            luas = math.pi * r**2
            # Rumus Keliling Lingkaran
            keliling = 2 * math.pi * r
            # Masukkan kedalam list variabel circle
            circle = [luas, keliling]
            # Formatkan isi list pada output
            print("\nLingkaran: Luas = {:.2f} | Keliling = {:.2f}\n".format(circle[0], circle[1]))
            konfirmasi1()

        # Pilihan 5 - Jajaran Genjang
        elif choice1 == '5':
            show_menu2 = True
            while show_menu2 == True:
                clear()
                print(garis)
                print("Jajaran Genjang:")
                print(menu2)
                print(garis)
                choice2 = input("Masukkan pilihan [0-9]\t: ")
                # Luas Jajaran Genjang
                if choice2 == '1':
                    print("\nLuas = a x t")
                    a = float(input("\nMasukkan nilai alas\t: "))
                    t = float(input("Masukkan nilai tinggi\t: "))
                    luas = a * t
                    print("\nLuas Jajaran Genjang = {}\n".format(luas))
                    # Konfirmasi
                    konfirmasi2()
                # Keliling Jajaran Genjang
                elif choice2 == '2':
                    print("\nKeliling = a + b + c + d")
                    a = float(input("\nMasukkan nilai a\t: "))
                    b = float(input("Masukkan nilai b\t: "))
                    c = float(input("Masukkan nilai c\t: "))
                    d = float(input("Masukkan nilai d\t: "))
                    keliling = a + b + c + d
                    print("\nKeliling Jajaran Genjang = {}\n".format(keliling))
                    # Konfirmasi
                    konfirmasi2()
                # Kembali ke Menu Awal
                elif choice2 == '9':
                    break
                # Keluar
                elif choice2 == '0':
                    bye()
                # Input selain angka
                else:
                    print(salah)
                    choice2
        
        # Pilihan 6 - Belah Ketupat
        elif choice1 == '6':
            show_menu2 = True
            while show_menu2 == True:
                clear()
                print(garis)
                print("Belah Ketupat:")
                print(menu2)
                print(garis)
                choice2 = input("Masukkan pilihan [0-9]\t: ")
                # Luas Belah Ketupat
                if choice2 == '1':
                    print("\nLuas = (d1 x d2) / 2")
                    d1 = float(input("\nMasukkan nilai d1\t: "))
                    d2 = float(input("Masukkan nilai d2\t: "))
                    luas = (d1 * d2)/2
                    print("\nLuas Belah Ketupat = {}\n".format(luas))
                    # Konfirmasi
                    konfirmasi2()
                # Keliling Belah Ketupat
                elif choice2 == '2':
                    print("\nKeliling = a + b + c + d")
                    a = float(input("\nMasukkan nilai a\t: "))
                    b = float(input("Masukkan nilai b\t: "))
                    c = float(input("Masukkan nilai c\t: "))
                    d = float(input("Masukkan nilai d\t: "))
                    keliling = a + b + c + d
                    print("\nKeliling Belah Ketupat = {}\n".format(keliling))
                    # Konfirmasi
                    konfirmasi2()
                # Kembali ke Menu Awal
                elif choice2 == '9':
                    break
                # Keluar
                elif choice2 == '0':
                    bye()
                # Input selain angka
                else:
                    print(salah)
                    choice2

        # Pilihan 7 - Layang-Layang
        elif choice1 == '7':
            show_menu2 = True
            while show_menu2 == True:
                clear()
                print(garis)
                print("Layang-Layang:")
                print(menu2)
                print(garis)
                choice2 = input("Masukkan pilihan [0-9]\t: ")
                # Luas Layang-Layang
                if choice2 == '1':
                    print("\nLuas = (d1 x d2) / 2")
                    d1 = float(input("\nMasukkan nilai d1\t: "))
                    d2 = float(input("Masukkan nilai d2\t: "))
                    luas = 0.5 * d1 * d2
                    print("\nLuas Layang-Layang = {}\n".format(luas))
                    # Konfirmasi
                    konfirmasi2()
                # Keliling Layang-Layang
                elif choice2 == '2':
                    print("\nKeliling = 2 x (a + c)")
                    a = float(input("\nMasukkan nilai a\t: "))
                    c = float(input("Masukkan nilai c\t: "))
                    keliling = 2*(a+c)
                    print("\nKeliling Layang-Layang = {}\n".format(keliling))
                    # Konfirmasi
                    konfirmasi2()
                # Kembali ke Menu Awal
                elif choice2 == '9':
                    break
                # Keluar
                elif choice2 == '0':
                    bye()
                # Input selain angka
                else:
                    print(salah)
                    choice2
        
        # Pilihan 8 - Trapesium
        elif choice1 == '8':
            show_menu2 = True
            while show_menu2 == True:
                clear()
                print(garis)
                print("Trapesium:")
                print(menu2)
                print(garis)
                choice2 = input("Masukkan pilihan [0-9]\t: ")
                # Luas Trapesium
                if choice2 == '1':
                    print("\nLuas = (a + b)/2 * t")
                    a = float(input("\nMasukkan nilai a\t: "))
                    b = float(input("Masukkan nilai b\t: "))
                    t = float(input("Masukkan nilai t\t: "))
                    luas = (a+b)/2 * t
                    print("\nLuas Trapesium = {}\n".format(luas))
                    # Konfirmasi
                    konfirmasi2()
                # Keliling Trapesium
                elif choice2 == '2':
                    print("\nKeliling = a + b + c + d")
                    a = float(input("\nMasukkan nilai a\t: "))
                    b = float(input("Masukkan nilai b\t: "))
                    c = float(input("Masukkan nilai c\t: "))
                    d = float(input("Masukkan nilai d\t: "))
                    keliling = a + b + c + d
                    print("\nKeliling Trapesium = {}\n".format(keliling))
                    # Konfirmasi
                    konfirmasi2()
                # Kembali ke Menu Awal
                elif choice2 == '9':
                    break
                # Keluar
                elif choice2 == '0':
                    bye()
                else:
                    print(salah)
                    choice2

        # Pilihan 9 - Tentang
        elif choice1 == '9':
            print("\nProgram ini dibuat oleh:\nFazri Rahmad Nor Gading (2009106031) \nInformatika A'20 \nUniversitas Mulawarman\n")
            konfirmasi1()

        # Pilihan 0 - Keluar
        elif choice1 == '0':
            bye()
        # Jika input tidak sesuai dengan yang diinginkan.
        else:
            print(salah)
            time.sleep(0.75)
        break
