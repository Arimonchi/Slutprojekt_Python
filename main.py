#E-butik systemmet 

#"ordbok" för varor
varor = {
    1: {"Namn": "Tröja", "pris": 520},
    2: {"Namn": "Jacka", "pris": 1700},
    3: {"Namn": "Mössa", "pris": 200},
    4: {"Namn": "Halsduk", "pris": 300},
    5: {"Namn": "Strumpor", "pris": 80},
    6: {"Namn": "Halsband", "pris": 1100},
    7: {"Namn": "Väska", "pris": 12000},
    8: {"Namn": "Sneakers", "pris": 1400},
    9: {"Namn": "T-shirt", "pris": 400},
    10: {"Namn": "Jeans", "pris": 980},
}

#total belpop (Börja med 0 kr)
total_price = 0
kundvagn = [ ]

#Meny
while True :
    print ("-----------------------------")

    print ("\nVälkomen till e-butik!!☺️🛍️\n")
    print("--- MENY ---\n")
    print("1. Visa produkter och handla")
    print("2. Visa totalbelopp")
    print("3. Betala och avsluta\n")

    väl = input ("\nVälj ett altanativ 1, 2 eller 3 :")
 
    print ("------------------------------")
 

#  1. Visa produkter och handla"
    
    if väl == "1" :

        print ("\nVåra produkter👞\n") 
  
        for i in varor :
             print(i, varor[i]["Namn"], varor[i]["pris"], "kr")
        
        varnummer= int(input ("Ange varunummer du vill köpa:"))
        print ()
        
        if varnummer in varor :
            total_price += varor[varnummer]["pris"]
            print ("\nTack😁! Varan har lagts till i kundvagnen🛒✨\n")

        else :
            print ("\nNumret finns inte i tillgängliga varor.")
            print ("Försök igen.\n")


#2. Visa totalbelopp
       
    elif väl == "2" :
        print ("\n💰Ditt totalbellop : ", total_price, "kr\n")


#3. . Betala och avsluta  

    elif väl == "3" :
        print ("\n✨Tack för ditt köp!😀✨\n")
        print ("💰Ditt totalbelopp är ", total_price, " kr.\n")
        print ("Välkommen åter!\n")
        print ("----------------------------------------")

        break


#else
else :
        print ("----------------------------------------")
        print("\nFel😭! \n")
        print("\nVälj nummer 1 eller 2.\n")
        print ("----------------------------------------")