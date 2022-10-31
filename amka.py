from datetime import date


def enter_amka():
    while True:
        amka = input("Εισαγετε τον AMKA: ")
        if len(amka) == 11 and amka.isdigit():
            return amka
        else:
            print("Παρακαλώ εισάγετε 11 ΨΗΦΙΑ")


def analyze_amka(amka):
    xronia = amka[:6]
    year = int(xronia[4:])
    gender_digit = int(amka[6:10])
    gender = 'αντρας'
    if gender_digit % 2 == 0:
        gender = "γυναικα"
    if year < 22:
        year += 2000
    else:
        year += 1900
    age = date.today().year - year
    print(f"ο/η κατοχος ειναι {age} ετων {gender}")


def rerun():
    while True:
        choise = input("Θελετε να ελεγξετε αλλο AMKA, (Ν)ΑΙ/(Ο)ΧΙ: ")
        if choise.upper() in ("ΟΧΙ", 'Ο', 'O'):
            print("ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ")
            exit(0)
        elif choise.upper() in ("ΝΑΙ", 'Ν', 'N'):
            break
        else:
            print("Λαθος επιλογη")
            continue


def main():
    while True:
        analyze_amka(enter_amka())
        rerun()


main()
