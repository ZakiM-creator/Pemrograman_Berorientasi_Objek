class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
        self.kecepatan = 0 #default mobil diam

    def maju(self, tambah=150):
        self.kecepatan += tambah
        print(f" {self.merk} {self.warna} maju dengan kecepatan {self.kecepatan} km/jam.")

    def mundur (self, kurang=35):
        if self.kecepatan - kurang < 0:
            self.kecepatan = 0
        else:
            self.kecepatan -= kurang
        print (f" {self.merk} {self.warna} mundur/berkurang kecepatan jadi {self.kecepatan} km/jam.")

    def berhenti(self):
        self.kecepatan = 0
        print(f"{self.merk} {self.warna} berhenti.")

    def info (self):
        print(f"{self.merk} {self.warna} | Kecepatan: {self.kecepatan} km/jam")

#--- Contoh Penggunaan ----
# ...existing code...
mobil1 = Mobil ("Supra GTR", "Putih")
mobil2 = Mobil ("Brio", "Ungu")

mobil1.info()
mobil2.info()

print("\n--- Simulasi Mobil 1---")
mobil1.maju(400)
mobil1.maju(80)
mobil1.mundur(30)
mobil1.berhenti()

print("\n --- Simulasi Mobil 2 ---")
mobil2.maju(700)
mobil2.mundur(500)
mobil2.info()