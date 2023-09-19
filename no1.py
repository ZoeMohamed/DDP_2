# Nama File : no1.py
# Pembuat : Zoe Mohamed
# Tanggal : 18 September 2023
# Deskripsi : Menentukan hasil penjumlahan detik dari parameter jam,menit,dan detik

# Definisi dan spesifikasi dari fungsi penjumlahan total detik bernama totalDetik(jam,menit,detik) adalah:
    # totalDetik :integer [0..23],integer [0...59],integer [0...59] ---> integer 
        # totalDetik(jam,menit,detik) menentukan total detik dari parameter jam,menit,dan detik 
        # dengan menggunakan fungsi antara jamkeDetik(jam),menitkeDetik(menit), dan validasiInput(jam,menit,detik)

# menitkeDetik : 1 integer -----> integer
 # menitkeDetik(menit) mengkonversi satuan menit ke detik dengan menggunakan parameter menit

# jamkeDetik: 1 integer ---> integer
    # jamkeDetik(jam) mengkonversi satuan jam ke detik dengan menggunakan parameter jam

#validasiInput:integer [0..23],integer [0...59],integer [0...59] ---> boolean
  #validasiInput(jam,menit,detik) mengecek apakah nilai yang diinputkan sudah sesuai dengan batasan yang telah ditetapkan


# Realisasi
def totalDetik(jam:int,menit:int,detik:int):
  if validasiInput(jam,menit,detik):
    return int(jamkeDetik(jam) + menitkeDetik(menit) + detik)
  else:
      return "Terdapat Kesalahan dalam penginputan waktu Silahkan Perhatikan nilai pada penginputan waktu"
  
def menitkeDetik(menit:int) -> int:
      return (menit * 60)
    

def jamkeDetik(jam: int) -> int:
      return (jam * 3600)

def validasiInput(jam:int,menit:int,detik:int)-> bool:
    if 0<= detik <= 59 and 0<= menit <= 59 and 0<= jam <= 23:
        return True                                             

    
    else:
        return False
  
# Aplikasi
print(totalDetik(1, 2, 60))  # -> Terdapat Kesalahan dalam penginputan waktu Silahkan Perhatikan nilai pada penginputan waktu
print(totalDetik(1, 3, 5)) # -> 3785