"""
Code yang pertama kali dijalankan ketika main.py di run
"""
import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    """
    tanggal : 26 Oktober 2021
    waktu : 16:46:08 WIB
    magnitude : 5.1
    kedalaman : 92 KM
    kordinat : LU=1.51  BT=127.01
    lokasi : 67 km BaratLaut HALMAHERABARAT-MALUT
    tsunami : tidak berpotensi TSUNAMI
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        tanggalwaktu = soup.find('span', {'class': 'waktu'})
        tanggal = tanggalwaktu.text.split(', ')[0]
        waktu = tanggalwaktu.text.split(', ')[1]
        result = soup.find('div', {'class', "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren('li')
        magnitude = None
        kedalaman = None
        lintang = None
        bujur = None
        lokasi = None
        dirasakan = None
        i = 0
        for res in result:
            if i == 1:
                magnitude = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                kordinat = res.text.split(' - ')
                lintang = kordinat[0]
                bujur = kordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1
    hasil = dict()
    hasil['tanggal'] = tanggal
    hasil['waktu'] = waktu
    hasil['magnitude'] = magnitude
    hasil['kedalaman'] = kedalaman
    hasil['kordinat'] = {'lintang': lintang, 'bujur': bujur}
    hasil['lokasi'] = lokasi
    hasil['dirasakan'] = dirasakan
    return hasil


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitude']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Kordinat : Lintang ={result['kordinat']['lintang']}, Bujur= {result['kordinat']['bujur']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Skala {result['dirasakan']}")
