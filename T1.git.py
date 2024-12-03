data_panen = {
    'lokasi1': {
        'nama lokasi': 'kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("Seluruh Data Panen:")
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data.get('nama_lokasi', data.get('nama lokasi'))}")
    for hasil, jumlah in data['hasil_panen'].items():
        print(f"  {hasil}: {jumlah} kg")
    print()

jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung dari lokasi2: {jumlah_jagung_lokasi2} kg\n")

nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}\n")

jumlah_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
jumlah_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}
print("Jumlah hasil panen padi per lokasi:", jumlah_padi)
print("Jumlah hasil panen kedelai per lokasi:", jumlah_kedelai, "\n")

print("Status Lokasi Berdasarkan Hasil Panen:")
for lokasi, data in data_panen.items():
    nama_lokasi = data.get('nama_lokasi', data.get('nama lokasi'))
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"{nama_lokasi} memerlukan perhatian khusus.")
    else:
        print(f"{nama_lokasi} dalam kondisi baik.")