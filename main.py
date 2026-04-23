# Sistem Antrian Parkir menggunakan Queue (Array)

# Inisialisasi queue
antrian_parkir = []

# Kapasitas parkiran
kapasitas = 5

# Enqueue (kendaraan masuk)
def enqueue(kendaraan):
    if len(antrian_parkir) < kapasitas:
        antrian_parkir.append(kendaraan)
        print(f"Kendaraan {kendaraan} masuk ke parkiran.")
    else:
        print("Parkiran penuh! Tidak bisa menambah kendaraan.")

# Dequeue (kendaraan keluar)
def dequeue():
    if len(antrian_parkir) > 0:
        keluar = antrian_parkir.pop(0)
        print(f"Kendaraan {keluar} keluar dari parkiran.")
    else:
        print("Parkiran kosong!")

# Peek (lihat kendaraan paling depan)
def peek():
    if len(antrian_parkir) > 0:
        print(f"Kendaraan paling depan: {antrian_parkir[0]}")
    else:
        print("Parkiran kosong!")

# Display (tampilkan seluruh antrian)
def display():
    if len(antrian_parkir) > 0:
        print("Antrian parkir saat ini:")
        for i, kendaraan in enumerate(antrian_parkir):
            print(f"{i+1}. {kendaraan}")
    else:
        print("Parkiran kosong!")
