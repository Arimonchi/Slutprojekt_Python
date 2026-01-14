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


#Meny
while True :
    print ("◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎")

    print ("\nVälkomen till e-butik!!☺️🛍️\n")
    print("--- MENY ---\n")
    print("1. Visa produkter och handla")
    print("2. Visa kundvagn och totalbelopp")
    print("3. Betala och avsluta\n")

    väl = input ("\nVälj ett altanativ 1, 2 eller 3 :")
 
    print ("◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎")
 

#  1. Visa produkter och handla"  
    
    print ("\nTillgängliga varor👞\n") 
  
    for i in varor :
          print(i, varor[i]["Namn"], varor[i]["pris"], "kr")
    print ()
    print ("----------------------------------------")
 
    
    if väl == "1" :
        print ("----------------------------------------")
        print ()
        varnummer= int(input ("Ange varunummer du vill köpa:"))
        print ("----------------------------------------")

        if varnummer in varor :
            print ("\nTack😁! Varan har lagts till i kundvagnen🛒✨\n")
            total_price += varor[varnummer]["pris"]
            print ("\n💰Ditt totalbellop : ", total_price, "kr\n")
      
        else :
            print ("\nNumret finns inte i tillgängliga varor.")
            print ("Försök igen.\n")

#2. Visa kundvagn och totalbelopp

    elif väl == "2" :
        print ("----------------------------------------")
        print ("\n✨Tack för ditt köp!😀✨\n")
        print ("💰Ditt totalbelopp är ", total_price, " kr.")
        print ("Välkommen åter!\n")
        print ("----------------------------------------")
        break

#Väl3 : else
    else :
        print ("----------------------------------------")
        print("\nFel😭! Välj nummer 1 eller 2.\n")
        print ("----------------------------------------")