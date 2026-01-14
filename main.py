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


#Loop (Om man vill köpa eller inte)
while True :
    print ("◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎")

    print ("\nVälkomen till e-butik!!☺️🛍️\n")

    print ("◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎・◼︎")

    print ("\nTillgängliga varor👞\n") 
   
#isa varor
    for i in varor :
          print(i, varor[i]["Namn"], varor[i]["pris"], "kr")
    print ()
    print ("----------------------------------------")
#Fråga vad kunden vill göra
 
    print ("\nVad vill du göra?\n")
    print ("1 : Handla ")
    print ("2 : Avsluta och betala")
    väl = input ("\nVälj ett altanativ 1 eller 2 :")
    print ()
#Väl 1: Handla
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

#Väl2 :Avsluta och betala
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