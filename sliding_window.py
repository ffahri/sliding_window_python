import csv
import math
class Nokta:
	def __init__(self,x,y): #nokta sınıfı tanımladım
		self.x = x
		self.y = y
file = open("s5000.txt","r") #dışarıdan 5000 nokta için dosyayı açtım
threshold = 80             #threshold değerini seçtim
noktalar=[]                  #noktalar adında boş liste oluşturdum
for a in range (5000) :      #5000 satırı okumak için for döngüsü
    tmp = file.readline()
    x,y = tmp.split(",")    #her bir satırı virgül ile ayırıp x ve y değişkenine atadım
    x_int = int(x)
    y_int = int(y)
    tmp = Nokta(x_int,y_int)    #nokta nesnesi oluşturdum
    noktalar.append(tmp)        #bu nesneyi noktalar listesine ekledim
anomali={}                  #anomali adında boş dictionary oluşturdum
anomali_count = 0
for b in range(4989) :      #4989 seçtim çünkü windowsize + 1 kadar veriye bakmam gerekiyor
    toplam_x1 = 0
    toplam_x2 = 0
    toplam_y1 = 0
    toplam_y2 = 0
    for j in range(b,b+10):
        toplam_x1 += noktalar[j].x
        toplam_y1 += noktalar[j].y
        toplam_x2 += noktalar[j+1].x
        toplam_y2 += noktalar[j+1].y
    x1 = toplam_x1 / 10;
    y1 = toplam_y1 / 10;
    x2 = toplam_x2 / 10;
    y2 = toplam_y2 / 10;
    uzaklik = math.hypot(x1-x2,y1-y2) #öklid bağıntısı için math kütüphanesinden hazır fonksiyon
 
    if(uzaklik > threshold):
        anomali_count = anomali_count + 1
        tmpdict={} #boş bir dict oluşturdum
        tmpdict["Anomali_No"]=anomali_count
        tmpdict["Birinci_Nokta"]=str(str(str(x1) + "," + str(y1)))
        tmpdict["Ikinci_Nokta"]=str(str(str(x2) + "," + str(y2)))
        anomali[anomali_count]=tmpdict  #bu dictleri içeren başka bir dictionary oluşturdum
print("Bulunan anomali sayısı  = " + str(len(anomali)))
alanlar = ['Anomali_No', 'Birinci_Nokta','Ikinci_Nokta']
with open('AnomaliTespitleri.csv', 'w') as dosya: 
    yaz = csv.DictWriter(dosya,alanlar) #csv yazacağım dosyayı açtım
    yaz.writeheader() #alanları yazdırdım
    for a in range(1,anomali_count+1): 
        tmpdict = anomali[a] #dictionary içerisindeki temp dictleri açtım
        yaz.writerow(tmpdict) #satır olarak yazdırdım
