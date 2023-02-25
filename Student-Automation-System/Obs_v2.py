# -*- coding: utf-8 -*-
"""
@author: halil.durmus
"""


import time
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
#create class structure
#******pandas sayesinde verileri çekmek için class yapısına ihtiyaç yok.******
#class Student(object):
#
#   def __init__(self, ID, Name, Surname, V1, V2, F, average, grade, Success):
#      self.ID = ID
#      self.Name = Name
#      self.Surname = Surname
#      self.V1 = V1
#      self.V2 = V2
#      self.F = F
#      self.average = average
#      self.grade = grade
#      self.Success = Success
   
#%%
#2-Yeni Kayıt Ekle
#yeni kayıt eklemek için fonksiyon oluşturulur.
def AddNewStudent(SinifList, ID, Name, Surname, V1, V2, F, average, grade, success):
    #SinifList: eklenecek liste            

    newStudent = pd.DataFrame([[ID, Name, Surname, V1, V2, F, average, grade, success]],columns = SinifList.columns);
    
    #listede bu öğrenci var mı kontrol et. Yoksa listeye ekle.
    for i in range(len(SinifList)):
        if newStudent.iloc[0]['Ogrenci No'] == SinifList.iloc[i]['Ogrenci No']: #iloc ile istenilen indexe ait istenilen col okunabilir. 
            IsExists = True;                     
#            raise Exception('Listeye eklemeye çalıştığınız öğrenci zaten listede mevcut!');
            print('Exception: Listeye eklemeye çalıştığınız öğrenci zaten listede mevcut!');
            break; #varlığını tespit ettim diğerlerine bakmama gerek yok bu yüzden döngüden çıkıyorum.
        else:
            IsExists = False;
    
    if IsExists == False:
        SinifList = SinifList.append(newStudent);
        print('Yeni Öğrenci Eklendi!');
    return SinifList;

#%%
#3-Kayıt Güncelle
#Güncellenecek öğrenciye ait ID:öğrenci no verilir, value:değişecek değer ne olacak, 
#VariableName: hangisi değişecek öğrencinin adı mı vize1 mi vs   
def UpdateStudent(SinifList,ID,value,VariableName):
        s = pd.Series(SinifList['Ogrenci No']); # s ile öğrenci numaraları seçilir.
        
        if (ID in s.unique()) == False :#unique ile kontrol edilebilir liste haline getirilir.
#             raise Exception('Böyle bir öğrenci(ID:{x}) mevcut değil!'.format(x=ID));
             print('Exception: Böyle bir öğrenci(ID:{x}) mevcut değil!'.format(x=ID));
             exit;
                
        if (VariableName in SinifList.columns) == False :#column'da böyle bir değişken var mı yok mu kontrol edilir.
#             raise Exception('Böyle bir değer(ID:{x}) mevcut değil!'.format(x=VariableName));
             print('Exception: Böyle bir değişken({x}) mevcut değil!'.format(x=VariableName));
             exit;  
        
        idx = SinifList[SinifList['Ogrenci No']==ID].index.values.astype(int)[0];
        SinifList.loc[idx, VariableName] = value;
             
        #SinifList = SinifList[VariableName].replace({ID:value},inplace=True);    
        print(VariableName,' güncellendi!');
        return SinifList;
        
#%%
#4-Kayıt Sil
#listeyi ve kaldırılacak öğrenciye ait numara alınır.
def DeleteStudent(SinifList,ID):
        s = pd.Series(SinifList['Ogrenci No']); # s ile öğrenci numaraları seçilir.
        
        if (ID in s.unique()) == False :#unique ile kontrol edilebilir liste haline getirilir.
#             raise Exception('Böyle bir öğrenci(ID:{x}) mevcut değil!'.format(x=ID));
             print('Exception: Böyle bir öğrenci(ID:{x}) mevcut değil!'.format(x=ID));
             exit;
        
        SinifList = SinifList[SinifList['Ogrenci No'] != ID];
        
        
        print('Öğrenci listeden silindi!');
        return SinifList;
    
#%%
# 5-Kayıtları Listele

def PrintList(SinifList):
    print(SinifList);
    
#%%
#6-Sınıf Başarı Notlarını Hesapla
def CalculateGrade(SinifList):
    SinifList['Ortalama'] = round(0.2*SinifList['Vize1'] + 0.3*SinifList['Vize2']  + 0.5*SinifList['Final']); 
    
    for i in range(len(SinifList)):
        if SinifList.iloc[i]['Ortalama'] >= 90:
            SinifList.loc[i,'Not'] = 'AA';
            SinifList.loc[i,'Basari'] = 'GECTI';
        elif (SinifList.iloc[i]['Ortalama'] < 90) and (SinifList.iloc[i]['Ortalama'] >= 85):
            SinifList.loc[i,'Not'] = 'BA';
            SinifList.loc[i,'Basari'] = 'GECTI';
        elif (SinifList.iloc[i]['Ortalama'] < 85) and (SinifList.iloc[i]['Ortalama'] >= 80):
            SinifList.loc[i,'Not'] = 'BB';
            SinifList.loc[i,'Basari'] = 'GECTI';
        elif (SinifList.iloc[i]['Ortalama'] < 80) and (SinifList.iloc[i]['Ortalama'] >= 75):
            SinifList.loc[i,'Not'] = 'CB';
            SinifList.loc[i,'Basari'] = 'GECTI';
        elif (SinifList.iloc[i]['Ortalama'] < 75) and (SinifList.iloc[i]['Ortalama'] >= 70):
            SinifList.loc[i,'Not'] = 'CC';
            SinifList.loc[i,'Basari'] = 'GECTI';            
        elif (SinifList.iloc[i]['Ortalama'] < 70) and (SinifList.iloc[i]['Ortalama'] >= 65):
            SinifList.loc[i,'Not'] = 'DC';
            SinifList.loc[i,'Basari'] = 'GECTI';            
        elif (SinifList.iloc[i]['Ortalama'] < 65) and (SinifList.iloc[i]['Ortalama'] >= 60):
            SinifList.loc[i,'Not'] = 'DD';
            SinifList.loc[i,'Basari'] = 'GECTI';                       
        elif (SinifList.iloc[i]['Ortalama'] < 60) and (SinifList.iloc[i]['Ortalama'] >= 50):
            SinifList.loc[i,'Not'] = 'FD';
            SinifList.loc[i,'Basari'] = 'SARTLI GECTI';                        
        elif (SinifList.iloc[i]['Ortalama'] < 50):
            SinifList.loc[i,'Not'] = 'FF';
            SinifList.loc[i,'Basari'] = 'KALDI'; 
            

            
#%%
#7-Kayıtları başarı notuna göre sırala
def SortList(SinifList):
    SinifList.sort_values(by=['Ortalama'], ascending=False, inplace=True)

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
        #pandas ile oku.
        #daha önce oluşturulmuş Sinif.csv okunur ve liste direkt pandas tarafından oluşturulur.
        import pandas as pd
        from pandas import DataFrame
        
        a = pd.read_csv('Sinif.csv') 
        SinifList = DataFrame(a);
        print(SinifList);
    
    #%%
    #2-Yeni Kayıt Ekle
    #yeni kayıt eklemek için fonksiyon oluşturulur.
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
        SinifList = AddNewStudent(SinifList,ID,name,surname,v1,v2,f,0,'xx','GECTI');#bu öğrenci listede mevcut
 
    
    
    
    #%%
    if girisNo == 3:
    #3-Kayıt Güncelle
    #Güncellenecek öğrenciye ait ID:öğrenci no verilir, value:değişecek değer ne olacak, 
    #VariableName: hangisi değişecek öğrencinin adı mı vize1 mi vs         
        print('Lütfen güncellenecek öğrencinin bilgilerini giriniz.');
        ID = int(input("Öğrenci No: "));
        print("Güncellenecek Veri ne ise onu giriniz(Ogrenci No, Ad, Soyad, Vize1, Vize2, Final).")
        variableName = input("Güncellenecek Veri:");
        #3-Kayıt Güncelle
        #Güncellenecek öğrenciye ait ID:öğrenci no verilir, value:değişecek değer ne olacak, 
        #VariableName: hangisi değişecek öğrencinin adı mı vize1 mi vs
        if (variableName == 'Vize1') or (variableName == 'Vize2') or (variableName == 'Final') or (variableName == 'Ogrenci No'):
            value = int(input("Veri Ne Olacak(Örn: Vize1 seçtiyseniz 50 yazınız.):"));
        else:
            value = input("Veri Ne Olacak(Örn: V1=50 ise 50 yazınız.):");            
    
        #ID öğrenci nolu öğrencinin variableName bilgisini value yapalım.
        SinifList = UpdateStudent(SinifList,ID,value,variableName);
    
    
    #%%
    if girisNo == 4:
        #4-Kayıt Sil
        #listeyi ve kaldırılacak öğrenciye ait numara alınır.
        #öğrenci no 12345601 olan öğrenciyi listeden silelim.
        ID = int(input("Silinecek Öğrencinin Numarası: "));
        SinifList = DeleteStudent(SinifList,ID);

    
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
    if girisNo == 8:    
        #8-İstatistiki Bilgiler
        from statistics import mean
        from statistics import stdev
        
        
        maxGrade = max(SinifList['Ortalama']);
        #veya
        maxGrade = SinifList['Ortalama'].max();
        print('Max Grade is:',maxGrade);
        
        minGrade = min(SinifList['Ortalama']);
        #veya
        minGrade = SinifList['Ortalama'].min();
        print('Min Grade is:',minGrade);
        
        meanGrade = sum(SinifList['Ortalama'])/len(SinifList);
        #veya
        meanGrade = SinifList['Ortalama'].mean();
        print('Mean/Average Grade is:',meanGrade);
        
        count = sum(SinifList['Ortalama'] >= meanGrade)
        print('Ortalama üzerindeki kişi sayısı:',count);
        print('Sınıfın başarı yüzdesi: %', 100*(count/len(SinifList)));
        
        std = stdev(SinifList['Ortalama']);
        print('Sınıfın standart sapması:', std);
        
        #%%
        #çan eğrisi
        import matplotlib.pyplot as plt
        import scipy.stats
        import numpy as np
        
        
        x_min = minGrade
        x_max = maxGrade
        
        mean1 = meanGrade 
        std = std
        
        x = np.linspace(x_min, x_max, 100)
        
        y = scipy.stats.norm.pdf(x,mean1,std)
        
        plt.plot(x,y, color='coral')
        
    #    # fill area 1
    #    
    #    pt1 = mean + std
    #    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='black')
    #    
    #    pt2 = mean - std
    #    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='black')
    #    
    #    ptx = np.linspace(pt1, pt2, 10)
    #    pty = scipy.stats.norm.pdf(ptx,mean,std)
    #    
    #    plt.fill_between(ptx, pty, color='#0b559f', alpha='1.0')
    #    
    #    #----------------------------------------------------------------------------------------#
    #    # fill area 2
    #    
    #    pt1 = mean + std
    #    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='black')
    #    
    #    pt2 = mean + 2.0 * std
    #    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='black')
    #    
    #    ptx = np.linspace(pt1, pt2, 10)
    #    pty = scipy.stats.norm.pdf(ptx,mean,std)
    #    
    #    plt.fill_between(ptx, pty, color='#2b7bba', alpha='1.0')
    #    
    #    # fill area 3
    #    
    #    pt1 = mean - std
    #    plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std)], color='black')
    #    
    #    pt2 = mean - 2.0 * std
    #    plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std)], color='black')
    #    
    #    ptx = np.linspace(pt1, pt2, 10)
    #    pty = scipy.stats.norm.pdf(ptx,mean,std)
    #    
    #    plt.fill_between(ptx, pty, color='#2b7bba', alpha='1.0')                 
    #                     
    #    plt.grid()
    #    
    #    plt.xlim(x_min,x_max)
    #    plt.ylim(0,0.05)
    #    
    #    plt.title('Çan Eğrisi',fontsize=10)
    #    
    #    plt.xlabel('x')
    #    plt.ylabel('y')
    #    
    #    plt.savefig("canegrisi.png")
        plt.show()
        
        #%%
        #harfnotu dağılımı
        
        AACount = sum(SinifList['Not'] == 'AA');
        BACount = sum(SinifList['Not'] == 'BA');
        BBCount = sum(SinifList['Not'] == 'BB');
        CBCount = sum(SinifList['Not'] == 'CB');
        CCCount = sum(SinifList['Not'] == 'CC');
        DCCount = sum(SinifList['Not'] == 'DC');
        DDCount = sum(SinifList['Not'] == 'DD');
        FDCount = sum(SinifList['Not'] == 'FD');
        FFCount = sum(SinifList['Not'] == 'FF');
        
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
    #write csv files
    if girisNo == 9:
        print('Kaydediliyor...')
        SinifList.to_csv('Output.csv');
    
    time.sleep(1);