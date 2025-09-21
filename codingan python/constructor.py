class Mahasiswa:
    def __init__ (self, jurusan, kampus): #constructor multi parameter
        self.jurusan = jurusan #variabel
        self.kampus = kampus
        
        print (f'Perkenalkan saya mahasiswa dari jurusan {self.jurusan} kampus {self.kampus}') #method


mhs1 = Mahasiswa('Bisnis', 'UIN Panjang')
mhs2 = Mahasiswa ('Psikologi', 'UNSRI')



# constructor adalah method khusus yang akan dijalankan pertama kali ketika sebuah objek dibuat dari sebuah kelas. Constructor biasanya digunakan untuk menginisialisasi atribut-atribut objek tersebut.
# constructor @ methode yg bisa jalan sendiri tanpa di panggil
# self adalah parameter pertama pada method dalam sebuah kelas yang merujuk pada instance (objek) dari kelas tersebut. Self digunakan untuk mengakses atribut dan metode dari objek itu sendiri.
#default value berfungsi 