class Mahasiswa:
    def __init__(self, kampus, jurusan = "Informatika"): #constuktor multi parametet
        self.jurusan = jurusan #variabel 
        self.kampus = kampus
        print(f"Mahasiswa ini merupakan mahasiswa jurusan {self.jurusan} dari kampus {self.kampus}")

mhs1 = Mahasiswa("UIN Panjang")
mhs2 = Mahasiswa("UIN Bojong", "Bisnis Digital")

#default value dan multiple parameter bisa digabungkan