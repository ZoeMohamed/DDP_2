# Nama File : no3.py
# Pembuat : Zoe Mohamed
# Tanggal : 18 September 2023
# Deskripsi : Menentukan segitiga sama sisi 

# Definisi dan spesifikasi dari fungsi pengecekan segitiga sama sisi bernama IsSegitigasamasisi(a,b,c) adalah:
    # Issegitigasamasisi :3 integer ---> integer 
        # IsSegitigasamasisi(a,b,c) menentukan apakah segitiga tersebut merupakan segitiga sama 
        # sisi atau bukan,berdasar pada parameter sisi a,b,c


# Realisasi
def IsSegitigasamasisi(a:int,b:int,c:int) -> bool:
    if a == b == c:
        return True
    else:
        return False

# Aplikasi
print(IsSegitigasamasisi(12,12,12)) # True
print(IsSegitigasamasisi(12,11,12)) # False
print(IsSegitigasamasisi(12,16,13)) # False