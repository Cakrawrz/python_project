# BELAJAR MEMBUAT METHOD / FUNCTION

"""
METHOD : tempat untuk menyimpan kode blok, 
         kode blok akan dieksekusi jika dibutuhkan/dipanggil
        
         Syntax Method : "def"
         contoh : def print_nama()"
                        (KODE BLOK)
"""
# dengan nilai variable kosong
nama = []

def print_nama():
    print("===============")
    for data in nama:
        print(data)

nama.append("Cakra")
print_nama()

nama.append("Wira")
print_nama()

nama.append("Bumi")
print_nama()

# Fungsi Method untuk meringkas syntax, agar lebih rapi
