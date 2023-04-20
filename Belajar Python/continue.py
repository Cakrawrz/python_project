# BELAJAR KATA KUNCI "CONTINUE"

"""
jika ingin menampilkan Genap saja, atau Ganjil saja
Range tidak bisa membedakan angka antara ganjil dan Genap

Dengan memanfaatkan Continue, kita bisa melewati proses yang ada
dalam looping
"""

for i in range(1, 100):
    print(i)


for data in range(1, 10):
    if data % 2 == 1:   #Nilai Genap
        continue
    print(data)