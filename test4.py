riwayat_abc = []
while True:
    print("... > Pers. Kuadrat > Rumus ABC:")
    print("Bentuk Umum: ax² + bx + c = 0\nDiskriminan: b² - 4ac")
    print("Rumus ABC: (-b ± √D)/2a\nHasil: x = x1 ∧ x2")
    try:
        a = float(input("Masukkan nilai a\t: "))
        b = float(input("Masukkan nilai b\t: "))
        c = float(input("Masukkan nilai c\t: "))
    except:
        print(nilaierror)
        time.sleep(1)
        pass
    else:
        d = float((b**2) - (4*a*c))
        if a, b, c == 0:
            print("Syarat: a ≠ 0")
            time.sleep(1)
            pass
        elif d > 0:
            x1 = (-b + sqrt(d)) / 2*a
            x2 = (-b - sqrt(d)) / 2*a
            input_abc = [a, b, c]
            hasil_abc = [x1, x2]
            print("x₁ = {:.2f} ∧ x₂ = {:.2f}".format(hasil_abc[0], hasil_abc[1]))
            select = input("Ulang [8] / Kembali [9] / Keluar [0]: ")
            if select == '8':
                pass
            elif select == '9':
                inputan_abc.append(input_abc)
                riwayat_abc.append(hasil_abc)
                break
            elif select == '0':
                bye()
            else:
                print(salah)
                konfirmasi()
print("Rumus ABC:")
for i in range(len(riwayat_abc)):
    print("{}. {}".format(i + 1, riwayat_abc[i]))
    