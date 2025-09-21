import os

class Mahasiswa: # mendefinisikan kelas
    nim = '' # atribut kelas
    jurusan = '' #variabel int tidak perlu pakai petik
    nama = ''

    def belajar(self): #method #self u/ merepresentasi objek itu sendiri
        print (f'Mahasiswa atas nama {self.nama} masuk jurusan {self.jurusan} dengan nim {self.nim} sedang belajar')
        # cara memanggil mhs1.belajar()

mhs1 = Mahasiswa() # membuat objek = mhs1
mhs2 = Mahasiswa()

mhs1.nim = '345'
mhs1.jurusan = 'agama'
mhs1.nama = 'Lanang'

mhs2.nim = '987'
mhs2.jurusan = 'pendidikan'
mhs2.nama = 'Malboro'

mhs1.belajar()
mhs2.belajar()
