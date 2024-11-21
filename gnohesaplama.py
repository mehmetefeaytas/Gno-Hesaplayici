import matplotlib.pyplot as plt
import json

# Ders bilgileri
dersler = {
    "Ata101": {"notlar": {"Vize": 0.4, "Final": 0.6}, "kredi": 2},
    "Blg101": {"notlar": {"Vize": 0.35, "Ödev": 0.1, "Devam": 0.05, "Final": 0.5}, "kredi": 3},
    "Blg111": {"notlar": {"Vize": 0.5, "Final": 0.5}, "kredi": 3},
    "Fiz101": {"notlar": {"Vize": 0.4, "Final": 0.6}, "kredi": 3},
    "İK101": {"notlar": {"Ödev": 1.0}, "kredi": 1},
    "KİM111": {"notlar": {"Vize": 0.4, "Final": 0.6}, "kredi": 4},
    "Mat111": {"notlar": {"Vize": 0.5, "Final": 0.5}, "kredi": 5},
    "Tür101": {"notlar": {"Vize": 0.4, "Final": 0.6}, "kredi": 2},
    "Univ101": {"notlar": {"Ödev": 1.0}, "kredi": 1},
    "Univ102": {"notlar": {"Ödev": 1.0}, "kredi": 1},
    "Blg102": {"notlar": {"Vize": 0.4, "Final": 0.6}, "kredi": 2}
}

# Notlara göre harf karşılıkları ve katsayıları
harf_notlari = {
    (88, 100): ("AA", 4.0),
    (81, 87): ("BA", 3.5),
    (76, 80): ("BB", 3.0),
    (65, 75): ("CB", 2.5),
    (55, 64): ("CC", 2.0),
    (45, 54): ("DC", 1.5),
    (40, 44): ("DD", 1.0),
    (30, 39): ("FD", 0.5),
    (0, 29): ("FF", 0)
}

# Notları girme fonksiyonu
def notlari_al():
    ogrenci_notlari = {}
    for ders, bilgiler in dersler.items():
        print(f"{ders} için notlarınızı girin:")
        ders_notlari = {}
        for kategori in bilgiler["notlar"]:
            while True:
                try:
                    not_girisi = input(f"  {kategori} notu (0-100 arası veya 'G' girin, geri dönmek için 'q' girin): ")
                    if not_girisi == 'q':
                        return None
                    if not_girisi == 'G':
                        ders_notlari[kategori] = 'G'
                        break
                    not_girisi = float(not_girisi)
                    if 0 <= not_girisi <= 100:
                        ders_notlari[kategori] = not_girisi
                        break
                    else:
                        print("Geçersiz giriş! Lütfen 0 ile 100 arasında bir not girin.")
                except ValueError:
                    print("Geçersiz giriş! Lütfen sayısal bir değer girin.")
        ogrenci_notlari[ders] = ders_notlari
    return ogrenci_notlari

# Harf notunu bulma fonksiyonu
def harf_notu_bul(not_ortalamasi):
    for aralik, harf_katsayi in harf_notlari.items():
        if aralik[0] <= not_ortalamasi <= aralik[1]:
            return harf_katsayi
    return ("FF", 0)

# Ders notunu hesaplama fonksiyonu
def ders_notu_hesapla(notlar, yuzdeler):
    toplam = 0
    toplam_yuzde = 0
    for kategori, yuzde in yuzdeler.items():
        kategori = kategori.strip()  # Boşlukları temizle
        if notlar.get(kategori) != 'G':
            toplam += notlar.get(kategori, 0) * yuzde
            toplam_yuzde += yuzde
    return toplam / toplam_yuzde if toplam_yuzde > 0 else 0

# GNO ve AGNO hesaplama fonksiyonu
def gno_hesapla(ogrenci_notlari, eski_agno=None, toplam_akts=None):
    toplam_puan, toplam_kredi = 0, 0
    for ders, bilgiler in dersler.items():
        notlar = ogrenci_notlari.get(ders, {})
        yuzdeler = bilgiler["notlar"]
        kredi = bilgiler["kredi"]
        ders_notu = ders_notu_hesapla(notlar, yuzdeler)
        _, katsayi = harf_notu_bul(ders_notu)
        toplam_puan += katsayi * kredi
        toplam_kredi += kredi

    gno = toplam_puan / toplam_kredi
    if eski_agno is not None and toplam_akts is not None:
        agno = (eski_agno * toplam_akts + gno * toplam_kredi) / (toplam_akts + toplam_kredi)
        return gno, agno, toplam_kredi
    return gno, None, toplam_kredi

# Hedef GNO'ya ulaşmak için gereken ortalama hesaplama fonksiyonu
def hedef_gno_icin_ortalama_hesapla(mevcut_gno, mevcut_kredi, hedef_gno, yeni_ders_kredisi):
    gereken_toplam_puan = hedef_gno * (mevcut_kredi + yeni_ders_kredisi)
    mevcut_toplam_puan = mevcut_gno * mevcut_kredi
    yeni_ders_ortalama = (gereken_toplam_puan - mevcut_toplam_puan) / yeni_ders_kredisi
    return yeni_ders_ortalama

# Hedef GNO'ya ulaşmak için yapılması gereken GNO hesaplama aracı
def hedef_gno_hesaplama_araci():
    mevcut_gno = float(input("Mevcut GNO: "))
    mevcut_kredi = int(input("Mevcut Kredi: "))
    hedef_gno = float(input("Hedef GNO: "))
    yeni_ders_kredisi = int(input("Yeni Derslerin Toplam Kredisi: "))
    yeni_ders_ortalama = hedef_gno_icin_ortalama_hesapla(mevcut_gno, mevcut_kredi, hedef_gno, yeni_ders_kredisi)
    print(f"Hedef GNO'ya ulaşmak için yeni derslerde alınması gereken ortalama: {yeni_ders_ortalama:.2f}")

# Ders özeti raporu
def ozet_rapor(ogrenci_notlari):
    print("\nDetaylı Ders Özeti:")
    for ders, bilgiler in dersler.items():
        yuzdeler = bilgiler["notlar"]
        kredi = bilgiler["kredi"]
        notlar = ogrenci_notlari.get(ders, {})
        ders_notu = ders_notu_hesapla(notlar, yuzdeler)
        harf, katsayi = harf_notu_bul(ders_notu)
        print(f"{ders} - Ortalama Not: {ders_notu:.2f}, Harf Notu: {harf}, Katsayı: {katsayi}, Kredi: {kredi}")

# Sonuçları dosyaya kaydetme fonksiyonu
def sonuclari_dosyaya_kaydet(gno, agno, ogrenci_notlari):
    with open("not_raporu.txt", "w") as dosya:
        dosya.write("Ders Notları ve Harf Notları:\n")
        for ders, bilgiler in dersler.items():
            yuzdeler = bilgiler["notlar"]
            kredi = bilgiler["kredi"]
            notlar = ogrenci_notlari.get(ders, {})
            ders_notu = ders_notu_hesapla(notlar, yuzdeler)
            harf, katsayi = harf_notu_bul(ders_notu)
            dosya.write(f"{ders}: {ders_notu:.2f} ({harf}) - Kredi: {kredi}, Katsayı: {katsayi}\n")
        
        dosya.write(f"\nGNO: {gno:.2f}\n")
        if agno is not None:
            dosya.write(f"AGNO: {agno:.2f}\n")
        print("Sonuçlar 'not_raporu.txt' dosyasına kaydedildi.")

# AGNO grafik gösterimi
def agno_grafik(agno_listesi):
    plt.plot(agno_listesi, marker='o', linestyle='-', color='b')
    plt.title("AGNO Değişimi")
    plt.xlabel("Dönem")
    plt.ylabel("AGNO")
    plt.grid(True)
    plt.show()

# Başarı tahmini fonksiyonu
def basari_tahmini(gno, hedef_gno):
    tahmini_gno = gno * 0.7 + hedef_gno * 0.3  # Mevcut ortalamaya %70, hedefe %30 ağırlık
    print(f"Bir sonraki dönem tahmini AGNO: {tahmini_gno:.2f}")

# Ders kredi güncelleme fonksiyonu
def ders_kredi_guncelle():
    print("\n=== Ders Kredi Güncelleme ===")
    secim = input("Tüm derslerin kredilerini mi yoksa tek tek mi güncellemek istiyorsunuz? (T/Tek): ").lower()
    if secim == 't':
        for ders in dersler:
            while True:
                try:
                    yeni_kredi = input(f"{ders} için yeni kredi değeri (0 veya pozitif bir değer): ")
                    yeni_kredi = int(yeni_kredi)
                    if yeni_kredi >= 0:
                        dersler[ders]["kredi"] = yeni_kredi
                        break
                    else:
                        print("Geçersiz giriş! Lütfen 0 veya pozitif bir değer girin.")
                except ValueError:
                    print("Geçersiz giriş! Lütfen sayısal bir değer girin.")
    elif secim == 'tek':
        while True:
            print("\nMevcut Dersler ve Kredileri:")
            for ders, bilgiler in dersler.items():
                print(f"{ders}: {bilgiler['kredi']} kredi")
            ders_adi = input("\nKredisini güncellemek istediğiniz ders adı (geri dönmek için 'q' girin): ").strip()
            if ders_adi == 'q':
                break
            if ders_adi in dersler:
                while True:
                    try:
                        yeni_kredi = input(f"{ders_adi} için yeni kredi değeri (0 veya pozitif bir değer): ")
                        yeni_kredi = int(yeni_kredi)
                        if yeni_kredi >= 0:
                            dersler[ders_adi]["kredi"] = yeni_kredi
                            break
                        else:
                            print("Geçersiz giriş! Lütfen 0 veya pozitif bir değer girin.")
                    except ValueError:
                        print("Geçersiz giriş! Lütfen sayısal bir değer girin.")
            else:
                print(f"{ders_adi} dersi bulunamadı.")
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")

# Ders puanlama güncelleme fonksiyonu
def ders_puanlama_guncelle():
    print("\n=== Ders Puanlama Güncelleme ===")
    while True:
        print("\nMevcut Dersler ve Puanlamaları:")
        for ders, bilgiler in dersler.items():
            print(f"{ders}: {bilgiler['notlar']}")
        ders_adi = input("\nPuanlamasını güncellemek istediğiniz ders adı (geri dönmek için 'q' girin): ").strip()
        if ders_adi == 'q':
            break
        if ders_adi in dersler:
            yeni_yuzdeler = {}
            for kategori in dersler[ders_adi]["notlar"]:
                while True:
                    try:
                        yeni_yuzde = input(f"{kategori} yüzdesi (0-1 arası, geri dönmek için 'q' girin): ")
                        if yeni_yuzde == 'q':
                            return
                        yeni_yuzde = float(yeni_yuzde)
                        if 0 <= yeni_yuzde <= 1:
                            yeni_yuzdeler[kategori] = yeni_yuzde
                            break
                        else:
                            print("Geçersiz giriş! Lütfen 0 ile 1 arasında bir değer girin.")
                    except ValueError:
                        print("Geçersiz giriş! Lütfen sayısal bir değer girin.")
            toplam_yuzde = sum(yeni_yuzdeler.values())
            if toplam_yuzde == 1:
                dersler[ders_adi]["notlar"] = yeni_yuzdeler
                print(f"{ders_adi} için puanlamalar güncellendi.")
            else:
                print(f"{ders_adi} için yüzdelerin toplamı 1 olmalıdır. Güncelleme yapılmadı.")
        else:
            print(f"{ders_adi} dersi bulunamadı.")

# Ders düzenleme fonksiyonu
def ders_duzenle():
    while True:
        print("\n=== Ders Düzenleme ===")
        print("1. Ders Ekle")
        print("2. Ders Çıkar")
        print("3. Ders Adını Güncelle")
        print("4. Geri Dön")
        secim = input("Bir seçenek seçin: ")

        if secim == "1":
            ders_adi = input("Yeni ders adı: ").strip()
            kredi = int(input(f"{ders_adi} için kredi değeri: "))
            notlar = {}
            while True:
                kategori = input("Not kategorisi (bitirmek için 'q' girin): ").strip()
                if kategori == 'q':
                    break
                yuzde = float(input(f"{kategori} yüzdesi (0-1 arası): "))
                notlar[kategori] = yuzde
            dersler[ders_adi] = {"notlar": notlar, "kredi": kredi}
            print(f"{ders_adi} dersi eklendi.")
        elif secim == "2":
            ders_adi = input("Çıkarmak istediğiniz ders adı: ").strip()
            if ders_adi in dersler:
                del dersler[ders_adi]
                print(f"{ders_adi} dersi çıkarıldı.")
            else:
                print(f"{ders_adi} dersi bulunamadı.")
        elif secim == "3":
            eski_ders_adi = input("Güncellemek istediğiniz ders adı: ").strip()
            if eski_ders_adi in dersler:
                yeni_ders_adi = input(f"{eski_ders_adi} için yeni ders adı: ").strip()
                dersler[yeni_ders_adi] = dersler.pop(eski_ders_adi)
                print(f"{eski_ders_adi} dersinin adı {yeni_ders_adi} olarak güncellendi.")
            else:
                print(f"{eski_ders_adi} dersi bulunamadı.")
        elif secim == "4":
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

# Ders ve kredileri sıfırlama ve yenisini yazma fonksiyonu
def dersleri_sifirla():
    global dersler
    dersler = {}
    print("\n=== Ders ve Kredileri Sıfırlama ve Yeniden Yazma ===")
    while True:
        ders_adi = input("Yeni ders adı (bitirmek için 'q' girin): ").strip()
        if ders_adi == 'q':
            break
        kredi = int(input(f"{ders_adi} için kredi değeri: "))
        notlar = {}
        while True:
            kategori = input("Not kategorisi (bitirmek için 'q' girin): ").strip()
            if kategori == 'q':
                break
            yuzde = float(input(f"{kategori} yüzdesi (0-1 arası): "))
            notlar[kategori] = yuzde
        dersler[ders_adi] = {"notlar": notlar, "kredi": kredi}
    print("Dersler ve krediler sıfırlandı ve yeniden yazıldı.")

# Ders bilgilerini kaydetme fonksiyonu
def dersleri_kaydet():
    with open("dersler.json", "w") as dosya:
        json.dump(dersler, dosya, indent=4)
    print("Dersler başarıyla kaydedildi.")

# İnteraktif menü
def menu():
    agno_listesi = []
    ogrenci_notlari = {}
    while True:
        print("\n=== Ana Menü ===")
        print("1. Notları Gir")
        print("2. GNO ve AGNO Hesapla")
        print("3. Ders Özeti Görüntüle")
        print("4. Sonuçları Dosyaya Kaydet")
        print("5. AGNO Grafik Gösterimi")
        print("6. Başarı Tahmini")
        print("7. Ders Kredilerini Güncelle")
        print("8. Ders Puanlamasını Güncelle")
        print("9. Ders Düzenle")
        print("10. Dersleri Sıfırla ve Yeniden Yaz")
        print("11. Tüm Dersleri Kaydet")
        print("12. Hedef GNO Hesaplama Aracı")
        print("13. Çıkış")
        secim = input("Bir seçenek seçin: ")

        if secim == "1":
            ogrenci_notlari = notlari_al()
            if ogrenci_notlari is None:
                continue
        elif secim == "2":
            atla = input("Önceki AGNO ve Toplam AKTS girmek istiyor musunuz? (E/H): ").lower()
            if atla == 'e':
                eski_ort = float(input("Önceki AGNO: "))
                toplam_akts = int(input("Toplam AKTS: "))
                gno, agno, toplam_kredi = gno_hesapla(ogrenci_notlari, eski_ort, toplam_akts)
            else:
                gno, agno, toplam_kredi = gno_hesapla(ogrenci_notlari)
            print(f"GNO: {gno:.2f}")
            if agno is not None:
                print(f"AGNO: {agno:.2f}")
                agno_listesi.append(agno)
            hedef_gno = float(input("Hedef GNO: "))
            yeni_ders_kredisi = int(input("Yeni derslerin toplam kredisi: "))
            yeni_ders_ortalama = hedef_gno_icin_ortalama_hesapla(gno, toplam_kredi, hedef_gno, yeni_ders_kredisi)
            print(f"Hedef GNO'ya ulaşmak için yeni derslerde alınması gereken ortalama: {yeni_ders_ortalama:.2f}")
        elif secim == "3":
            ozet_rapor(ogrenci_notlari)
        elif secim == "4":
            gno, agno, _ = gno_hesapla(ogrenci_notlari)
            sonuclari_dosyaya_kaydet(gno, agno, ogrenci_notlari)
        elif secim == "5":
            agno_grafik(agno_listesi)
        elif secim == "6":
            hedef_gno = float(input("Hedef GNO: "))
            basari_tahmini(gno, hedef_gno)
        elif secim == "7":
            ders_kredi_guncelle()
        elif secim == "8":
            ders_puanlama_guncelle()
        elif secim == "9":
            ders_duzenle()
        elif secim == "10":
            dersleri_sifirla()
        elif secim == "11":
            dersleri_kaydet()
        elif secim == "12":
            hedef_gno_hesaplama_araci()
        elif secim == "13":
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

# Programı başlat
menu()
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('program_logs.log')
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# ... (rest of the code remains the same)

# Notları girme fonksiyonu
def notlari_al():
    logger.info('Notları girme fonksiyonu çağrıldı.')
    ogrenci_notlari = {}
    for ders, bilgiler in dersler.items():
        logger.info(f'{ders} için notları giriliyor.')
        print(f"{ders} için notlarınızı girin:")
        ders_notlari = {}
        for kategori in bilgiler["notlar"]:
            while True:
                try:
                    not_girisi = input(f"  {kategori} notu (0-100 arası veya 'G' girin, geri dönmek için 'q' girin): ")
                    if not_girisi == 'q':
                        logger.warning('Not girişi iptal edildi.')
                        return None
                    if not_girisi == 'G':
                        ders_notlari[kategori] = 'G'
                        break
                    not_girisi = float(not_girisi)
                    if 0 <= not_girisi <= 100:
                        ders_notlari[kategori] = not_girisi
                        break
                    else:
                        logger.error('Geçersiz not girişi.')
                        print("Geçersiz giriş! Lütfen 0 ile 100 arasında bir not girin.")
                except ValueError:
                    logger.error('Geçersiz giriş.')
                    print("Geçersiz giriş! Lütfen sayısal bir değer girin.")
        ogrenci_notlari[ders] = ders_notlari
    logger.info('Notları girme fonksiyonu başarıyla tamamlandı.')
    return ogrenci_notlari

# ... (rest of the code remains the same)

# İnteraktif menü
def menu():
    logger.info('İnteraktif menü çağrıldı.')
    agno_listesi = []
    ogrenci_notlari = {}
    while True:
        logger.info('Menü seçenekleri gösteriliyor.')
        print("\n=== Ana Menü ===")
        print("1. Notları Gir")
        print("2. GNO ve AGNO Hesapla")
        print("3. Ders Özeti Görüntüle")
        print("4. Sonuçları Dosyaya Kaydet")
        print("5. AGNO Grafik Gösterimi")
        print("6. Başarı Tahmini")
        print("7. Ders Kredilerini Güncelle")
        print("8. Ders Puanlamasını Güncelle")
        print("9. Ders Düzenle")
        print("10. Dersleri Sıfırla ve Yeniden Yaz")
        print("11. Tüm Dersleri Kaydet")
        print("12. Hedef GNO Hesaplama Aracı")
        print("13. Çıkış")
        secim = input("Bir seçenek seçin: ")

        # ... (rest of the code remains the same)