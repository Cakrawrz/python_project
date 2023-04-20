#Belajar Input Number
# tambahkan (f) untuk mendeklarasikan hasil String
#Input secara umum hanya menghasilkan STRING
"""
Jika ingin menampilkan input dengan tipe Integer, 
harus mendeklarasi dengan tambahkan (int)
contoh : angka = int (input ())
"""

print("Angka Pertama :")
a = input()

print("Angka Kedua :")
b = input()

hasil = a + b
print(f"{a} + {b} = {hasil}")

#Hanya menampilkan Hasil String


#Merubah kedalam Integer
print("Angka Pertama :")
a = int (input())

print("Angka Kedua :")
b = int (input())

hasil = a + b
print(f"{a} + {b} = {hasil}")

#Jadi harus menambahkan deklarasi (int sebelum tag Input())