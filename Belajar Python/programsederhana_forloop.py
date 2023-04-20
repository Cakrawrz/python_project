# MEMBUAT PROGRAM SEDERAHANA MENGGUNAKAN for-loop, list, dan RANGE

# INI UNTUK AKSES LIST
katalog = int(input("Berapa banyak buku? "))

beli = []
sewa = []
# INI ADALAH FOR LOOP
# MENAMBAHKAN RANGE UNTUK MEMPERMUDAH
#Data dikelola dimulai dari angka "0"
for data in range(1, katalog):
    print(f"Data ke {data}")
    input_beli = int(input("Banyak buku yang dibeli : "))
    input_sewa = int(input("Banyak buku yang terjual : "))

    beli.append(input_beli)
    sewa.append(input_sewa)

print(f"Ini jumlah buku terbeli : {beli}")
print(f"Jumlah buku yang di sewa : {sewa}")