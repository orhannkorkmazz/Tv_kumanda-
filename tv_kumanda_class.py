
import time
import random
class Kumanda():
    def __init__(self,tv_durum="Kapalı",kanal_listesi=["Trt","Atv","Kanal D"],mevcut_kanal="Trt",mevcut_ses=int("15")):
        self.tv_durum=tv_durum
        self.kanal_listesi=kanal_listesi
        self.mevcut_kanal=mevcut_kanal
        self.mevcut_ses=mevcut_ses
    def tv_ac(self):
        if (self.tv_durum=="Açık"):
            print("Televizyonunuz zaten açık durumda!")
        else:
            print("Tv Açılıyor..")
            self.tv_durum="Açık"
    def tv_kapa(self):
        if (self.tv_durum=="Kapalı"):
            print("Televizyonunuz zaten kapalı durumda!")
        else:
            print("Tv kapatılıyor..")
            self.tv_durum="Kapalı"
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor..")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Başarıyla eklendi..")
    def ses_durumu(self):
        while True:
            ses_giris=input("Ses azaltmak için '-' tuşuna basınız:\n Ses artırmak için '+' tuşuna basınız:\n geri dönmek için 'Q' ya basınız:")
            if (ses_giris=="-"):
                if (self.mevcut_ses!=0):
                    self.mevcut_ses -=1
                    print("Ses:",self.mevcut_ses)
            elif (ses_giris=="+"):
                if self.mevcut_ses!=32:
                    self.mevcut_ses+=1
                    print("Ses:",self.mevcut_ses)
            else:
                print("Ses ayarı güncellendi:",self.mevcut_ses)
                break
    def rastgele_kanala_gecis(self):
         rastgele=random.randint(0,len(self.kanal_listesi)-1)
         self.mevcut_kanal=self.kanal_listesi[rastgele]
         print("Geçiş yapılan kanal:",self.mevcut_kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return ("Tv durumu:{}\nMevcut kanal:{}\nKanal listesi:{}\nSes Düzeyi:{}".format(self.tv_durum,self.mevcut_kanal,self.kanal_listesi,self.mevcut_ses))
kumanda=Kumanda()
print("""
            ********** TV KUMANDASI UYGULAMASINA HOŞGELDİNİZ***********
1)TV AÇ
2)TV KAPA
3)SES AYARLARI
4)KANAL EKLE
5)KANAL SAYISI
6)RASTGELE KANALA GEÇ
7)TV BİLGİLER
8)ÇIKIŞ      
""")
while True:
    işlem=int(input("Lütfen yapmak istediğiniz işlemi seçiniz:"))
    if(işlem==1):
        kumanda.tv_ac()
    elif(işlem==2):
        kumanda.tv_kapa()
    elif(işlem==3):
        kumanda.ses_durumu()
    elif(işlem==4):
        kanal_ismi=input("Eklenecek kanalları girerken ',' kullanınız:..")
        kanal_listesi=kanal_ismi.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(işlem==5):
        print("Kanal Sayısı:",len(kumanda))
    elif(işlem==6):
        kumanda.rastgele_kanala_gecis()
    elif(işlem==7):
        print(kumanda)
    elif(işlem==8):
        print("Kumanda programından çıkışınız yapılıyor:...")
        time.sleep(1)
        print("Hoşçakalın,tekrar grüşmek dileğiyle..")
        break
    else:
        print("Lütfen belirtilen işlemleri tuşlayınız..")


    

            
        