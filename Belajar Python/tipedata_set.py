# BELAJAR TIPE DATA SET

"""
List => []  List, bisa memasukkan data yang sama
Tuple => () Tuple, datanya tidak bisa berubah (juga bisa memasukkan data yang sama)
Set => {}   Set, Datanya harus bersifat UNIK, jika datanya sama akan dihapus (jadi cuman diterima 1 data saja)
"""

"""
Penambahan Data :
list    => .append
set     => .add
tuple   =>
"""

"""
SET hanya bisa menambahkan dan mengurangi DATA,
tidak bisa mengubah Data (Tidak bisa duplikat data)
"""

mana = {"Cakra", "Wira", "Bumi","Cakra", "Wira", "Bumi"}

mana.add("Bryan")

print(mana)

mana.remove("Wira")

# Posisi index data bakal selalu berubah, setiap running ulang
# Tidak bisa mengambil data dengan index
# Caranya harus memakai for-loop
for data in mana:
    print(data)
