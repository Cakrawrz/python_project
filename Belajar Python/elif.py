"""
BELAJAR ELIF
menerima input dari user, setelah itu menampilkan input
Jika kita menggunakan ELIF, jika pilihan awal benar, maka statement 
yang lain tidak akan di eksekusi
"""

menu_pilihan = input("Silahkan Pilih menu [1-3] : ")

if menu_pilihan == "1":
    print("anda memilih menu 1")

elif menu_pilihan == "2":
    print("anda memilih menu 2")

elif menu_pilihan == "3":
    print("anda memilih menu 3")

else:
    print("menu tidak tersedia")