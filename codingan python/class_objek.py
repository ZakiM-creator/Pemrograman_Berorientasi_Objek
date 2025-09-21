class mobil: #membuat class mobil
    warna = "" #membuat atribut class mobil
    merk = ""
    tahun = ""

    #membuat method dari class mobil
    def maju(self): #method maju
        print(f"{self.merk} warna {self.warna} tahun {self.tahun} melaju dengan kencang") #memanggil atribut class mobil

mobil1 = mobil() #class mobil di instansiasi menjadi objek mobil1
mobil1.warna = "merah" #memberikan nilai pada atribut objek mobil1
mobil1.merk = "inova"
mobil1.tahun = 2024

mobil2 = mobil() #class mobil di instansiasi menjadi objek mobil2
mobil2.warna = "hitam" #memberikan nilai pada atribut objek mobil2
mobil2.merk = "avanza"
mobil2.tahun = 2023

mobil1.maju() #memanggil method maju dari objek mobil1
mobil2.maju() #memanggil method maju dari objek mobil2
