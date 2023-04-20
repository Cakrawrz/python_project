# BELAJAR METHOD PARAMETER

"""
Data yang dipanggil pada sebuah print("") disebut parameter

"""

def say_hello(nama):
    print(f"Halo {nama} ")

say_hello("cakra")
say_hello("Wira")

# Bisa dengan menambahkan 2 variable
def library(stok_barang, riwayat_sewa):
    print(f"HASIL KESELURUHAN {stok_barang} dengan {riwayat_sewa}")

library(23, "Sewa")
library(12, "Terjual")