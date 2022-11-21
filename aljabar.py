## Mengimpor library math agar dapat menghitung secara matematika.
import math
from operator import contains
from sympy import symbols, Eq, solve

p = "Masukkan pilihan: "
s = "Tulis soal: "
x = symbols('x')
y = symbols('y')
z = symbols('z')

## Tampilan Selamat Datang
def welcome():
    print("""
Selamat Datang di Kalkulator Matematika Aljabar!
Program ini dibuat oleh:
Fazri Gading - Informatika '20 - Universitas Mulawarman
    """)

# Tampilan Menu
def print_menu():
    print(20 * "-","MENU",20 * "-")
    print("""    1. Sistem Linear
    2. Persamaan Kuadrat
    3. Persamaan Garis
    4. Phytagoras
    5. Bangun Datar
    6. Bangun Ruang""")
    print(46 * "-")

# Konfirmasi User untuk mencoba lagi
def ulang():
    ulang = str(input("Kembali ke menu (y): "))
    if ulang == str("y") or str("Y"):
        print_menu() 
    else:
        print("Terima Kasih, semoga harimu menyenangkan!")

# Rumus Sistem Linear
def sistemlinear():
    dua_variabel = Eq(a*x + b*x = c)
    print(15 * "-","Sistem Linear",16 * "-")
    print("""    1. Satu Variabel
    2. Dua Variabel
    3. Tiga Variabel    """)
    print(46 * "-")
    pilihan2 = int(input(p))
    if pilihan2 == 1:
        inputsoal = input("Ketik soal: ")
        if (inputsoal contains '+'):
            satuvariabel = Eq(a*x + b = c)
            hasil = solve(inputsoal)
            print("Nilai x = ", hasil)
        elif (inputsoal contains '-'):
            duavariabel = Eq(a*x - b = c)
            hasil = solve(duavariabel)
        else:
            ulang()
    elif pilihan2 == 2:
        inputsoal = input("Ketik soal: ")
        hasil = solve(inputsoal)
        print("Nilai xy = ", hasil)
    elif pilihan2 == 3:
        inputsoal = input("Ketik soal: ")
        hasil = solve(inputsoal)
        print(": ", hasil)
    else:
        ulang()

# Rumus Mencari Nilai X1 dan X2 pada persamaan Ax^2 + Bx + C = 0
def persamaankuadrat():
    print("ax^2 + bx + c = 0")
    a = int(input("Masukkan nilai a: "))
    b = int(input("Masukkan nilai b: "))
    c = int(input("Masukkan nilai c: "))

    # menghitung nilai Diskriminan
    d = ((b**2) - (4*a*c))

    # mendapatkan nilai x1 dan x2
    x1 = ((-b + math.sqrt(d)) / 2*a)
    x2 = ((-b - math.sqrt(d)) / 2*a)

    print("""
    Himpunan Penyelesaiannya adalah {0} dan {1}
    """.format(x1, x2))

def nilaiab():
    a = int(input("Masukkan nilai a: "))
    b = int(input("Masukkan nilai b: "))

welcome()
print_menu()

pilihan = int(input(p))
if pilihan == 1:
    sistemlinear()

elif pilihan == 2:
    persamaankuadrat()
    ulang()
    
elif pilihan == 3:
    print("""
    a. y = mx + c
    b. y - y1 = m(x - x1)
    c. 
    """)

elif pilihan == 4:
    print("c^2 = a^2 + b^2")

elif pilihan == 5:
    print(" ")
    ulang()


elif pilihan == 6:
    print(" ")
else:
    print("Input salah.")