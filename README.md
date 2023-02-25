# Student-Automation-System
Student automation system is the registration of the student to the program, updating, deleting, listing, calculating the grade and statistical information of the student's grade in the program.

# Öğrenci Otomasyon Sistemi
•	Bu projede Python ile aşağıdaki işlemler yapılıyor.
#### MENÜ
1. Dosyadan oku
2. Yeni Kayıt Ekle
3. Kayıt Güncelle
4. Kayıt Sil
5. Kayıtları Listele
6. Sınıf Başarı Notlarını Hesapla
7. Kayıtları Başarı Notuna Göre Sırala
8. İstatistiki Bilgiler
9. Dosyaya yaz
10. Çıkış

**Projeyi nesneye yönelik programlamaya uygun olarak Sınıf, Nesne oluşturarak yazılmıştır.**

•	**1. Dosyadan Oku:** “Sinif.csv” dosyasından **OgrNo,Ad,Soyad,Vize1,Vize2,Final** formatında dosya alarak verileri sisteme alınıyor. 
Okunan her bir satırdaki veriyi object(nesne) oluşturarak List içerisinde sinif nesnelerini saklıyoruz. 
Bundan sonraki tüm işlemlerinizi List üzerinden gerçekleştiriniz. (50 veri olacak şekilde Sinif.csv dosyası oluşturuldu.)

•	**2-Yeni Kayıt Ekle:** Kullanıcıdan ilgili bilgileri alarak List ekleme yapılıyor. OgrNo tekil (unique) alandır, sistemde kayıtlı benzer 
öğrenci no girilmesi durumunda Exception-istisnai durum fırlatılır.

•	**3-Kayıt Güncelle:** Kullanıcıdan ÖğrenciNo alarak ilgili öğrencinin bilgilerini güncelleniyor. ÖğrenciNo bulunamadığı takdirde Exception-istisnai durum fırlatılır.

•	**4-Kayıt Sil:** Kullanıcıdan ÖğrenciNo alarak ilgili öğrenciyi sistemden silinir. ÖğrenciNo bulunamadığı takdirde Exception-istisnai durum fırlatılır.

•	**5-Kayıtları Listele:** Sistemde kayıtlı öğrencileri ekrana yazdır.

•	**6-Sınıf Başarı Notlarını Hesapla:** Öğrenci başarı notunu birinci ara sınavın %20si, ikinci ara sınavın %30 ve yarıyıl sonu sınavının %50’si şeklinde hesaplanmalı 
ve çıkan ortalama virgülden sonraki hane 5 ve üzeri ise yukarı, 5’den aşağı ise aşağıya doğru tam sayıya yuvarlanır. Öğrenci not ortalamasına göre ekrana harf notu 
90-100 (AA), 85-89 (BA), 80-84 (BB), 75-79 (CB), 70-74 (CC), 65-69 (DC), 60-64 (DD), 50-59(FD), 49 ve altı (FF) olarak yazıyor.

•	Başarı durumu kolonunda FF için ekrana KALDI, FD için “Şartlı Geçti” diğer durumlar için “GEÇTİ” bilgisini ekrana yazılıyor.

•	**7-Kayıtları Başarı Notuna Göre Sırala:** Öğrenci not ortalamasına göre kayıtları sıralayıp, harf notu ve başarı durumları ile birlikte sıralı bir şekilde ekrana yansıtılır.

•	**8-İstatistiki Bilgiler:** Öğrencilerin başarı not ortalamasına göre en yüksek başarı notu en düşük başarı notu, sınıf ortalaması, 
ortalama üzerinde olan kişi sayısı (sınıfın başarı yüzdesi) ve standart sapma bilgilerini ekranda değerleri görebilirsiniz. 
(Python-İstatistik kütüphanelerinden faydalanıyorum)

• Sınıfın çan eğrisi grafiğini ekrana yazdırıyorum. (Matplotlib)

• Sınıftaki harf notu dağılımlarını (AA-5, BB-15, BA-10 gibi chart grafik ile gösteriyorum) (Matplotlib)

•	**9- Dosyaya yaz:** Sistemdeki kayıtlı öğrencileri başarı durumlarına göre sıralı bir şekilde Output.csv dosyasına yazdılırılır.

•	**Python Pandas kullanarak DataFrame ile gerçekleşmiştir. Obs_v2.py şeklinde yazılmıştır. Bu bölümde dosyadan okunan veriler üzerinden pandas ile veri manüpülasyonu 
üzerine işlemler gerçekleşmiştir.**



