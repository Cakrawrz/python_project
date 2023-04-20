# BELAJAR WHILE LOOP

"""
Perbedaan For dengan While
FOR : untuk melakukan perulangan, harus memasukkan sebuah data list
      (range)
WHILE : melakukan perulangan berdasarkan boolean, perulangan akan dieksekusi
        jika kondisi bernilai "TRUE" (akan dieksekusi terus, hingga mendapat nilai FALSE)
        (PERULANGAN BERDASARKAN KONDISI)
"""

data = ""

while data != "x":
    print("Data tereksekusi!")
    data = input("data : ")

# Kita menggunakan else untuk menampilkan kondisi FALSE yang terhenti
else:
    print("DATA HABIS")