import random

def cipher(x, y): # Funkcja kodujaca kryptogram
    v=0
    newString1=""
    for ix in range(int(len(x)/len(y))): # Przestaw znaki wedlug klucza
       for iy in y:
           pos=v-1+iy
           newString1+=x[pos]
       v=(ix+1)*len(y)
    newString2=""
    for iz in newString1: # Przesun znaki w tablicy ASCII
        if ord(iz) > 79:
            newString2+=chr(ord(iz)-48)
        elif ord(iz) < 79:
            newString2+=chr(ord(iz)+48)
        else:
            newString2+=iz
    return newString2

def decipher(x, y): # Funkcja dekodujaca kryptogram
    v=0
    newString1=""
    for ix in x: # Przesun znaki w tablicy ASCII
        if ord(ix) > 79:
            newString1+=chr(ord(ix)-48)
        elif ord(ix) < 79:
            newString1+=chr(ord(ix)+48)
        else:
            newString1+=ix
    newList=list(newString1)
    for ix in range(int(len(x)/len(y))): # Przestaw znaki wedlug klucza
       c=0
       for iy in y:
           pos=v-1+iy
           newList[pos]=newString1[v+c]
           c+=1
       v=(ix+1)*len(y)
    newString2=""
    return newString2.join(newList)

def appender(x, y): # Funkcja dodajaca spacje na koncu tekstu jawnego
    while (float(len(x))%float(len(y))!=0): # Sprawdz czy tekst jawny jest podzielny przez dlugosc klucza
        x=x+" " # Dodaj spacje i powtorz sprawdzenie
    return x 

def keyGenerator(xStop, defKey): # Funkcja generujaca odpowiedni klucz
    xStart=1
    if 1 <= (xStop-1):
        newKey=random.sample(range(xStart, xStop), (xStop-1))
        print(f"Twoj nowy klucz to: {newKey}")
        return newKey
    else:
        print("Nieprawidlowa wielkosc klucza. Sprobuj ponownie.")
        return defKey

def keyImplementer(xKeyLength, defKey): # Funkcja implementujaca istniejacy klucz / pozwalajaca na utworzenie wlasnego
    ans2=True
    if 1 <= xKeyLength:
        newKey=[]
        for ik in range(xKeyLength):
            newKey.append(int(input(f"Podaj liczbe na pozycji {ik+1}: ")))
        for i2k in range(xKeyLength):
            if (i2k+1) not in newKey:
                ans2=False
        if ans2==True:
            print(f"Zmieniono klucz. Twoj nowy klucz to: {newKey}")
            return newKey
        elif ans2==False:
            print(f"Klucz nieprawidlowy. Musi zawierac liczby z przedzialu od 1 do {xKeyLength}, bez powtorzen. Sprobuj ponownie")
            return defKey        
    else:
        print("Nieprawidlowa wielkosc klucza. Sprobuj ponownie.")
        return defKey

key=[5, 3, 6, 4, 2, 1] # Klucz domyslny

ans=True
while ans:
    print ("""
    Kryptografia Projekt 
    Wiktor Skrzypczak 249384
    -------------------------
    !! Program nie wspiera Polskich znakow !!
    -------------------------
    1.Szyfrowanie
    2.Deszyfrowanie
    3.Wprowadzenie klucza
    4.Generacja klucza
    5.Wyswietl obecny klucz
    6.Wyjscie
    """)
    ans=input("Co chcialbyś zrobić? ") 
    if (ans=="1"): 
       cont=input("Wprowadz tresc do zaszyfrowania: ")
       cont=appender(cont, key)
       print(f"Otrzymany kryptogram: {cipher(cont, key)}")
    elif (ans=="2"):
        code=input("Wprowadz tresc do rozszyfrowania: ")
        print(f"Otrzymany tekst jawny: {decipher(code, key)}")
    elif (ans=="3"):
        keyLength=int(input("Podaj wielkosc klucza: "))
        key=keyImplementer(keyLength, key)
    elif (ans=="4"):
        keyLength=(int(input("Podaj wielkosc klucza: "))+1)
        key=keyGenerator(keyLength, key)
    elif (ans=="5"):
        print(f"Obecny klucz: {key}")
    elif (ans=="6"):
        ans=False
    elif (ans !=""):
      print("\n Nieprawidlowy wybor. Sprobuj ponownie.") 