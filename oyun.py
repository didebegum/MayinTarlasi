import random
from scipy import mat
satir1 = []
satir2 =[]
satir3= []
bayrakSayi = 0
mayinSayi= 0
puan = 0
while True:
    bayrakSayi1 = 0
    mayinSayi1= 0
    diziSay = str(random.randint(0,1))
    if diziSay == "0":
        if mayinSayi1 <2:
            satir1 = satir1  + [diziSay] 
            mayinSayi1 += 1
    if diziSay =="1":
        if bayrakSayi1 <3:
            satir1 = satir1  +[diziSay]
            bayrakSayi1 += 1
    if bayrakSayi1 + mayinSayi1 ==5:
        print (satir1 )
        break 
        
while True:
    bayrakSayi2 = 0
    mayinSayi2 = 0
    diziSay = str(random.randint(0,1))
    if diziSay == "0":
        if mayinSayi2 <2:
            satir2  = satir2 + [diziSay] 
            mayinSayi2 += 1
    if diziSay =="1":
        if bayrakSayi2 <3:
            satir2  = satir2 +[diziSay]
            bayrakSayi2 += 1
    if bayrakSayi2+ mayinSayi2 ==5:
        print (satir2  )
        break
        
while True:
    bayrakSayi3 = 0
    mayinSayi3 = 0
    diziSay = str(random.randint(0,1))
    if diziSay == "0":
        if mayinSayi3 <2:
            satir3  = satir3 + [diziSay] 
            mayinSayi3 += 1
    if diziSay =="1":
        if bayrakSayi3  <3:
            satir3  = satir3 +[diziSay]
            bayrakSayi3 += 1
    if bayrakSayi3+ mayinSayi3 ==5:
        print (satir3  )
        break    
            
matris = [satir1 , satir2 ,satir3 ]   
print (matris )              
  
"""    
while True :
    secilen= input("koordinat giriniz x,y")
    secilenDeger = dizi[int(secilen)-1]
    if secilenDeger =='0':
        print ("Mayina bastiniz. Puaniniz:"+ str(puan ) )
        break 
        
    if secilenDeger =='1':
        puan = puan +10
        print (str(puan )+"Puan")
        secilenDeger = 'a'
            
"""     
        
    
        
     
