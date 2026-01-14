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
    print ("Välkomen till e-butik!!")
    print ("Tillgängliga varor:") 
#isa varor
    print (varor)

#Fråga vad kunden vill göra
    print ("Vad vill du göra?")
    print ("1 : Handla ")
    print ("2 : Avsluta och betala")
    var = input ("Välj ett altanativ : 1 eller 2")

#Altanativ 1

