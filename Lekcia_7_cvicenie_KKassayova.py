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


# input
def choose_username() -> str:
    for _ in range(1):
        while True:
            user_name = input("Please, choose your user name (at lesat 4 characters): ")
            if len(user_name) >= 4:
                # yield user_name
                # break
            else:
                print("User name must be at least 4 characters long.")

usernames = list(choose_username())

print("usernames:")
print(usernames)

# input

def is_adult (valid_age, minimum_age=17) -> bool:
    valid_age = int(input("Please, add your age: "))
    return valid_age > minimum_age

upravit cez loop? vratit 4 x user name?


# def create_user(0)

def create_user(

        return is_adult, is_name_valid
        if statements
        is_name_valid==True + is_adult==True > slovnik

        else exceptions
)

#exceptions
try:
    def is_name_valid
        if min_lenght== False
except ValueError:
    print("Minimum user name lenghth is 4 characters")

try:
    def is_adult
        if minimum_age== False
except ValueError:
    print("Minimum age must be 18 years old.")


def print_user_info(print_user, str):
    print("Hello  ", print_user)

def print_email_info(print_email, str):
    print("Your email account ", print_email, "has been created.")



def get_numbers () -> tuple [int, str]:
    return int, "str"

def work() ->
    x,y = def_int ()
    def_str("abc")
    print(def3())

work()


yield



#
# is_adult(valid_age)





# input username

# def greet_user(name: str) -> None:
#     print("Hello ", name)
#
# greet_user("Jano")
#


#
# # input email
# # input vek
#
# def age (input_age): -> int
#     print (f"What is your age?: ".lower() (input_age)
#
# age ("What is your age?: ".lower(), age_input)
# age_input  = input ("What is your age?: ").lower()
# print(age_input)
# def is_adult  -> int:
#     x = age_input
#
#     return x >= 18
# print

# age validation
# usename validation

# create user 4x
# check dictionary

# print: users <> eroor message
#
#
# from my_package.new import add
# from my_package import new
#
# res = new.add(6, 6)
# print(res)
