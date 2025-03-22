books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]

# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
books.append(
    {
        "name": "Malý princ",
        "price": 600,
        "author": "Antoine de Saint-Exupéry",
        "publication_year": 1943,
    }
)
books.append(
    {
        "name": "Nič nehovor ",
        "price": 700,
        "author": "Patrick Radden Keefe",
        "publication_year": 2021,
    }
)
print (books)

# 2. Změň cenu jedné libovolné knihy. Vypiš list.
a = {'name': 'Pán prstenů: Společenstvo prstenu', 'price': 500, 'author': 'J.R.R. Tolkien', 'publication_year': 1954}
b = {'name': 'Malý princ', 'price': 600, 'author': 'Antoine de Saint-Exupéry', 'publication_year': 1943}
c = {'name': 'Nič nehovor ', 'price': 700, 'author': 'Patrick Radden Keefe', 'publication_year': 2021}
books = [a , b , c]
a.update(price = 550)

print (books)

# 3. Odstraň nějakou knihu. Vypiš list.
del books[2]
print (books)

# 4. Vypiš celkový počet knih v listu.
počet_kníh = len(books)
print (počet_kníh )

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)
print("Pridaj knihu - ")
name = input("Uveď názov knihy: ")
price = input("Uveď cenu: ")
author = input("Uveď autora: ")
publication_year = input("Uveď rok vydania: ")

d = {'name': name, 'price': price, 'author': author, 'publication_year': publication_year }
print(d)
books.append(d)
print(books)


# uf, bola to fuška!