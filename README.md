# GNO Hesaplama Aracı

Bu proje, öğrencilerin ders notlarını girerek Genel Not Ortalaması (GNO) ve Ağırlıklı Genel Not Ortalaması (AGNO) hesaplamalarını sağlayan bir Python uygulamasıdır. Ayrıca, belirli bir hedef GNO'ya ulaşmak için yeni derslerde alınması gereken ortalamayı hesaplama ve ders bilgilerini güncelleme gibi ek özellikler de sunar.

## Özellikler

- Öğrenci notlarını girme
- GNO ve AGNO hesaplama
- Hedef GNO'ya ulaşmak için gereken ortalamayı hesaplama
- Ders kredi ve puanlama bilgilerini güncelleme
- Ders ekleme ve çıkarma
- Ders notlarını ve harf karşılıklarını dosyaya kaydetme
- AGNO değişimini grafik olarak gösterme

## Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
    ```bash
    git clone https://github.com/kullaniciadi/gno-hesaplama.git
    cd gno-hesaplama
    ```

2. Gerekli Python paketlerini yükleyin:
    ```bash
    pip install matplotlib
    ```

## Kullanım
   ```bash
gnohesaplayici.py dosyasını direkt çalıştırıp gerekli ayarlamları yapıp kullanabilirsiniz.
```
### Notları Girme

Öğrenci notlarını girmek için `notlari_al` fonksiyonunu kullanın. Bu fonksiyon, kullanıcıdan her ders için notları girmesini ister ve notları bir sözlük olarak döner.

### GNO ve AGNO Hesaplama
GNO ve AGNO hesaplamak için gno_hesapla fonksiyonunu kullanın. Bu fonksiyon, öğrenci notlarını ve ders bilgilerini kullanarak GNO ve AGNO'yu hesaplar.
   ```bash
gno, agno, toplam_kredi = gno_hesapla(ogrenci_notlari, eski_agno, toplam_akts)
```
### Hedef GNO Hesaplama
Belirli bir hedef GNO'ya ulaşmak için yeni derslerde alınması gereken ortalamayı hesaplamak için hedef_gno_hesapla fonksiyonunu kullanın.

   ```bash
hedef_gno = 3.5
yeni_dersler = {
    "Mat111": {"kredi": 4, "notlar": {"Vize": 88, "Final": 92}},
    "Tur101": {"kredi": 2, "notlar": {"Vize": 84, "Final": 89}},
}
gerekli_ortalama = hedef_gno_hesapla(mevcut_gno, mevcut_kredi, hedef_gno, yeni_dersler)
print(f"Hedef GNO'ya ulaşmak için yeni derslerde alınması gereken ortalama: {gerekli_ortalama:.2f}")
```
### Ders Bilgilerini Güncelleme
Ders kredi ve puanlama bilgilerini güncellemek için ders_kredi_guncelle ve ders_puanlama_guncelle fonksiyonlarını kullanın.
   ```bash
ders_kredi_guncelle()
ders_puanlama_guncelle()
```
### Ders Ekleme ve Çıkarma
Ders eklemek veya çıkarmak için ders_duzenle fonksiyonunu kullanın.
   ```bash
ders_duzenle()
```
### Sonuçları Dosyaya Kaydetme
Ders notlarını ve harf karşılıklarını dosyaya kaydetmek için sonuclari_dosyaya_kaydet fonksiyonunu kullanın.
   ```bash
sonuclari_dosyaya_kaydet(gno, agno, ogrenci_notlari)
```
### AGNO Değişimini Grafik Olarak Gösterme
AGNO değişimini grafik olarak göstermek için agno_grafik fonksiyonunu kullanın.
   ```bash
agno_listesi = [3.0, 3.2, 3.4, 3.5]
agno_grafik(agno_listesi)
```

### Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
