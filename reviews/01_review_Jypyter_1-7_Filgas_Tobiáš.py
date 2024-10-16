"""_summary_
-----------------------------------------------------------------
VYPRACOVAL/A: Tobiáš Filgas
-----------------------------------------------------------------
"""

import os

os.system("clear")


def print_task_name(name: str):
    """
    Prints the task name in a bold green format.

    :param name: The name of the task to display.
    """
    print(f"\n\033[1;32m{name} \033[0m\n")


def print_error(error: str):
    """
    Prints an error message in a bold red format.

    :param error: The error message to display.
    """
    print(f"\n\033[1;31m{error} \033[0m\n")


def get_number_from_user(input_text: str = "Vložte číslo: ", 
                         error_message: str = "Špatný vstup, zkuste znova!", 
                         conditions: list = None) -> float:
    """
    Prompts the user for a number input and validates it against optional conditions.

    :param input_text: The prompt text to display when asking for input (default is in Czech: "Vložte číslo").
    :param error_message: The error message to display in case of invalid input (default is in Czech: "Špatný vstup, zkuste znova!").
    :param conditions: A list of boolean conditions to validate the number against. If any condition fails, the error message is shown.
    :return: The valid number entered by the user.
    """
    while True:
        try:
            number = float(input(input_text))

            if conditions and not all(condition(number) for condition in conditions):
                print_error(error_message)
                continue

            return number
        except ValueError:
            print_error(error_message)



##############################################################
# 1. Úkol: Základní aritmetické operace
# Napište kód, který bude načítat 2 čísla od uživatele (number1 a number2) a bude:
# a) sčítat dvě načtená čísla (suma)
# b) používat dělení a vracet jak běžné, tak celočíselné dělení (quotient, integer_division)
print_task_name("1. Úkol: Základní aritmetické operace")

# Načtení čísel
number_1 = get_number_from_user(input_text="Vložte první číslo: ")
number_2 = get_number_from_user(input_text="Vložte druhé číslo: ", conditions=[lambda n: n != 0])

# a) Sčítání
print(f"Součet: {number_1 + number_2}")

# b) Dělení a celočíselné dělení
print(f"Dělení: {number_1 / number_2}")
print(f"Celočíselné dělení: {number_1 // number_2}")


##############################################################
# 2. Úkol: Exponenty
# Doplňte kód, který načte číslo od uživatele a:
# a) spočítá třetí odmocninu čísla
# b) spočítá druhou odmocninu čísla
print_task_name("2. Úkol: Exponenty")

# Načtení čísla
number = get_number_from_user(conditions=[lambda n: n >= 0])

# a) Třetí odmocnina
print(f"Třetí odmocnina: {number ** (1/3)}")

# b) Druhá odmocnina
print(f"Druhá odmocnina: {number ** (1/2)}")

##############################################################
# 3. Úkol: Práce s proměnnými
# Zadejte proměnnou 'my_savings' a přiřaďte jí hodnotu od uživatele (např. 200)
# Poté vypočítejte, kolik budete mít peněz po přidání 10% úroků, které si uložíte do proměnné 'my_interest'.
print_task_name("3. Úkol: Práce s proměnnými")

my_savings = get_number_from_user(conditions=[lambda n: n >= 0])
my_interest = my_savings + my_savings * 0.1 

print(f"Zúročeno: {my_interest}")

##############################################################
# 4. Úkol: Operace s řetězci
# Napište kód, který:
# a) načte dva řetězce od uživatele (string1 a string2)
# b) zkontroluje, zda jsou oba řetězce stejné délky
# c) spojí oba řetězce do jednoho a vypíše výsledek
print_task_name("4. Úkol: Operace s řetězci")

# a) Načtení řetězců
string_1 = input("Zadejte první řetězec: ")
string_2 = input("Zadejte druhý řetězec: ")

# b) Zkontrolujte délku řetězců
if (len(string_1) != len(string_2)):
    print_error("Řetězce nejsou stejně dlouhé!")

# c) Spojení řetězců
print(f"Spojené řetězce: {string_1 + string_2}")

##############################################################
# 5. Úkol: Práce s cykly
# Napište kód, který:
# a) načte číslo od uživatele (např. 16)
# b) vypíše všechna čísla od 1 do tohoto čísla
# c) na každém pátém čísle vypíše text "Pátý krok!"
print_task_name("5. Úkol: Práce s cykly")

# Načtení čísla
number = get_number_from_user(conditions=[lambda n: n > 0])

# b) Výpis čísel
for i in range(1, int(number) + 1):
    if i % 5 == 0:
        print(f"\033[1;32m{i} - Pátý krok! \033[0m")
    else:
        print(i)

##############################################################
# 6. Úkol: Slovníky v Pythonu
# Napište kód, který:
# a) vytvoří prázdný slovník "person"
# b) přidá do slovníku tři položky, které načte od uživatele (např. name, age, city)
# c) vypíše všechny klíče a hodnoty slovníku v cyklu
print_task_name("6. Úkol: Slovníky v Pythonu")

# a) Vytvoření slovníku
person = {}

# b) Načtení údajů od uživatele
name = input("Jméno: ")
age = get_number_from_user(input_text="Věk: ", error_message="Neplatný věk!", conditions=[lambda n: n >= 0])
city = input("Město: ")

# Přidání údajů do slovníku
person["name"] = name
person["age"] = age
person["city"] = city

# c) Výpis slovníku
print(f"Osoba:\tJméno: {person['name']}\n\tVěk: {person['age']}\n\tMěsto: {person['city']}")

##############################################################
# 7. Úkol: Použití f-string
# Napište kód, který načte dva číselné údaje (např. result, score) a poté:
# a) použije f-string pro vložení těchto hodnot do textu
# b) použije f-string pro zobrazení těchto hodnot s přesností na 2 desetinná místa
print_task_name("7. Úkol: Použítí f-string")

# Načtení čísel
number_1 = get_number_from_user()
number_2 = get_number_from_user()

# a) Použití f-string
print(f"Čísla: {int(number_1)} & {int(number_2)}")

# b) Použití f-string s přesností na 2 desetinná místa
print(f"Čísla: {number_1:.02f} & {number_2:.02f}")


##############################################################
# 8. Úkol: Vytváření seznamů a indexování
# Napište kód, který:
# a) vytvoří seznam my_list o pěti prvcích na základě vstupu od uživatele
# b) vypíše třetí prvek seznamu
# c) vypíše poslední dva prvky seznamu
print_task_name("8. Úkol: Vytváření seznamů a indexování")

# a) Vytvoření seznamu
my_list = []

for i in range(1, 6):
    my_list.append(get_number_from_user(input_text=f"Vložte {i}. číselný prvek: "))

# b) Třetí prvek
print(f"Třetí prvek: {my_list[2]}")

# c) Poslední dva prvky
print(f"Poslední dva prvky: {my_list[3:]}")

##############################################################
# 9. Úkol: Základní metody seznamu
# Napište kód, který:
# a) vytvoří seznam my_list o třech prvcích od uživatele a přidá nový prvek pomocí metody append() + zobrazí
# b) odstraní prvek z určeného indexu od uživatele, pomocí metody pop() + zobrazí
# c) seřadí seznam abecedně pomocí metody sort() + zobrazí
print_task_name("9. Úkol: Základní metody seznamu")

# a) Vytvoření seznamu a přidání nového prvku
my_list = []

for i in range(1, 4):
    my_list.append(get_number_from_user(input_text=f"Vložte {i}. číselný prvek: "))


# b) Odstranění prvku na zvoleném indexu
i = int(get_number_from_user(input_text="Vložte pořadí prvku které chcete odstranit: ", conditions=[lambda n: n >= 1 and n <= 3]))

print(f"\nPrvek '{my_list[i - 1]}' se vymazává ...")
my_list.pop(i - 1)
print("Hotovo!")

# c) Seřazení seznamu
print(f"\nSeřazovaní...")
my_list.sort()
print(f"Seřazený list: {my_list}")

##############################################################
# 10. Úkol: Vytvoření tuple a indexování
# Napište kód, který:
# a) vytvoří tuple my_tuple se třemi prvky na základě vstupu od uživatele
# b) vypíše první prvek tohoto tuple
# c) vypíše poslední prvek tohoto tuple
print_task_name("10. Úkol: Vytvoření tuple a indexování")

# a) Vytvoření tuple
number_1 = get_number_from_user(input_text="Vložte 1. číselný prvek: ")
number_2 = get_number_from_user(input_text="Vložte 2. číselný prvek: ")
number_3 = get_number_from_user(input_text="Vložte 3. číselný prvek: ")

my_tuple = (number_1, number_2, number_3)

# b) První prvek
print(f"První prvek: {my_tuple[0]}")

# c) Poslední prvek
print(f"Poslední prvek: {my_tuple[len(my_tuple) - 1]}")

##############################################################
# 11. Úkol: Základní metody pro tuple
# Napište kód, který:
# a) vytvoří tuple my_tuple, který bude obsahovat následující prvky: 1, 2, 3, 2, 4, 2, 5
#    a spočítá počet výskytů uživatelem zadaného prvku pomocí metody count()
# b) zjistí index uživatelem zadaného prvku element_to_find v tuplu my_tuple pomocí metody index()
print_task_name("11. Úkol: Základní metody pro tuple")

# a) Vytvoření tuple a použití metody count()
my_tuple = (1,2,3,2,4,2,5)

number_to_count = int(get_number_from_user(input_text="Zadejte prvek: "))
print(f"Prvek se objevuje v tuplu: {my_tuple.count(number_to_count)}x")
# b) Použití metody index()
number_to_index = int(get_number_from_user(input_text="Zadejte prvek: ", conditions=[lambda n: n >= 1 and n <= 5]))
print(f"Index tohoto prvku v tuplu: {my_tuple.index(number_to_index)}")

##############################################################
# 12. Úkol: Neměnnost tuple
# Napište kód, který:
# a) vytvoří tuple a pokusí se změnit jeden z jeho prvků (tím demonstruje chybu)
# b) dokáže zachytit tuto chybu a informovat uživatele o chybě
print_task_name("12. Úkol: Němennost tuple")

# a) Vytvoření tuple
my_tuple = (1,2,3,2,4,2,5)

# b) Pokus o změnu prvku
try:
    my_tuple[0] = 0
except TypeError as e:
    print_error(f"An error occurred: {e}")


##############################################################

## NEZAPOMEŇTE ZMĚNIT JMÉNO SOUBORU! ##
