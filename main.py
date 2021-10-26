"""
Aplikasi deteksi gempa terkini
"""
import Scrapping_BMKG

if __name__ == '__main__':
    print('Aplikasi utama')
    result = Scrapping_BMKG.ekstraksi_data()
    Scrapping_BMKG.tampilkan_data(result)


