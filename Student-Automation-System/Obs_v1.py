# -*- coding: utf-8 -*-
"""
@author: halil.durmus
"""
#%%
#import part
import csv;
import time;
#%%
#generate csv file
#import csv
#from random import randint
#
#with open('Sinif.csv', 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(["Ogrenci No", "Ad", "Soyad", "Vize1", "Vize2", "Final", "Ortalama","Not","Basari"]);
#    for i in range(50):
#        writer.writerow([12345600 + i,"Ad{x}".format(x = i+1),"Soyad{x}".format(x = i+1),randint(0, 100),randint(0, 100),randint(0, 100),0,'xx','GECTI' ]);
#%%    
#read with standard way   
#with open('Sinif.csv', 'r') as file:
#    reader = csv.reader(file)
#    for row in reader:
#        print(row)
        
#%%        
#read with pandas
#import pandas as pd
#from pandas import DataFrame
#a = pd.read_csv('Sinif.csv') 
#df = DataFrame(a);


      

#%%    
#create class structure
class Student(object):

   def __init__(self, ID, Name, Surname, V1, V2, F, average, grade, Success):
      self.ID = ID
      self.Name = Name
      self.Surname = Surname
      self.V1 = V1
      self.V2 = V2
      self.F = F
      self.average = average
      self.grade = grade
      self.Success = Success


#%%
#yeni kayıt eklemek için fonksiyon oluşturulur.
def AddNewStudent(SinifList, ID, Name, Surname, V1, V2, F, average, grade, success):
    #SinifList: eklenecek liste            

    newStudent = Student(ID, Name, Surname, V1, V2, F, average, grade, success);
    
    #listede bu öğrenci var mı kontrol et. Yoksa listeye ekle.
    for i in range(len(SinifList)):
        if newStudent.ID == int(SinifList[i].ID): #yukarıda dosyadan okurken bütün bilgileri string şeklinde okuyor 
            IsExists = True;                     #gerekli yerlerde int() komutu ile string2int dönüşümü yapmak gerekecek.
#            raise Exception('Listeye eklemeye çalıştığınız öğrenci zaten listede mevcut!'); #bunu kullanınca program tamamen kapanıyor.
            print('Exception: Listeye eklemeye çalıştığınız öğrenci zaten listede mevcut!');

            break; #varlığını tespit ettim diğerlerine bakmama gerek yok bu yüzden döngüden çıkıyorum.
        else:
            IsExists = False;
    
    if IsExists == False:
        SinifList.append(newStudent);
        print('Yeni Öğrenci Eklendi!');
        
#%%
#3-Kayıt Güncelle
#Güncellenecek öğrenciye ait ID:öğrenci no verilir, value:değişecek değer ne olacak, 
#VariableName: hangisi değişecek öğrencinin adı mı vize1 mi vs
def UpdateStudent(SinifList,ID,value,VariableName):
    IsExists = False;
    for i in range(len(SinifList)):
        if ID == int(SinifList[i].ID):
            IsExists = True;
            if VariableName == 'ID':
                SinifList[i].ID = value;
                print('Öğrenci no güncellendi!');
                break;
            elif VariableName == 'Name':
                SinifList[i].Name = value;
                print('Öğrenci adı güncellendi!');
                break;
            elif VariableName == 'SurName':
                SinifList[i].Surname = value;
                print('Öğrenci soyadı güncellendi!');
                break;
            elif VariableName == 'V1':
                SinifList[i].V1 = value;
                print('Öğrenci Vize1 notu güncellendi!');
                break;
            elif VariableName == 'V2':
                SinifList[i].V2 = value;
                print('Öğrenci Vize2 notu güncellendi!');
                break;
            elif VariableName == 'F':
                SinifList[i].F = value;
                print('Öğrenci Final notu güncellendi!');
                break;  
            else:
                print('Exception: Böyle bir değişken({x}) mevcut değil!'.format(x=VariableName));   
                #raise Exception('Böyle bir değişken({x}) mevcut değil!'.format(x=VariableName));   
                
    if IsExists == True:
        print('Güncellenen Öğrenci:')
        print([SinifList[i].ID, SinifList[i].Name, SinifList[i].Surname, SinifList[i].V1, SinifList[i].V2, SinifList[i].F]);
    else:
        #raise Exception('Böyle bir öğrenci(ID:{x}) mevcut değil!'.format(x=ID));
        print('Exception: Böyle bir öğrenci(ID:{x}) mevcut değil!'.format(x=ID));

#%%
#4-Kayıt Sil
#listeyi ve kaldırılacak öğrenciye ait numara alınır.        
def DeleteStudent(SinifList,ID):
    IsExists = False;

    for i in range(len(SinifList)):
        if ID == int(SinifList[i].ID):            
            SinifList.pop(i);#index ile listeden nesne silme.
            print('Öğrenci({x}) kaldırıldı!'.format(x=ID));
            IsExists = True;
            break;
            
    if IsExists == False:
        #raise Exception('Böyle bir öğrenci(ID:{x}) mevcut değil!'.format(x=ID));
        print('Exception: Böyle bir öğrenci(ID:{x}) mevcut değil!'.format(x=ID));


#%%
# 5-Kayıtları Listele
def PrintList(SinifList):
    print(['Öğrenci No', 'Ad', 'Soyad','Vize1', 'Vize2', 'Final', 'Ortalama', 'Harf Notu', 'Başarı']);
    for i in range(len(SinifList)):
        print([SinifList[i].ID, SinifList[i].Name, SinifList[i].Surname, SinifList[i].V1, SinifList[i].V2, SinifList[i].F, SinifList[i].average, SinifList[i].grade, SinifList[i].Success]);

#%%
#6-Sınıf Başarı Notlarını Hesapla
def CalculateGrade(SinifList):
    for i in range(len(SinifList)):
        average = round(int(SinifList[i].V1)*0.2 + int(SinifList[i].V2)*0.3 + int(SinifList[i].F)*0.5);
        SinifList[i].average = average;
        if average >= 90:
            SinifList[i].grade = 'AA';
            SinifList[i].Success = 'GECTI';
        elif (average < 90) and (average >= 85):
            SinifList[i].grade = 'BA';
            SinifList[i].Success = 'GECTI';
        elif (average < 85) and (average >= 80):
            SinifList[i].grade = 'BB';
            SinifList[i].Success = 'GECTI';
        elif (average < 80) and (average >= 75):
            SinifList[i].grade = 'CB';
            SinifList[i].Success = 'GECTI';
        elif (average < 75) and (average >= 70):
            SinifList[i].grade = 'CC';
            SinifList[i].Success = 'GECTI';            
        elif (average < 70) and (average >= 65):
            SinifList[i].grade = 'DC';
            SinifList[i].Success = 'GECTI';            
        elif (average < 65) and (average >= 60):
            SinifList[i].grade = 'DD';
            SinifList[i].Success = 'GECTI';                       
        elif (average < 60) and (average >= 50):
            SinifList[i].grade = 'FD';
            SinifList[i].Success = 'SARTLI GECTI';                        
        elif (average < 50):
            SinifList[i].grade = 'FF';
            SinifList[i].Success = 'KALDI';                        
     
#%%
def SortList(SinifList):
    def takeAverage(student):#sıralama için kural belirlenir.
        return student.average
    
    SinifList.sort(reverse=True,key=takeAverage)#student classının average değişkenine göre listeyi sırala.
  



#%%
#Print Menü:

          

out = False;
while out == False:
    
    print('MENÜ:')
    print('1-Dosyadan Oku');
    print('2-Yeni Kayıt Ekle');
    print('3-Kayıt Güncelle');
    print('4-Kayıt Sil');
    print('5-Kayıtları Listele');
    print('6-Sınıf Başarı Notlarını Hesapla');
    print('7-Kayıtları Başarı Notuna Göre Sırala');
    print('8- İstatistiki Bilgiler');
    print('9-Dosyaya Yaz'); 
    print('10-Çıkış') 
    
    girisNo = int(input("Hangi işlemi yapmak istiyorsanız ilgili numarayı giriniz: ")); 
    
    if girisNo == 10:
        print('Çıkılıyor...')
        outFalse = True;
        break;
    
    
#%%
    if girisNo == 1:        
        #1-Dosyadan Oku
        #standart yöntemle oku.
        #daha önce oluşturulmuş Student nesnesine veriler atanır ve ilgili nesne de liste eklenir.
        SinifList = [];
        
        with open('Sinif.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:      
                if row[1] != "Ad":
                    print(row)
                    student = Student(row[0],row[1],row[2],row[3],row[4],row[5], 0, 'xx', 'GECTI');#her bir veriden yeni bir student nesnesi oluştur.
                    SinifList.append(student) #oluşturulan objeyi listeye ekle.
                
    
#%%
    if girisNo == 2:                    
        #2-Yeni Kayıt Ekle
        print('Lütfen eklenecek öğrencinin bilgilerini giriniz.');
        ID = int(input("Öğrenci No: "));
        name = input("Öğrenci Adı: ");   
        surname = input("Öğrenci Soyadı: "); 
        v1 = int(input("Vize1 Notu: "));  
        v2 = int(input("Vize2 Notu: "));
        f = int(input("Final Notu: "));  
        #fonksiyonu çağır        
        AddNewStudent(SinifList,ID,name,surname,v1,v2,f,0,'xx','GECTI');
        
        
        
#%%
    if girisNo == 3:                    
       
        print('Lütfen güncellenecek öğrencinin bilgilerini giriniz.');
        ID = int(input("Öğrenci No: "));
        print("Güncellenecek Veri ne ise onu giriniz(Öğrenci No=ID, Ad=Name, Soyad=Surname, Vize1=V1, Vize2=V2, Final=F).")
        variableName = input("Güncellenecek Veri:");
        #3-Kayıt Güncelle
        #Güncellenecek öğrenciye ait ID:öğrenci no verilir, value:değişecek değer ne olacak, 
        #VariableName: hangisi değişecek öğrencinin adı mı vize1 mi vs
        if (variableName == 'V1') or (variableName == 'V2') or (variableName == 'F') or (variableName == 'ID'):
            value = int(input("Veri Ne Olacak(Örn: V1 seçtiyseniz 50 yazınız.):"));
        else:
            value = input("Veri Ne Olacak(Örn: V1=50 ise 50 yazınız.):");
        
        #ID öğrenci nolu öğrencinin variableName bilgisini value yapalım.
        UpdateStudent(SinifList,ID,value,variableName);
    
    
    
#%%
    if girisNo == 4:
        #4-Kayıt Sil
        #listeyi ve kaldırılacak öğrenciye ait numara alınır.
        #öğrenci no 12345601 olan öğrenciyi listeden silelim.
        ID = int(input("Silinecek Öğrencinin Numarası: "));
        DeleteStudent(SinifList,ID);
    
    
    #%%
    # 5-Kayıtları Listele
    if girisNo == 5:     
        PrintList(SinifList);
    
    #%%
    #6-Sınıf Başarı Notlarını Hesapla
    
    if girisNo == 6:    
        CalculateGrade(SinifList);
        PrintList(SinifList);
    
    #%%
    #7-Kayıtları başarı notuna göre sırala  
    if girisNo == 7:    
        SortList(SinifList);
        PrintList(SinifList);
    
    
    #%%
    #8-İstatistiki Bilgiler
    if girisNo == 8:
        from statistics import mean
        from statistics import stdev
        
        
        def takeAverage(student):#sıralama için kural belirlenir.
            return student.average
        
        maxGrade = max(SinifList, key=takeAverage).average; #en yüksek nota sahip öğrencinin average değişkeni.       
        print('Max Grade is:',maxGrade);
        minGrade = min(SinifList, key=takeAverage).average; #en düşük nota sahip öğrencinin average değişkeni.
        print('Min Grade is:',minGrade);
        
        averageList = [];
        for i in range(len(SinifList)):
            averageList.append(SinifList[i].average);
        
        meanGrade = mean(averageList);
        print('Mean/Average Grade is:',meanGrade);
        
        count = 0;
        for i in range(len(SinifList)):
            if SinifList[i].average > meanGrade:
                count = count + 1;
        print('Ortalama üzerindeki kişi sayısı:',count);
        print('Sınıfın başarı yüzdesi: %', 100*(count/len(SinifList)));
        
        averageList = [];
        for i in range(len(SinifList)):
            averageList.append(SinifList[i].average);
            
        std = stdev(averageList);
        print('Sınıfın standart sapması:', std);
        
        #%%
        #çan eğrisi
        import matplotlib.pyplot as plt
        import scipy.stats
        import numpy as np
        
        
        x_min = minGrade
        x_max = maxGrade
        
        mean = meanGrade 
        std = std
        
        x = np.linspace(x_min, x_max, 100)
        
        y = scipy.stats.norm.pdf(x,mean,std)
        
        plt.plot(x,y, color='coral')
        
#        # fill area 1
#        
#        pt1 = mean + std
#        plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='black')
#        
#        pt2 = mean - std
#        plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='black')
#        
#        ptx = np.linspace(pt1, pt2, 10)
#        pty = scipy.stats.norm.pdf(ptx,mean,std)
#        
#        plt.fill_between(ptx, pty, color='#0b559f', alpha='1.0')
#        
#        #----------------------------------------------------------------------------------------#
#        # fill area 2
#        
#        pt1 = mean + std
#        plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='black')
#        
#        pt2 = mean + 2.0 * std
#        plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='black')
#        
#        ptx = np.linspace(pt1, pt2, 10)
#        pty = scipy.stats.norm.pdf(ptx,mean,std)
#        
#        plt.fill_between(ptx, pty, color='#2b7bba', alpha='1.0')
#        
#        # fill area 3
#        
#        pt1 = mean - std
#        plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='black')
#        
#        pt2 = mean - 2.0 * std
#        plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='black')
#        
#        ptx = np.linspace(pt1, pt2, 10)
#        pty = scipy.stats.norm.pdf(ptx,mean,std)
#        
#        plt.fill_between(ptx, pty, color='#2b7bba', alpha='1.0')                 
#                         
#        plt.grid()
#        
#        plt.xlim(x_min,x_max)
#        plt.ylim(0,0.05)
#        
#        plt.title('Çan Eğrisi',fontsize=10)
#        
#        plt.xlabel('x')
#        plt.ylabel('y')
#        
#        plt.savefig("canegrisi.png")
        plt.show()
        
        
        #%%
        #harfnotu dağılımı
        
        
        AACount = 0;
        BACount = 0;
        BBCount = 0;
        CBCount = 0;
        CCCount = 0;
        DCCount = 0;
        DDCount = 0;
        FDCount = 0;
        FFCount = 0;
        
        for i in range(len(SinifList)):
            if SinifList[i].grade == 'AA':
                AACount = AACount + 1;
            elif SinifList[i].grade == 'BA':
                BACount = BACount + 1;                
            elif SinifList[i].grade == 'BB':
                BBCount = BBCount + 1; 
            elif SinifList[i].grade == 'CB':
                CBCount = CBCount + 1; 
            elif SinifList[i].grade == 'CC':
                BACount = CCCount + 1; 
            elif SinifList[i].grade == 'DC':
                DCCount = DCCount + 1; 
            elif SinifList[i].grade == 'DD':
                DDCount = DDCount + 1;         
            elif SinifList[i].grade == 'FD':
                FDCount = FDCount + 1;
            elif SinifList[i].grade == 'FF':
                FFCount = FFCount + 1;   
                
        fig = plt.figure()
        ax = plt.axes()
        GRADES = ('AA', 'BA', 'BB', 'CB', 'CC','DC','DD','FD','FF')
        y_pos = np.arange(len(GRADES))
        COUNTS = [AACount,BACount,BBCount,CBCount,CCCount,DCCount,DDCount,FDCount,FFCount]
        
        
        ax.barh(y_pos, COUNTS, align='center',color='Magenta')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(GRADES)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Counts')
        ax.set_title('Grades')
        
        plt.show()
        
        
    #%%
    #write csv file
    if girisNo == 9:
        print('Kaydediliyor...');
        with open('Output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Ogrenci No", "Ad", "Soyad", "Vize1", "Vize2", "Final", "Ortalama","Not","Basari"]);
            for i in range(len(SinifList)):
        #        print([SinifList[i].ID,SinifList[i].Name,SinifList[i].Surname,SinifList[i].V1,SinifList[i].V2,SinifList[i].F, SinifList[i].average, SinifList[i].grade, SinifList[i].Success])
                writer.writerow([SinifList[i].ID,SinifList[i].Name,SinifList[i].Surname,SinifList[i].V1,SinifList[i].V2,SinifList[i].F, SinifList[i].average, SinifList[i].grade, SinifList[i].Success ]);
    
    time.sleep(1);