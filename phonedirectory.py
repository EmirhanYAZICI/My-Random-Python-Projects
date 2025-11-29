import time as tk

tel_rehberi = dict()  #içi boş bir sözlük oluşturduk

def tel_no_ekle(x):
    while True:
        print('*** Telefon Numarası Ekleme ***')
        numara_isim_al = input('Lütfen kayıt edilecek kişinin adını yazınız: ')
        numara_no_al = input('Lütfen numara giriniz:')
        adres_al= input('Adres Giriniz:')
        tk.sleep(2)
        try:
         
            kontrol = int(numara_no_al) # 1. Telefonu kontrol et

            if adres_al.isdigit():          # 1. Hata Kontrolü
                print('Hata: sayıdan oluşamaz!')
            
            elif any(harf.isdigit() for harf in numara_isim_al):#u Yeni Kod Ne Yapıyor? any(...) komutu bir "Tarayıcı" gibi çalışır. İsmin içindeki her bir harfe bakar,tru doner ve for dongusu mantıgı var
                print('Hata: İsim içinde rakam bulunamaz! (Ahmet123 gibi)')

            elif adres_al == "":            
                    print("Hata: Adres boş bırakılamaz!")
            else:                           
                x.setdefault(numara_isim_al, [numara_no_al, adres_al]) 
                print(f'{numara_isim_al} rehbere eklendi.\n')
                input('\nDevam edilsin mi ?')
                break # Döngüden çık
        
        except ValueError:
            print('Hata! Telefon Numarası sadece rakam olmalı.')
          

def tel_rehberi_goster(x:dict): # dict items sozluk oldugunu anlasılır.
    kişi_sayısı = len(x)
    print(f'Rehberde toplam {kişi_sayısı} kişi bulunmaktadır.\n')
    print('*** Telefon Rehberi ***')
    tk.sleep(2)
    for i, j in x.items(): # BU MANTIKDA ANANHTAR KEY MANTIGINA GÖRE CALISIYOR YANİ SOZLUGE GÖRE
        print(f'İsim: {i} - Telefon Numarası: {j[0]} - Adresi: {j[1]} ')
    input('\nDevam edilsinmi ?')# simdi for ile aynı hizada olunca sistemde birkac kez enteere basmak zorunda kalmayacam


def tel_no_sil(x):
    while True:
        print('*** Telefon Numarası Silme***')
        silinecek_kisi= input('Lütfen silinecek kişinin adını yazınız: (çıkış için q): ')

        if silinecek_kisi == 'Q':
            print('ANA MENÜYE DONULUYOR..\n')
            break
        if silinecek_kisi.isdigit():
            print('hata isim yerine sayı giremezsiniz..')
            continue
        if silinecek_kisi in x:
            print(f'Bulunulan kayıt: {silinecek_kisi} - {x[silinecek_kisi][0]} - {x[silinecek_kisi][1]}')

            onay =input('Bu Kaydı silmek istediğinize eminmisiniz? (E/H):').lower()
            tk.sleep(2)

            if onay.isdigit():
                print('HATA:Onay kısmına sayı giremezsin! İşlem iptal edildi.')
            elif onay in ['E','e','evet','Evet']:
                x.pop(silinecek_kisi)
                print(f'Silme işlemi tamamlandı..') 
                print(f'Güncel Rehber:{tel_rehberi}') 
                tk.sleep(1)
                print('ANA MENÜYE DONULUYOR..\n')
                tk.sleep(1)
                break
            elif onay in ['H','h','hayır','Hayır']:
                print('İşlem iptal edildi.')  
            else:
                print('Geçersiz giriş..İşlem iptal edildi.')
        
        else:
            print('Böyle bir kayıt bulunulamadı tekrar deneyin.')        
            input('\nDevam edilsinmi ?')  # onay verme anlamı katıyor.


def cikis_yap(x):
    while True:
        cıkıs=input('Çıkış yapmak istiyormusunuz? (E/H)' )
        if cıkıs.isdigit():
            print('Lütfen rakam kullanmayınız.')
        elif cıkıs in  ['E','e','evet','Evet']:
            print('Çıkış Yapılıyor ....')
            tk.sleep(2)
            exit()
        elif cıkıs in ['H','h','hayır','Hayır']:
            print('Ana Menüye Dönülüyor...')
            tk.sleep(2)
            break
        else:
            ('Geçersiz giriş..')


while True:
    print('***HOŞGELDİNİZ***')
    tk.sleep(1)
    print('***Seçim Yapınız***')
    girdi = secim_yap= input('1-No,adres ve kişi ekle\n2-Sil\n3-Rehberi gör\n4-Çıkış yap:')
    if girdi ==' ':
        print('Boş Geçmeyiniz...')
        continue
    try:
        secim_yap = int(girdi)
    except ValueError:
        print('Lütfen Sayı Giriniz Harf Girmeyiniz.')    
        continue
    if secim_yap == 1:
        tel_no_ekle(tel_rehberi)
    elif secim_yap == 2:
        tel_no_sil(tel_rehberi)
    elif secim_yap == 3:
        tel_rehberi_goster(tel_rehberi)
    elif secim_yap == 4:
        cikis_yap(tel_rehberi)   
    else:
        print('Geçersiz seçim yaptınız. Lütfen tekrar deneyiniz.\n')     

# GELİŞTİRME NOTU: Bu kod, kullanıcıların telefon numaralarını ekleyip silebileceği ve rehberi görüntüleyebileceği basit bir telefon rehberi uygulamasıdır. Kullanıcıdan alınan 
# girdilere göre işlemler gerçekleştirilir ve sonuçlar ekrana yazdırılır. VE geliştirme için hata kontrolü ve veri doğrulama eklenebilir.
# ve acık eklemeler yapacağım sonradan.bu uygulam sıfırdan yazılacak ve time imoport edilecek ve aynı zamanda silme fonksiyonu düzeltilecek
# ve ekleme fonksiyonu geliştirilecek.ve aynı zamanda adresden ekleme telefon no bulunup silme fonksiyonu eklenecek.
