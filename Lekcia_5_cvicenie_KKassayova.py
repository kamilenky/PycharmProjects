numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]
#
# # # # 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.
negative_numbers = [n for n in numbers if n > 0]
print(negative_numbers)

# # # 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči
while True:
    user_input = input("List names: y/n: ").lower()
    if user_input == "y":
        for name in names:
            print(name)


    elif user_input == "n":
            print("Ok")
            exit()

# # moznost 2:
# # n = 0
# # while n < len(names):
# #     print(names[n])
# #     if names[n] == "Alice":
# #         break
# #     n += 1

# # 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0
new_list_random_codes = [x for x in random_codes if "0" in x]
print(new_list_random_codes)

# Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'
