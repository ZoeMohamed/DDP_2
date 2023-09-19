# Nama File : no5.py
# Pembuat : Zoe Mohamed
# Tanggal : 18 September 2023
# Deskripsi : Menentukan segitiga sembarang

# Definisi dan spesifikasi dari fungsi pengecekan segitiga sembarang bernama IsSegitigasembarang(a,b,c) adalah:
    # IsSegitigasembarang :3 integer ---> integer 
        # IsSegitigasembarang(a,b,c) menentukan apakah segitiga tersebut merupakan segitiga sembarang 
        # atau bukan,berdasar pada parameter sisi a,b,c

def IsSegitigasembarang(a:int,b:int,c:int) -> bool:
    if a!=b and a!=c and b!=c:
        return True
    else:
        return False

print(IsSegitigasembarang(15,11,12)) # True
print(IsSegitigasembarang(15,12,12)) # False
print(IsSegitigasembarang(15,15,15)) # False