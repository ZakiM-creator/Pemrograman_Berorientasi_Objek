class Mahasiswa: #constructor
    nama = "Agus"
    nim = 123
    jurusan = "informatika"

    def __init__(self): #constructor aja
         print(f"Mahasiswa ini bernama {self.nama} dengan nim {self.nim} jurusan {self.jurusan}")

mhs1 = Mahasiswa()
########################################################

class Mahasiswa:
     def __init__(self, nama): #constructor parameter
          self.nama = nama #variabel
          print(f"Mahasiswa ini bernama {self.nama}")

mhs1 = Mahasiswa("Agus")
#######################################################

class Mahasiswa:
     def __init__(self, jurusan = "informatika"): #constructor default value
          self.jurusan = jurusan #variabel
          print(f"Mahasiswa ini merupakan mahasiswa jurusan {self.jurusan}")

mhs1 = Mahasiswa("Bisnis Digital")
mhs2 = Mahasiswa()
#######################################################