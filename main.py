from math_ops import tambah, kurang, kali, bagi
from strings_ops import huruf_besar

def tampilkan_menu():
    print(huruf_besar("kalkulator sederhana"))
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

def ambil_angka():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        return a, b
    except ValueError:
        print("Input harus angka!")
        return ambil_angka()

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("Terima kasih telah menggunakan kalkulator")
        break

    a, b = ambil_angka()

    if pilihan == "1":
        hasil = tambah(a, b)
    elif pilihan == "2":
        hasil = kurang(a, b)
    elif pilihan == "3":
        hasil = kali(a, b)
    elif pilihan == "4":
        hasil = bagi(a, b)
    else:
        print("Pilihan tidak valid")
        continue

    print("Hasil:", hasil)
