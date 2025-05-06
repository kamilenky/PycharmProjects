# Napiš program, který bude pracovat s informacemi o uživatelském účtu: username, age, email
#
#
# Vytvoř následující funkce:
#
# is_adult: Funkce ověří zda je uživatel dospělý
# is_name_valid: Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé
# create_user:
#
#       Funkce vytvoří slovník reprezentujícího uživatele.
#      Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
#
# Pokud je vše v pořádku, create_user vrátí následující slovník:
# {
# "success": True,
# "user": {"username": "...", "age": ..., "email": "..."}
# }
#  Pokud validace selže, create_user vrátí:
# {
# "success": False,
# "error": "Chybová zpráva..."
# }
#
#
# print_user_info: Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření
#
# Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu.
#
# Nakonec vytvořené uživatele vytiskni pomocí cyklu a metody print_user_info.




# functions
def is_name_valid(username, min_length=4) -> bool:
    return len(username) > min_length

def is_adult (age, minimum_age=18) -> bool:
    return age > minimum_age

def create_user(username: str, age: int) -> dict:
    if not is_name_valid(username):
        return {
            "success": False,
            "error": "The username must be at least 4 characters long. Please. enter your name again."
        }

    if not is_adult(age):
        return {
            "success": False,
            "error": "The minimum age must be 18 years. Please. enter your age again."
        }
    return {
            "success": True,
            "user": {"username": username, "age": age, "email": f"{username.lower()}@gmail.com"}
    }

def print_user_info(result: dict) -> None:
    if result["success"]:
        u = result["user"]
        print(f"Your account has been created. Username: {u['username']}, Email: {u['email']}")
    else:
        print(f"Error: {result['error']}")


# username and age input
# def input (name_input) -> str:

created_users = [i for i in range(4)]
name_input = input("Please, choose a username:")

try:
    age_input = int(input("Please, enter your age:"))
except ValueError:
    print("The age must be a number.")


result = create_user(user["username"], user["age"])
created_users.append(result)


for u in created_users:
    print_user_info(u)





