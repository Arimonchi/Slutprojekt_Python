# Aktivitet 10 – Avancerat projekt: Design & planering

## 1. Projektidé och syfte
Jag bestämde att jag ska skapa en enkel e-butik i terminalen där användare kan köpa olika produkter. Det kan innehålla alla punkter som jag studerade den här kursen. 
Jag vill skapa ett användarvänligt flöde för en enkel transaktion.

## 2.Planering

-Ordbok för varor
Nyckel : Varunummer 
Värde : namn och pris

-Variabler
total_belopp : Börja med 0 kr och samla pris som man valde.

-Loop (while och if/elif/else)
Visa meny och löpande köping tills man väljer nej. 

## 3.Pseudokod
1. Skapa en 'Ordbok' för varor (Nummer, Namn, Pris).
2. Sätt 'Totalbelopp'.
3. Starta loopen - Skriv ut "Välkommen till e-butiken!".
4. Visa alla varor från ordboken.
5. Fråga "Vill du handla? (1: Ja / 2: Avsluta ).
6. Ta emot svar (1 eller 2).
7. Om det är "1":
    Fråga varunummer och ta emot nummer.
    Hämta varan (Namn och Pris) och addera priset till 'Totalbelopp'.
    Annas, skriv ut "Fel: Varunummer saknas".
8. Om det är "2":
        Skriv ut "Ditt kvitto " och Totalbelopp: [Totalbelopp] kr".
        Skriv ut "Tack för besöket! Hej då!" och avsluta loopen.
9. Om det är något annat än 1 eller 2, skriv ut "Fel: Välj 1 eller 2".




