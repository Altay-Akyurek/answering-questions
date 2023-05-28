import math
##Klavyeden girilen x’e göre denklemin sonucunu bulan programı yazınız
x=int(input("yapmak istediğiniz sorunun sayısını yazınız:"))
if (x==1):
    n=int(input("bir sayı giriniz:"))
    if (n<=0):
        c=n*n
        print(c)
    else:
        c=n*n*n
        print(c)
##cevap:bir sayı giriniz:25
##15625
##Klavyeden girilen x’e göre denklemin sonucunu bulan programı yazınız.
elif(x==2):
    n=int(input("bir sayı giriniz:"))
    if(n<=-5):
        c=n+5
        print(c)
    elif(n>5 and n<=10 ):
        c=n+2
        print(x)
    else:
        c=3*n
        print(c)
##cevap:bir sayı giriniz:11  33
elif(x==3):
    n=int(input("bir sayı giriniz:"))
    d=n%100
    if(d%2==0):
        c=2*n
        print(c)
    else:
        c=n/2
        print(c)
##cevap:bir sayı giriniz:21   10.5
elif(x==4):
    A=int(input("bir sayı giriniz:"))
    
    if(A>10 and A<17):
        print("girdiğiniz sayı 10 dan büyük ve 17 den küçüktür")
    else:
        print("girdiğiniz sayı 10 ile 17 arasında değildir.")
    B=int(input("bir sayı giriniz:"))
    if (B>20 and B<100):
        print("girdiğiniz sayı 20 dan büyük ve 100 den küçüktür")

    else:
        print("girdiğiniz sayı 20 ile 100 arasında değildir.")
    C=int(input("bir sayı giriniz:"))
    if(C>7 and C<77):
        if(C%7==0):
            print("bu sayı 7 ile 77 arasında ve 7 ye tam bölünmektedir ")
        else:
            print("bu sayı 7 ile 77 arasında ve 7 ye tam bölünememektedir ")
    else:
        print("bu sayı 7 ile 77 arasında değildir.")
    cinsiyet=str(input("cinsiyetinizi giriniz:"))
    yaş=int(input("yaşınıızı giriniz:"))
    if((cinsiyet=="kadın" and yaş==20)or (cinsiyet=="erkek" and yaş==30)):
        print("bilgiler için Teşekür ederiz")
    else:
        print("bilgiler için teşekkür ederiz.")
##cevap:
elif(x==5):
    def hesapla_mtv(motor_cc, fatura_degeri):
        if motor_cc <= 1300:
            if fatura_degeri <= 50000:
                return 750
            elif fatura_degeri <= 90000:
                return 1000
            else:
                return 1250
        elif motor_cc > 1300 and motor_cc <= 1600:
            if fatura_degeri <= 50000:
                return 900
            elif fatura_degeri <= 90000:
                return 1200
            else:
                return 1500
        elif motor_cc > 1600 and motor_cc <= 2000:
            if fatura_degeri <= 130000:
                return 1650
            else:
                return 2250
        elif motor_cc > 2000 and motor_cc <= 2500:
            if fatura_degeri <= 160000:
                return 3500
            else:
                return 5000
        else:  # motor_cc > 2500
            if fatura_degeri <= 300000:
                return 10000
            else:
                return 15000


    motor_cc = int(input("Aracın motor kapasitesini (cc) girin: "))
    fatura_degeri = float(input("Aracın fatura değerini (TL) girin: "))

    mtv = hesapla_mtv(motor_cc, fatura_degeri)
    print("Aracın Motorlu Taşıtlar Vergisi (MTV) tutarı:", mtv, "TL")
##cevap:
elif(x==6):
    n=int(input("tekrar etmesini istediğiniz sayının değerini giriniz:"))
    c=0
    for i in range(1,n+1):
        c+=i/(i+1)
    print(c)

##cevap:
elif(x==7):
    a=0
    b=0
    for i in range(7,7778):
        if (i%13==0 and i%2==1):
            a+=i
        print(a)
    for t in range(120,1201):
        if(t%27==2):
            b+=t
        print(b)
    print("{} ve {} nin oranı={}".format(a,b,a/b))
##cevap:
elif(x==8):
    for i in range(1,101):
        if(i%2==1):
            print(i)
##cevap:
elif(x==9):
    x=int(input("bir sayı giriniz:"))
    n=int(input("toplama yapılacak değeri yazınız:"))
    if (x<=10):
        c=7*x*x
        print(c)
    elif(x>10 and x<=20):
        c=x*x*x
        print(c)
    else:
        c=5*x
        print(c)
    for i in range(2,n+1):
        c+=c
    print(c)
##cevap:
elif(x==10):
    n=int(input("bir sayı giriniz:"))
    x=int(input("almak istediğiniz kuvveti giriniz:"))
    c=1
    for i in range(1,x+1):
        c*=n
    print(c)
##cevap:
elif(x==11):
    

    a = float(input("a değerini girin: "))
    b = float(input("b değerini girin: "))
    c = float(input("c değerini girin: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Reel kök yok.")
    elif delta == 0:
        x = -b / (2*a)
        print("Tek kök:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("İki kök var:")
        print("x1 =", x1)
        print("x2 =", x2)
##cevap:
elif(x==12):
    sayi1 = 0
    sayi2 = 0
    sonuc = 0

    print("sayı 1 girin:")

    sayi1 = int(input())

    print("sayı 2 girin:")

    sayi2 = int(input())

    for sayac in range(0,sayi2):
        sonuc = sonuc + sayi1


    
    print("girdiğiniz iki sayının çarpımı:", sonuc)
##cevap:        
elif(x==13):
    def ortalama(a,b,c):
        reply=((a*(0.4))+(b*0.1)+(c*0.5))
        if (c<50):
            print("note %s"%(reply))
            print("you stayed")
        elif (reply<50):
            print("note %s"%(reply))
            print("you stayed")
        else:
            print("note %s"%(reply))
            print("you passed ")
        return reply
    


    while True:
        a=int(input("visa note:"))
        b=int(input("homeword grade"))
        c=int(input("final grade"))
        ortalama(a,b,c)

##cevap:
elif(x==14):
    saniye=int(input("saniyer giriniz:"))
    print("saat={},dakika={},saniye={}".format(saniye/3600,saniye/60,saniye))
##cevap:
elif(x==15):
    sayi = input("6 haneli bir sayı girin: ")

    if len(sayi) != 6:
        print("Geçersiz giriş! 6 haneli bir sayı girmelisiniz.")
    else:
        yeni_sayi = sayi[:1] + "0" + sayi[4:]
        print("Yeni sayı:", yeni_sayi)
##cevap:
elif(x==16):
    x=int(input("bir sayı giriniz:"))
    f=x**3
    g=x**2+x/2+7
    h=((x**6)/5)/((7+9*x-2)/4*x)
    print("hog(x):{},fog(x):{},gof(x):{}".format(((g**6)/5)/((7+(9*g)-2)/4*g),g**3,(f**2)+(f/2)+7))
##cevap:          
elif(x==17):
    def kisaltma(sayi):
        if sayi >= 1000 and sayi <= 9999:
            return str(sayi // 1000) + "B"
        elif sayi >= 100 and sayi <= 999:
            return str(sayi // 100) + "K"
        elif sayi >= 10 and sayi <= 99:
            return str(sayi // 10) + "K"
        elif sayi >= 1 and sayi <= 9:
            return "1K"
        else:
            return "Geçersiz sayı"


    sayi = int(input("Bir sayı girin: "))

    kisaltma_str = kisaltma(sayi)
    print("Kısaltma:", kisaltma_str)
##cevap:
elif(x==18):
    def hesapla_maas(personel_tipi, calisma_saati):
        saat_ucretleri = {
            "işçi": 75,
            "usta": 100,
            "ustabaşı": 150
        }

        normal_calisma_saati = min(calisma_saati, 40)
        fazla_calisma_saati = max(calisma_saati - 40, 0)

        normal_ucret = normal_calisma_saati * saat_ucretleri[personel_tipi]
        fazla_ucret = fazla_calisma_saati * saat_ucretleri[personel_tipi] * 1.5

        toplam_ucret = normal_ucret + fazla_ucret

        return toplam_ucret


    personel_tipi = input("Personel tipini girin (işçi/usta/ustabaşı): ")
    calisma_saati = float(input("Haftalık çalışma saatinizi girin: "))

    maas = hesapla_maas(personel_tipi, calisma_saati)
    print("Haftalık maaşınız:", maas, "₺")  
##cevap:
elif(x==19):
    count = 0
    for sayi in range(1, 1001):
        if sayi % 13 == 0:
            print(sayi, end=" ")
            count += 1
            if count % 11 == 0:
                print()

            if count == 55:
                break
##cevap:
elif(x==20):
    sayi = int(input("Bir sayı girin: "))
    print("Sayının Tam Bölenleri:")
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            print(i)
##cevap:
elif(x==21):
    a=int(input("bir sayı giriniz:"))
    b=int(input("bir sayı giriniz:"))
    liste1=[]
    liste2=[]
    liste3=[]
    for i in range(1,a+1):
        if(a%i==0):
            liste1.append(i)
    for t in range (1,b+1):
        if(b%t==0):
            liste2.append(t)
    print(liste1)
    print(liste2)
    for eleman1 in liste1:
        for eleman2 in liste2:
            if(eleman1/eleman2==1):
                liste3.append((eleman1,eleman2))

    print(liste3)
##cevap:
elif(x==22):
    n = int(input("n sayısını girin: "))

    # Kare kısmı
    for i in range(n):
        for j in range(n):
            print("x", end="")
        print()

    # Üçgen kısmı
    for i in range(1, n+1):
        for j in range(i):
            print("x", end="")
        print()

    # Ters üçgen kısmı
    for i in range(n-1, 0, -1):
        for j in range(i):
            print("x", end="")
        print()

    # Dikdörtgen kısmı
    for i in range(n+1):
        for j in range(i):
            print("x", end="")
        print()

    # Ters dikdörtgen kısmı
    for i in range(n-1, 0, -1):
        for j in range(i):
            print("x", end="")
        print()
##cevap: