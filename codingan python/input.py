import os # 1. Impor modul os

def clear_screen():
    """Fungsi untuk membersihkan layar konsol."""
    # Cek sistem operasi
    # 'nt' adalah untuk Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # 'posix' adalah untuk macOS dan Linux
    else:
        _ = os.sytem('clear')

# -- Contoh Penggunaan --
print("Halo, ini adalah teks sebelum layar dibersihkan.")
input("Tekan Enter untuk melanjutkan...") # Jeda program agar kita bisa lihat teksnya

# Panggil fungsi untuk membersihkan layar
clear_screen()

print("Sekarang layar sudah bersih!")