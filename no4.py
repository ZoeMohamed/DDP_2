# Nama File : no4.py
# Pembuat : Zoe Mohamed
# Tanggal : 18 September 2023
# Deskripsi : Menentukan segitiga sama kaki

# Definisi dan spesifikasi dari fungsi pengecekan segitiga sama kaki bernama IsSegitigasamakaki(a,b,c) adalah:
    # IsSegitigasamakaki :3 integer ---> integer 
        # IsSegitigasamakaki(a,b,c) menentukan apakah segitiga tersebut merupakan segitiga sama 
        # kaki atau bukan,berdasar pada parameter sisi a,b,c

# Realisasi
def IsSegitigasamakaki(a:int,b:int,c:int) -> bool:
    if a == b or a == c or b == c:
        return True
    else:
        return False
    
# Aplikasi
print(IsSegitigasamakaki(12,15,15)) # True
print(IsSegitigasamakaki(12,10,15)) # False
print(IsSegitigasamakaki(12,11,9))  # False