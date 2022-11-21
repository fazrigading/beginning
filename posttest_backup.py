## Mengimpor library math agar dapat menghitung secara matematika.
import math
from math import sqrt

dadah = "\nSampai jumpa, semoga harimu menyenangkan ;)\n"

def kembali_ke_menu2():
    back_to_2 = input("Kembali [9] / Keluar [0]: ")
    if back_to_2 == '0':
        print(dadah)
        exit()

print("\nSelamat datang di Kalkulator Aljabar v1.0 \nProgram ini dibuat oleh @fazrigading\n")

menu0 = 1
while menu0 == 1:
    print("--------- MENU 1 ---------")
    print("1. Bangun Datar \n2. Bangun Ruang \n3. Phytagoras \n4. Persamaan Kuadrat \n0. Keluar")
    print("--------------------------")
    menu1 = input("Pilih menu [0-9]: ")
    if menu1 == '1':
        back_to_2 = '9'
        while(back_to_2 == '9'): 
            print("\n--------- MENU 2 ---------")
            print("1. Persegi \n2. Persegi Panjang \n3. Segitiga \n4. Lingkaran \n5. Jajar Genjang \n6. Belah Ketupat \n7. Layang-Layang \n8. Trapesium \n9. Kembali \n0. Keluar")
            print("--------------------------\n")

            choice1 = input("Masukkan pilihan [0-9]: ")

            # Pilihan 1 - Persegi
            if choice1 == '1':
                s = float(input("Masukkan nilai sisi: "))
                luas = s**2
                keliling = 4*s
                square = [luas, keliling]
                # Output Hasil Perhitungan pada Rumus Persegi
                print("\nPersegi: Luas = {} | Keliling = {}\n".format(square[0], square[1]))
                # Konfirmasi
                kembali_ke_menu2()

            # Pilihan 2 - Persegi Panjang
            elif choice1 == '2':
                p = float(input("Masukkan nilai panjang: "))
                l = float(input("Masukkan nilai lebar: "))
                # Rumus Persegi Panjang
                luas = p*l
                keliling = 2*(p+l)
                rectangle = [luas, keliling]
                # Output Hasil Perhitungan pada Rumus Persegi Panjang
                print("\nPersegi Panjang: Luas = {} | Keliling = {}\n".format(rectangle[0], rectangle[1]))
                # Konfirmasi
                kembali_ke_menu2()

            # Pilihan 3 - Segitiga
            elif choice1 == '3':
                print("\n--------- MENU 3 ---------")
                print("1. Luas Segitiga \n2. Keliling Segitiga \n9. Kembali \n0. Keluar")
                print("--------------------------\n")
                choice2 = input("Masukkan pilihan [0-9]: ")
                # Luas Segitiga
                if choice2 == '1':
                    a = float(input("Masukkan nilai alas: "))
                    t = float(input("Masukkan nilai tinggi: "))
                    luas = 0.5 * a * t
                    print("\nLuas Segitiga = \n", luas)
                    # Konfirmasi
                    kembali_ke_menu2()
                # Keliling Segitiga
                elif choice2 == '2':
                    a = float(input("Masukkan nilai a: "))
                    b = float(input("Masukkan nilai b: "))
                    c = float(input("Masukkan nilai c: "))
                    keliling = a + b + c
                    print("\nKeliling Segitiga = \n", keliling)
                    # Konfirmasi
                    kembali_ke_menu2()
                elif choice2 == '9':
                    break
                elif choice2 == '0':
                    print(dadah)
                    exit()

            # Pilihan 4 - Lingkaran
            elif choice1 == '4':
                r = float(input("Masukkan nilai ruas: "))
                luas = math.pi * r**2
                keliling = 2 * math.pi * r
                circle = [luas, keliling]
                print("\nLingkaran: Luas = {:.2f} | Keliling = {:.2f}\n".format(circle[0], circle[1]))
                kembali_ke_menu2()
            
            # Pilihan 5 - Jajar Genjang
            elif choice1 == '5':
                print("\n--------- MENU 3 ---------")
                print("1. Luas Jajargenjang \n2. Keliling Jajargenjang \n9. Kembali \n10. Keluar")
                print("--------------------------\n")
                choice2 = input("Masukkan pilihan [0-9]: ")
                # Luas Jajar Genjang
                if choice2 == '1':
                    a = float(input("Masukkan nilai alas: "))
                    t = float(input("Masukkan nilai tinggi: "))
                    luas = a * t
                    print("\nLuas Jajar Genjang = \n", luas)
                    # Konfirmasi
                    kembali_ke_menu2()
                # Keliling Jajar Genjang
                elif choice2 == '2':
                    a = float(input("Masukkan nilai a: "))
                    b = float(input("Masukkan nilai b: "))
                    c = float(input("Masukkan nilai c: "))
                    d = float(input("Masukkan nilai d: "))
                    keliling = a + b + c + d
                    print("\nKeliling Jajar Genjang = \n", keliling)
                    # Konfirmasi
                    kembali_ke_menu2()
                    
                elif choice2 == '9':
                    break
                elif choice2 == '0':
                    print(dadah)
                    exit()
            
            # Pilihan 6 - Belah Ketupat
            elif choice1 == '6':
                print("\n--------- MENU 3 ---------")
                print("1. Luas Belah Ketupat \n2. Keliling Belah Ketupat \n9. Kembali \n0. Keluar")
                print("--------------------------\n")
                choice2 = input("Masukkan pilihan [0-9]: ")
                # Luas Belah Ketupat
                if choice2 == '1':
                    d1 = float(input("Masukkan nilai diagonal 1: "))
                    d2 = float(input("Masukkan nilai diagonal 2: "))
                    luas = 0.5 * d1 * d2
                    print("\nLuas Belah Ketupat = \n", luas)
                    # Konfirmasi
                    kembali_ke_menu2()
                # Keliling Belah Ketupat
                elif choice2 == '2':
                    a = float(input("Masukkan nilai a: "))
                    b = float(input("Masukkan nilai b: "))
                    c = float(input("Masukkan nilai c: "))
                    d = float(input("Masukkan nilai d: "))
                    keliling = a + b + c + d
                    print("\nKeliling Belah Ketupat = \n", keliling)
                    # Konfirmasi
                    kembali_ke_menu2()
                    
                elif choice2 == '9':
                    break
                elif choice2 == '0':
                    print(dadah)
                    exit()

            # Pilihan 7 - Layang-Layang
            elif choice1 == '7':
                print("\n--------- MENU 3 ---------")
                print("1. Luas Layang-Layang \n2. Keliling Layang-Layang \n9. Kembali \n10. Keluar")
                print("------------------------\n")
                choice2 = input("Masukkan pilihan: ")
                # Luas Layang-Layang
                if choice2 == '1':
                    d1 = float(input("Masukkan nilai diagonal 1: "))
                    d2 = float(input("Masukkan nilai diagonal 2: "))
                    luas = 0.5 * d1 * d2
                    print("\nLuas Layang-Layang = \n", luas)
                    # Konfirmasi
                    kembali_ke_menu2()
                # Keliling Layang-Layang
                elif choice2 == '2':
                    a = float(input("Masukkan nilai a: "))
                    c = float(input("Masukkan nilai c: "))
                    keliling = 2*(a+c)
                    print("\nKeliling Layang-Layang = \n", keliling)
                    # Konfirmasi
                    kembali_ke_menu2()
                    
                elif choice2 == '9':
                    break
                elif choice2 == '0':
                    print(dadah)
                    exit()
            
            # Pilihan 8 - Trapesium
            elif choice1 == '8':
                print("\n--------- MENU 3 ---------")
                print("1. Luas Trapesium \n2. Keliling Trapesium \n9. Kembali \n10. Keluar")
                print("------------------------\n")
                choice2 = input("Masukkan pilihan: ")
                # Luas Trapesium
                if choice2 == '1':
                    a = float(input("Masukkan nilai a: "))
                    b = float(input("Masukkan nilai b: "))
                    t = float(input("Masukkan nilai t: "))
                    luas = (a+b)/2 * t
                    print("\nLuas Trapesium = \n", luas)
                    # Konfirmasi
                    kembali_ke_menu2()
                # Keliling Trapesium
                elif choice2 == '2':
                    a = float(input("Masukkan nilai a: "))
                    b = float(input("Masukkan nilai b: "))
                    c = float(input("Masukkan nilai c: "))
                    d = float(input("Masukkan nilai d: "))
                    keliling = a + b + c + d
                    print("\nKeliling Trapesium = \n", keliling)
                    # Konfirmasi
                    kembali_ke_menu2()
                    
                elif choice2 == '9':
                    break
                elif choice2 == '0':
                    print(dadah)
                    exit()
            
            # Pilihan 9 - Kembali ke Menu
            elif choice1 == '9':
                break
            
            # Pilihan 0 - Keluar
            elif choice1 == '0':
                print(dadah)
                exit()
            
            # Jika input tidak sesuai
            else:
                print("\nInput salah!\n")

    elif menu1 == '2':
        print("A")

    elif menu1 == '3':
        print("------------------------")
        print("1. Mencari nilai c \n2. Mencari nilai a \n3. Mencari nilai b \n9. Kembali \n0. Keluar")
        print("------------------------")
        phytagoras = math.sqrt(a**2 + b**2)
        print("")

    elif menu1 == '4':
        print("ax^2 + bx + c = 0")
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        c = float(input("Masukkan nilai c: "))

        d = ((b**2) - (4*a*c)) # menghitung nilai Diskriminan
        if d <= 0:
            print("Diskriminan tidak boleh <= 0.")
        else:
            pass
            # menghitung nilai x1 dan x2
            x1 = ((-b + math.sqrt(d)) / 2*a)
            x2 = ((-b - math.sqrt(d)) / 2*a)
            print("Himpunan Penyelesaiannya adalah {0} dan {1}".format(x1, x2))

    elif menu1 == '0':
        print(dadah)
        exit()

    else:
        print("\nInput salah!\n")