# BELAJAR NESTED LOOP
"""
LOOP AKAN MENGAMBIL DARA VARIABEL DARI list, tuple, dll
NESTED LOOP (Perulangan Bersarang) jenis perulangan yang mengizinkan pengunaan loop dalam loop

"""

for i in range(3):
    print("Perulangan luar [i] = ", i)

    for j in range(10):
        print("Perulangan dalam [i,j] = ", str(i) + ", " + str(j))


python = "python"
for item in python:
    print(item)


""""
KONSEP LOOPING NESTED
dengan EKSPRESI Outer_loop : yang menghasilkan nilai luar
Ekspresi Inner_loop : yang menghasilkan nilai dalam
Pernyataan didalam inner_loop

"""