# Vytvořte program pro určení ceny tramvajových jízdenek.
#
# Program bude pracovat se třemi údaji: věk zákazníka, cena jízdenky a zda je nakupující zaměstnancem tramvajové služby.
#
#     Hodnoty pro údaje k určení ceny jízdenky můžeš určit libovolně přímo v kódu [+0B],
#     nebo je můžeš načíst z uživatelského vstupu - pomocí funkce input [+1B],
#     pokud ještě navíc ukončíš program s chybovou hláškou, když je zadaný datový typ špatný, dostaneš [+1B]
#
# Program určí a následně vypíše konečnou cenu na základě těchto kritérií:
#
#     Plná cena jízdenky je 45 Kč.
#     Cestující do 12 let jezdí zdarma.
#     Cestující mladší 18 let má slevu 50%.
#     Cestující nad 65 let mají 30% slevu.
#     Zaměstnanci tramvajové služby mají slevu 80%.
#     Zaměstnanci tramvajové služby nad 55 let mají jízdenku zdarma.
#
# Bonusový úkol (Pokud ho nebudete mít hotový, nebude to mít vliv na váš celkový výsledek, body za něj nebudou odečítány.):
# Při zadání špatného datového typu se program neukonči, ale vyzve uživatele o nové zadání hodnoty.
#from kod import employee
#

basic_fare = 45
price = basic_fare

print ("Vyberte si typ cestovného listka: \n Dospelý (nad 18 rokov, plna cena) \n Dieta (od 0 do 12 rokov, zadarmo) \n Junior (od 13 do 17 rokov, zľava 50%) \n Senior (nad 65 rokov, zľava 30%) \n Zamestnanec 1 (do 55 rokov, zľava 80%)\n Zamestnanec 2 (nad 55 rokov, zadarmo) ")



try:
    employee = str(input("Ste zamestnanec MHD? ano/nie: ").strip().lower())
except ValueError:
    print("Nespravny udaj. Opakujte volbu A.")
    emolyee != "ano", "nie"
    if employee == "ano":
        if age >= 55:
            price = 0
            print(f"Vasa kategoria je zamestnanec 1. Cena listka je {price: 0.2f} Kc")
        else:
            price = basic_fare * 0.2
            print(f"Vasa kategoria je zamestnanec 1. Cena listka je {price: 0.2f} Kc")

#otazka: ako mam osetrit chybny vstup pre empoyee, ak sa zada ina hodnota ako str "ano", "nie"?
# response = input("Do you want to try a guessing game?: [yes or no]")
# while response != "yes" or "no":
#   if response =="yes":
#     print("Great, let's get started! Guess a number from 0-20")
#     break
#   elif response == "no":
#     print("Okay, see you later!")
#     exit()
#   else:
#     print("Sorry, please type 'yes' or 'no':")
#   break


try:
    age = int(input("Kolko mate rokov: ").strip())
except ValueError:
    print("Nespravny udaj. Opakujte volbu.B")
    age = None
#otazka: ako v tomto bode spustim program odznovu?

if age <= 12:
     price = 0
     print(f"Vasa kategoria je dieta. Cena listka je {price: 0.2f} Kc")

elif 13 <= age <=17:
     price = basic_fare * 0.5
     print(f"Vasa kategoria je junior. Cena listka je {price: 0.2f} Kc")

elif 18 <= age < 65:
     price = basic_fare
     print(f"Vasa kategoria je dospely. Cena listka je {price: 0.2f} Kc")

elif age >= 65:
     price = basic_fare * 0.7
     print(f"Vasa kategoria je senior. Cena listka je {price: 0.2f} Kc")

else:
    print("Nespravny udaj. Opakujte volbu.C")

