# Nama File : no2.py
# Pembuat : Zoe Mohamed
# Tanggal : 18 September 2023
# Deskripsi : Menentukan hasil penjumlahan detik dari parameter jam,menit,detik,dan am/pm

# Definisi dan spesifikasi dari fungsi penjumlahan total detik berdasar kepada am/pm bernama time_conversion_ampm_based(j,m,s,k) adalah:
    # time_conversion_ampm_based :integer [0....11],integer [0...59],integer [0...59],string ---> integer 
        # time_conversion_ampm_based(j,m,s,k)menentukan total detik dari parameter jam,menit,detik,dan am/pm
        # dengan menggunakan fungsi antara jamkeDetik(jam),menitkeDetik(menit), dan isinputValid(j,m,s,k)

# menitkeDetik : 1 integer -----> integer
 # menitkeDetik(menit) mengkonversi satuan menit ke detik dengan menggunakan parameter menit

# jamkeDetik: 1 integer ---> integer
    # jamkeDetik(jam) mengkonversi satuan jam ke detik dengan menggunakan parameter jam

#isinputValid:integer [0..23],integer [0...59],integer [0...59],string ---> boolean
  #isinputValid(j,m,s,k) mengecek apakah nilai yang diinputkan sudah sesuai dengan batasan yang telah ditetapkan


# Realisasi
def time_conversion_ampm_based(j:int,m:int,s:int,k:str):
    if isinputValid(j,m,s,k):
        if k == 'pm':
            if j == 0:
                return 12 * 3600 + menitkeDetik(m) + s
            else:
                return jamkeDetik(j) + menitkeDetik(m) +  s
        elif k == 'am':
            if j == 0 :
                return 0 * 3600 + menitkeDetik(m) + s
            else:
                return jamkeDetik(j) + menitkeDetik(m) + s
    else:
         return "Terdapat Kesalahan dalam penginputan waktu Silahkan Perhatikan nilai pada penginputan waktu"        
       

def menitkeDetik(menit:int) -> int:
      return (menit * 60)
    

def jamkeDetik(jam: int) -> int:
      return (jam * 3600)


def isinputValid(j:int,m:int,s:int,k:str) -> bool:
    if (0<= j <= 11) and (0<= m <= 59) and (0<= s<= 59) and (k == 'pm' or k == 'am'):
        return True

    else:
        return False

# Aplikasi
print(time_conversion_ampm_based(0,0,1,'axm')) # Terdapat Kesalahan dalam penginputan waktu Silahkan Perhatikan nilai pada penginputan waktu
print(time_conversion_ampm_based(0,0,1,'am')) # 1
print(time_conversion_ampm_based(0,0,1,'pm')) # 43201
