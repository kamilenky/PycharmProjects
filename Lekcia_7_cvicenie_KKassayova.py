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



def is_name_valid(username: str) -> bool:
    return len(username) >= 4

def is_adult (age: int) -> bool:
    return age >= 18

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

users =  [{"username": "Adam", "age": 18},
{"username": "Brano", "age": 17},
{"username": "Cyril", "age": 20},
{"username": "Dan", "age": 21}]

for user in users:
    result = create_user(user["username"], user["age"])
    print_user_info(result)
