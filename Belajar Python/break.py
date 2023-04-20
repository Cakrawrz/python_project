# BELAJAR KATA KUNCI "BREAK"

"""
Break digunakan untuk menghentikan proses perulangan 
(tidak akan dilanjut)

Break bisa dipakai ke semua perulangan
"""

for i in range(1, 100):
    if i % 50 == 0:
        break
    print(i)

# JIKA DATA SUDAH MENCAPAO DIBAWAH 50, AKAN DIHENTIKAN

#CONTOH LAIN dengan "While"
#True adalah proses pengulangan secara terus menerus, yang bersifat benar
while True:
    data = input("Data : ")
    if data == "x":
        break
    print(data)

# Ketika data yang dimasukkan "x", akan secara otomatis berhenti