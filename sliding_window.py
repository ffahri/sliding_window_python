import csv
import math
class Nokta:
	uzaklik = 0
	def __init__(self,x,y):
		self.x = x
		self.y = y
file = open("s5000.txt","r")
threshold = 100
noktalar=[]
for a in range (5000) :
    tmp = file.readline()
    x,y = tmp.split(",")
    x_int = int(x)
    y_int = int(y)
    tmp = Nokta(x_int,y_int)
    noktalar.append(tmp)
anomali={}
anomali_count = 0
for b in range(4989) :
    ##WINDOW 1
    sum_x = noktalar[b].x +  noktalar[b+1].x +  noktalar[b+2].x +  noktalar[b+3].x +  noktalar[b+4].x +  noktalar[b+5].x +  noktalar[b+6].x +  noktalar[b+7].x +  noktalar[b+8].x +  noktalar[b+9].x +  noktalar[b+10].x
    avg_x = sum_x / 10
    sum_y = noktalar[b].y +  noktalar[b+1].y +  noktalar[b+2].y +  noktalar[b+3].y +  noktalar[b+4].x +  noktalar[b+5].x +  noktalar[b+6].x +  noktalar[b+7].x +  noktalar[b+8].x +  noktalar[b+9].x +  noktalar[b+10].x
    avg_y = sum_x / 10
    ## WINDOW2
    sum_x2 = noktalar[b+1].x +  noktalar[b+2].x +  noktalar[b+3].x +  noktalar[b+4].x +  noktalar[b+5].x +  noktalar[b+6].x +  noktalar[b+7].x +  noktalar[b+8].x +  noktalar[b+9].x +  noktalar[b+10].x +  noktalar[b+11].x
    avg_x2 = sum_x2 / 10
    sum_y2 = noktalar[b+1].y +  noktalar[b+2].y +  noktalar[b+3].y +  noktalar[b+4].y +  noktalar[b+5].x +  noktalar[b+6].x +  noktalar[b+7].x +  noktalar[b+8].x +  noktalar[b+9].x +  noktalar[b+10].x +  noktalar[b+11].x
    avg_y2 = sum_x2 / 10
    uzaklik = math.sqrt(math.pow(math.fabs(avg_x-avg_x2),2) + math.pow(math.fabs(avg_y-avg_y2),2))
    if(uzaklik > threshold):
        #print("anomali")
        #anomali.append(noktalar[b+11])
        anomali_count = anomali_count + 1
        anomali[anomali_count] = str(str(noktalar[b+11].x) + "," + str(noktalar[b+11].y))
print("Found Anomalies  = " + str(len(anomali)))

with open('lab.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, anomali.keys())
    w.writeheader()
    w.writerow(anomali)
print("'lab.csv' has been saved with values")

## 10 veri al --> avg al kontrol
