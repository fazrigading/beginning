#menu_utama = ["Menu Utama:", "[1]", "[2]", , "[9]", "[0]"]
riwayat = [1, 2, 3, 4, 5, 6, 7, 8]

def show_history():
    for i in range(len(riwayat)):
        print(riwayat[i])

show_history()
x = input("Tambah: ")
riwayat.append(x)
show_history()
