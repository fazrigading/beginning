import math
import time
from math import sqrt

logo = """\t      W e l c o m e  t o 
\t   ___    ____  _____  _____ 
\t  / _ \  / ___|| ____||  ___|
\t | | | || |    |  _|  | |_   
\t | |_| || |___ | |___ |  _|  
\t  \__\_\ \____||_____||_|    

\t    Quadratic and Circle
\t      Equation Finder"""
goodbye = "Terima kasih telah menggunakan aplikasi kami.\n"
garis = 46 * "="
menu_utama = "Menu Utama:\n[1] Persamaan Kuadrat\n[2] Persamaan Lingkaran\n[8] Riwayat Seluruh Kalkulasi\n[9] Tentang Program\n[0] Keluar"
menu_kuadrat = "Menu Utama > Persamaan Kuadrat:\n[1] Rumus ABC \n[2] Diskriminan\n[3] Jumlah Akar-Akar\n[4] Hasil Kali Akar-Akar\n[5] Selisih Akar-Akar\n[8] Riwayat Kalkulasi Persamaan Kuadrat \n[9] Kembali\n[0] Keluar"
menu_lingkaran = "Menu Utama > Persamaan Lingkaran:\n[1] Nilai Jari-Jari\n[2] Nilai Titik Pusat\n[3] Letak (x, y) pada pusat 0\n[4] Letak (x, y) pada pusat (a, b)\n[5] Persamaan r pada pusat 0\n[6] Persamaan r pada pusat (a,b)\n[8] Riwayat Kalkulasi Persamaan Lingkaran\n[9] Kembali\n[0] Keluar"
salah = "Input salah!"
nilaierror = "Nilai harus angka atau desimal."
inputan_ab = []
inputan_ac = []
inputan_abc = []
riwayat_abc = []
riwayat_d = []
riwayat_jumlahakar = []
riwayat_kaliakar = []
riwayat_selisihakar = []
inputan_r = []
inputan_abr = []
inputan_xyr = []
inputan_xabyr = []
riwayat_r_abc = []
riwayat_p_ab = []
riwayat_r_p0 = []
riwayat_xy_p0 = []
riwayat_xy_pab = []
riwayat_r_pab = []

def clear():
    print("\n"*50)

def show_riwayat_p_kuadrat():
    print("a. Rumus ABC:")
    for i in range(len(riwayat_abc)):
        print("{}. {}".format(i + 1, riwayat_abc[i]))
    print("\nb. Diskriminan:")
    for i in range(len(riwayat_d)):
        print("{}. {}".format(i + 1, riwayat_d[i]))
    print("\nc. Jumlah Akar-Akar:")
    for i in range(len(riwayat_jumlahakar)):
        print("{}. {}".format(i + 1, riwayat_jumlahakar[i]))
    print("\nd. Hasil Kali Akar-Akar:")
    for i in range(len(riwayat_kaliakar)):
        print("{}. {}".format(i + 1, riwayat_kaliakar[i]))
    print("\ne. Selisih Akar-Akar:")
    for i in range(len(riwayat_selisihakar)):
        print("{}. {}".format(i + 1, riwayat_selisihakar[i]))

def show_riwayat_p_lingkaran():
    print("a. Nilai Jari-Jari:")
    for i in range(len(riwayat_r_abc)):
        print("{}. {}".format(i + 1, riwayat_r_abc[i]))
    print("\nb. Nilai Titik Pusat:")
    for i in range(len(riwayat_p_ab)):
        print("{}. {}".format(i + 1, riwayat_p_ab[i]))
    print("\nc. Letak (x, y) pada pusat 0:")
    for i in range(len(riwayat_xy_p0)):
        print("{}. {}".format(i + 1, riwayat_xy_p0[i]))
    print("\nd. Letak (x, y) pada pusat (a, b):")
    for i in range(len(riwayat_xy_pab)):
        print("{}. {}".format(i + 1, riwayat_xy_pab[i]))
    print("\ne. Persamaan r pada pusat 0:")
    for i in range(len(riwayat_r_p0)):
        print("{}. {}".format(i + 1, riwayat_r_p0[i]))
    print("\nf. Persamaan r pada pusat (a,b):")
    for i in range(len(riwayat_r_pab)):
        print("{}. {}".format(i + 1, riwayat_r_pab[i]))

def show_riwayat_keseluruhan():
    print(garis)
    print("--------------Persamaan Kuadrat--------------")
    show_riwayat_p_kuadrat()
    print("\n-------------Persamaan Lingkaran-------------")
    show_riwayat_p_lingkaran()
    print(garis)

def konfirmasi(): # Input Konfirmasi untuk Sub-Menu
    select2 = input("Kembali [9] / Keluar [0]: ")
    if select2 == '9':
        pass
    elif select2 == '0':
        bye()
    else:
        print(salah)
        konfirmasi()

def bye(): # Fungsi saat keluar
    clear()
    print(goodbye)
    exit(1)

clear() # Output Selamat Datang
print(logo)
print(garis)
print("Selamat datang di QCEF\nProgram ini dibuat oleh Kelompok 10")
print("Informatika A '20 - Universitas Mulawarman")
print(garis)
time.sleep(1.75)
while True: # Loop ini berguna untuk kembali ke Menu Utama
    clear()
    print(garis)
    print(menu_utama)
    print(garis)
    pilihan1 = input("Masukkan pilihan [0-9]\t: ")
    if pilihan1 == '1': # Pilihan 1 - Persamaan Kuadrat
        while True:
            clear()
            print(garis)
            print(menu_kuadrat)
            print(garis)
            pilihan2 = input("Masukkan pilihan [0-9]\t: ")
            if pilihan2 == '1': # Rumus ABC
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Kuadrat > Rumus ABC:")
                    print("Bentuk Umum: ax² + bx + c = 0\nDiskriminan: b² - 4ac")
                    print("Rumus ABC: (-b ± √D)/2a\nHasil: x = x1 ∧ x2")
                    print(garis)
                    try:
                        a = float(input("Masukkan nilai a\t: "))
                        b = float(input("Masukkan nilai b\t: "))
                        c = float(input("Masukkan nilai c\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        inputan_abc[0:3] = [a,b,c]
                        D = float((b**2) - (4*a*c))
                        if a == 0:
                            print("Syarat: a ≠ 0")
                            time.sleep(1)
                            pass
                        elif D > 0:
                            x1 = (-b + sqrt(D)) / 2*a
                            x2 = (-b - sqrt(D)) / 2*a
                            hasil_abc = [x1, x2]
                            riwayat_abc.append(hasil_abc)
                            print("x₁ = {:.2f} ∧ x₂ = {:.2f}".format(hasil_abc[0], hasil_abc[1]))
                            select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                            if select == '8':
                                pass
                            elif select == '9':
                                break
                            elif select == '0':
                                bye()
                            else:
                                print(salah)
                                konfirmasi()
                        elif D == 0:
                            x1 = (-b + sqrt(D)) / 2*a
                            x2 = (-b - sqrt(D)) / 2*a
                            hasil_abc = [x1, x2]
                            print("x₁ = {:.2f} ∧ x₂ = {:.2f} (D = 0)".format(hasil_abc[0], hasil_abc[1]))
                            select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                            if select == '8':
                                riwayat_abc.append(hasil_abc)
                                pass
                            elif select == '9':
                                riwayat_abc.append(hasil_abc)
                                break
                            elif select == '0':
                                bye()
                            else:
                                print(salah)
                                konfirmasi()
                        elif D < 0:
                            print("Nilai Diskriminan < 0, kedua akar tidak riil.")
                            time.sleep(1)
                            pass
            elif pilihan2 == '2': # Rumus Diskriminan
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Kuadrat > Diskriminan:\nRumus: b² - 4ac")
                    print(garis)
                    try:
                        a = float(input("Masukkan nilai a\t: "))
                        b = float(input("Masukkan nilai b\t: "))
                        c = float(input("Masukkan nilai c\t: "))
                    except:
                        print("Nilai harus angka atau desimal.")
                        time.sleep(1)
                        pass
                    else:
                        inputan_abc[0:3] = [a,b,c]
                        D = (b**2) - (4*a*c)
                        if a == 0:
                            print("Syarat: a ≠ 0")
                            time.sleep(1)
                            pass
                        elif D >= 0:
                            riwayat_d.append(D)
                            print("D = {:.2f}".format(D))
                            select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                            if select == '8':
                                pass
                            elif select == '9':
                                break
                            elif select == '0':
                                bye()
                            else:
                                print(salah)
                                konfirmasi()
                        elif D < 0:
                            print("Nilai Diskriminan ≤ 0, coba angka lainnya.")
                            time.sleep(1)
                            pass
            elif pilihan2 == '3': # Jumlah Akar-Akar
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Kuadrat > Jumlah Akar-Akar:")
                    print("Bentuk Umum: ax² + bx + c = 0\nRumus: x₁ + x₂ = -b/a")
                    print(garis)
                    try:
                        a = float(input("Masukkan nilai a\t: "))
                        b = float(input("Masukkan nilai b\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        inputan_ab[0:2] = [a,b]
                        x1_plus_x2 = -b / a
                        riwayat_jumlahakar.append(x1_plus_x2)
                        print("x₁ + x₂ = ", x1_plus_x2)
                        select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                        if select == '8':
                            pass
                        elif select == '9':
                            break
                        elif select == '0':
                            bye()
                        else:
                            print(salah)
                            konfirmasi()
            elif pilihan2 == '4': # Hasil Kali Akar-Akar
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Kuadrat > Hasil Kali Akar-Akar:")
                    print("Bentuk Umum: ax² + bx + c = 0\nRumus: x₁ . x₂ = c/a")
                    print(garis)
                    try:
                        a = float(input("Masukkan nilai a\t: "))
                        c = float(input("Masukkan nilai c\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        inputan_ac[0:2] = [a,c]
                        x1_kali_x2 = c / a
                        riwayat_kaliakar.append(x1_kali_x2)
                        print("x₁ . x₂ = ", x1_kali_x2)
                        select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                        if select == '8':
                            pass
                        elif select == '9':
                            break
                        elif select == '0':
                            bye()
                        else:
                            print(salah)
                            konfirmasi()
            elif pilihan2 == '5': # Selisih Akar-Akar
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Kuadrat > Selisih Akar-Akar:")
                    print("Bentuk Umum: ax² + bx + c = 0\nRumus: x₁ - x₂ = ±√D/a")
                    print(garis)
                    try:
                        a = float(input("Masukkan nilai a\t: "))
                        b = float(input("Masukkan nilai b\t: "))
                        c = float(input("Masukkan nilai c\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        inputan_abc[0:3] = [a,b,c]
                        D = (b**2) - (4*a*c)
                        x1_kurang_x2 = abs(math.sqrt(D)/a)
                        riwayat_selisihakar.append(x1_kurang_x2)
                        print("x₁ - x₂ = ", x1_kurang_x2)
                        select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                        if select == '8':
                            pass
                        elif select == '9':
                            break
                        elif select == '0':
                            bye()
                        else:
                            print(salah)
                            konfirmasi()
            elif pilihan2 == '8': # Tampilkan Riwayat Kuadrat
                while True:
                    clear()
                    print(garis)
                    show_riwayat_p_kuadrat()
                    print(garis)
                    select = input("Hapus [8] / Kembali [9] / Keluar [0]: ")
                    if select == '8':
                        while True:
                            select3 = input("Bagian [a-e] Kembali [9] Keluar [0]: ")
                            if select3 == 'a':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_abc):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_abc.pop(select4 - 1)
                                            break
                            elif select3 == 'b':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_d):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_d.pop(select4 - 1)
                                            break
                            elif select3 == 'c':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_jumlahakar):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_jumlahakar.pop(select4 - 1)
                                            break
                            elif select3 == 'd':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_kaliakar):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_kaliakar.pop(select4 - 1)
                                            break
                            elif select3 == 'e':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_selisihakar):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_selisihakar.pop(select4 - 1)
                                            break
                            elif select3 == '9':
                                break
                            elif select3 == '0':
                                bye()
                            else:
                                print(salah)
                                time.sleep(1)
                            break
                    elif select == '9':
                        break
                    elif select == '0':
                        bye()
                    else:
                        print(salah)
                        time.sleep(1)
            elif pilihan2 == '9': # Kembali ke Menu Awal
                break
            elif pilihan2 == '0': # Keluar
                bye()
            else: # Jika tipe Input bukan angka int atau float
                print(salah)
                time.sleep(1)
    elif pilihan1 == '2': # Pilihan 2 - Persamaan Lingkaran
        while True:
            clear()
            print(garis)
            print(menu_lingkaran)
            print(garis)
            pilihan2 = input("Masukkan pilihan [0-9]\t: ")
            if pilihan2 == '1': # Mencari nilai jari-jari
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Lingkaran > Nilai Jari-Jari:")
                    print("Rumus: r = √((¼.a)^2 + (¼.b)^2 - c)")
                    print(garis)
                    try:
                        a = float(input("Masukkan nilai a\t: "))
                        b = float(input("Masukkan nilai b\t: "))
                        c = float(input("Masukkan nilai c\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        inputan_abc[0:3] = [a,b,c]
                        hitung_ruas = (0.25*a)**2 + (0.25*b)**2 - c
                        ruas = math.sqrt(hitung_ruas)
                        if ruas > 0:
                            riwayat_r_abc.append(ruas)
                            print("r = {:.2f}".format(ruas))
                            select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                            if select == '8':
                                pass
                            elif select == '9':
                                break
                            elif select == '0':
                                bye()
                            else:
                                print(salah)
                                konfirmasi()
                        elif ruas <= 0:
                            print("Nilai Ruas ≤ 0, tidak rasional.")
                            time.sleep(1)
            elif pilihan2 == '2': # Mencari nilai titik pusat
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Lingkaran > Nilai Titik Pusat:")
                    print("Rumus: Pusat (a,b) = {½.a, ½.b}")
                    print(garis)
                    try:
                        a = float(input("Masukkan nilai a\t: "))
                        b = float(input("Masukkan nilai b\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        inputan_ab[0:2] = [a,b]
                        titik_a = 0.5*a
                        titik_b = 0.5*b
                        pusatab = [titik_a, titik_b]
                        riwayat_p_ab.append(pusatab)
                        print("Titik Pusat (a,b) = ({:.2f}, {:.2f})".format(pusatab[0], pusatab[1]))
                        select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                        if select == '8':
                            pass
                        elif select == '9':
                            break
                        elif select == '0':
                            bye()
                        else:
                            print(salah)
                            konfirmasi()
            elif pilihan2 == '3': # Mencari letak xy pusat 0
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Lingkaran > Letak x,y Pusat 0:")
                    print("Rumus Letak x,y Pusat 0: x² + y² = r²")
                    print(garis)
                    try:
                        x = int(input("Masukkan nilai x\t: "))
                        y = int(input("Masukkan nilai y\t: "))
                        r = int(input("Masukkan nilai r\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        inputan_xyr[0:3] = [x,y,r]
                        titik_xy = x**2 + y**2
                        pers_r0 = r**2
                        if titik_xy == pers_r0:
                            xy0 = "{}² + {}² = {}²".format(x, y, r)
                            print(xy0, "\nTitik ({},{}) terletak pada lingkaran".format(x, y))
                        elif titik_xy > pers_r0:
                            xy0 = "{}² + {}² > {}²".format(x, y, r)
                            print(xy0, "\nTitik ({},{}) terletak di luar lingkaran".format(x, y))
                        elif titik_xy < pers_r0:
                            xy0 = "{}² + {}² < {}²".format(x, y, r)
                            print(xy0, "\nTitik ({},{}) terletak di dalam lingkaran".format(x, y))
                        riwayat_xy_p0.append(xy0)
                        select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                        if select == '8':
                            pass
                        elif select == '9':
                            break
                        elif select == '0':
                            bye()
                        else:
                            print(salah)
                            konfirmasi()
            elif pilihan2 == '4': # Mencari letak xy pusat ab
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Lingkaran > Letak x,y Pusat (a,b):")
                    print("Rumus: (x-a)² + (y-b)² = r²")
                    print(garis)
                    try:
                        x = int(input("Masukkan nilai x\t: "))
                        a = int(input("Masukkan nilai a\t: "))
                        y = int(input("Masukkan nilai y\t: "))
                        b = int(input("Masukkan nilai b\t: "))
                        r = int(input("Masukkan nilai r\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        inputan_xabyr[0:3] = [a,b,c]
                        titik_xy_pab = (x-a)**2 + (y-b)**2
                        r_pab = r**2
                        if titik_xy_pab == r_pab:
                            xy_pab = "({}-{})² + ({}-{})² = {}²".format(x, a, y, b, r)
                            print(xy_pab, "\nTitik ({},{}) terletak pada lingkaran".format(a, b))
                        elif titik_xy_pab > r_pab:
                            xy_pab = "({}-{})² + ({}-{})² > {}²".format(x, a, y, b, r)
                            print(xy_pab, "\nTitik ({},{}) terletak di luar lingkaran".format(a, b))
                        elif titik_xy_pab < r_pab:
                            xy_pab = "({}-{})² + ({}-{})² < {}²".format(x, a, y, b, r)
                            print(xy_pab, "\nTitik ({},{}) terletak di dalam lingkaran".format(a, b))
                        riwayat_xy_pab.append(xy_pab)
                        select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                        if select == '8':
                            pass
                        elif select == '9':
                            break
                        elif select == '0':
                            bye()
                        else:
                            print(salah)
                            konfirmasi()
            elif pilihan2 == '5': # Persamaan r pada Pusat 0
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Lingkaran > Persamaan r di Pusat 0:")
                    print("Bentuk Umum: x² + y² + ax + by + c = 0")
                    print("Rumus: Pusat (0,0) = x² + y² = r²")
                    print(garis)
                    try:
                        r = float(input("Masukkan nilai r\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        pers_r0 = r**2
                        hasil_pers_r0 = "x² + y² = {}".format(pers_r0)
                        riwayat_r_p0.append(hasil_pers_r0)
                        print("Persamaan: ", hasil_pers_r0)
                        inputan_r[0:] = [r]
                        select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                        if select == '8':
                            pass
                        elif select == '9':
                            break
                        elif select == '0':
                            bye()
                        else:
                            print(salah)
                            konfirmasi()
            elif pilihan2 == '6': # Persamaan r pada Pusat a,b
                while True:
                    clear()
                    print(garis)
                    print("... > Pers. Lingkaran > Persamaan r di Pusat (a,b):")
                    print("Bentuk Umum: x² + y² + ax + by + c = 0")
                    print("Rumus: Pusat (a,b) = (x - a)² + (y - b)² = r²")
                    print(garis)
                    try:
                        a = int(input("Masukkan nilai a\t: "))
                        b = int(input("Masukkan nilai b\t: "))
                        r = int(input("Masukkan nilai r\t: "))
                    except:
                        print(nilaierror)
                        time.sleep(1)
                        pass
                    else:
                        hitung_r = r**2
                        pers_r_ab = "(x - {})² + (y - {})² = {}".format(a, b, hitung_r)
                        inputan_abr[0:] = [a,b,r]
                        riwayat_r_pab.append(pers_r_ab)
                        print("Persamaan: ", pers_r_ab)
                        select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
                        if select == '8':
                            pass
                        elif select == '9':
                            break
                        elif select == '0':
                            bye()
                        else:
                            print(salah)
                            konfirmasi()
            elif pilihan2 == '8': # Tampilkan Riwayat Lingkaran
                while True:
                    clear()
                    print(garis)
                    show_riwayat_p_lingkaran()
                    print(garis)
                    select = input("Hapus [8] / Kembali [9] / Keluar [0]: ")
                    if select == '8':
                        while True:
                            select3 = input("Bagian [a-f] Kembali [9] Keluar [0]: ")
                            if select3 == 'a':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_r_abc):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_r_abc.pop(select4 - 1)
                                            break
                            elif select3 == 'b':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_p_ab):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_p_ab.pop(select4 - 1)
                                            break
                            elif select3 == 'c':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_xy_p0):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_xy_p0.pop(select4 - 1)
                                            break
                            elif select3 == 'd':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_xy_pab):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_xy_pab.pop(select4 - 1)
                                            break
                            elif select3 == 'e':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_r_p0):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_r_p0.pop(select4 - 1)
                                            break
                            elif select3 == 'f':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_r_pab):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_r_pab.pop(select4 - 1)
                                            break
                            elif select3 == '9':
                                break
                            elif select3 == '0':
                                bye()
                            else:
                                print(salah)
                                time.sleep(1)
                            break
                    elif select == '9':
                        break
                    elif select == '0':
                        bye()
                    else:
                        print(salah)
                        time.sleep(1)
            elif pilihan2 == '9': # Kembali ke Menu Awal
                break
            elif pilihan2 == '0': # Keluar
                bye()
            else: # Jika tipe Input bukan angka int atau float
                print(salah)
                time.sleep(1)
    elif pilihan1 == '8': # Pilihan 8 - Riwayat Keseluruhan
        while True:
            clear()
            show_riwayat_keseluruhan()
            select = input("Hapus [8] / Kembali [9] / Keluar [0]: ")
            if select == '8':
                while True:
                    select2 = input("Kuadrat [1] / Lingkaran [2]: ")
                    if select2 == '1':
                        while True:
                            select3 = input("Bagian [a-e] Kembali [9] Keluar [0]: ")
                            if select3 == 'a':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_abc):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_abc.pop(select4 - 1)
                                            break
                            elif select3 == 'b':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_d):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_d.pop(select4 - 1)
                                            break
                            elif select3 == 'c':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_jumlahakar):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_jumlahakar.pop(select4 - 1)
                                            break
                            elif select3 == 'd':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_kaliakar):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_kaliakar.pop(select4 - 1)
                                            break
                            elif select3 == 'e':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_selisihakar):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_selisihakar.pop(select4 - 1)
                                            break
                            elif select3 == '9':
                                break
                            elif select3 == '0':
                                bye()
                            else:
                                print(salah)
                                time.sleep(1)
                            break
                    elif select2 == '2':
                        while True:
                            select3 = input("Bagian [a-f] Kembali [9] Keluar [0]: ")
                            if select3 == 'a':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_r_abc):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_r_abc.pop(select4 - 1)
                                            break
                            elif select3 == 'b':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_p_ab):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_p_ab.pop(select4 - 1)
                                            break
                            elif select3 == 'c':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_xy_p0):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_xy_p0.pop(select4 - 1)
                                            break
                            elif select3 == 'd':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_xy_pab):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_xy_pab.pop(select4 - 1)
                                            break
                            elif select3 == 'e':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_r_p0):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_r_p0.pop(select4 - 1)
                                            break
                            elif select3 == 'f':
                                while True:
                                    try:
                                        select4 = int(input("Hapus nomor: "))
                                    except:
                                        print(nilaierror)
                                        time.sleep(1)
                                        pass
                                    else:
                                        if select4 != len(riwayat_r_pab):
                                            print(salah)
                                            time.sleep(1)
                                            pass
                                        else:
                                            riwayat_r_pab.pop(select4 - 1)
                                            break
                            elif select3 == '9':
                                break
                            elif select3 == '0':
                                bye()
                            else:
                                print(salah)
                                time.sleep(1)
                            break
                    else:
                        print(salah)
                        time.sleep(1)
                    break
            elif select == '9':
                break
            elif select == '0':
                bye()
            else:
                print(salah)
                time.sleep(1)
    elif pilihan1 == '9': # Pilihan 9 - Tentang
        clear()
        print(garis)
        print("Program ini dibuat oleh Kelompok:\n")
        print("\t         .o    .oooo.")
        print("\t       o888   d8P'`Y8b")
        print("\t        888  888    888")
        print("\t        888  888    888")
        print("\t        888  888    888")
        print("\t        888  `88b  d88'")
        print("\t       o888o  `Y8bd8P'")
        print("\nKetua: Fazri Rahmad Nor Gading (2009106031)\nAhmad Nur Rifqi (2009106007)\nMuhammad Fajrianur (2009106040)\nInformatika A'20 - Universitas Mulawarman")
        print(garis)
        input("Tekan Enter untuk kembali: ")
    elif pilihan1 == '0': # Pilihan 0 - Keluar
        bye()
    else: # Jika input tidak sesuai
        print(salah)
        time.sleep(0.75)