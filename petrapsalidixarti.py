import random

mikosleksisypologisti = 15
charaktires = 'πψχ'.upper()


def user_choise():
    while True:
        choise = input('Εισαγετε "Π,Ψ,Χ" για να παιξτε Η "Ε" για επανεκκινηση η ENTER για τερματισμο: ').upper()
        if choise == '':
            print('Τερματισμος παιχνιδιου')
            exit(0)
        elif choise == 'Ε' or choise == 'E':
            print('Επανεκκινηση παιχνιδιου')
            play_game()
        elif choise not in charaktires:
            print('Λαθος επιλογη')
            continue
        else:
            return choise


def evaluate_winner(user, computer):
    if user == computer:
        print('Ισοπαλια')
    elif user == 'Π' and computer == 'Ψ':
        print('Κερδισες !')
    elif user == 'Χ' and computer == 'Π':
        print('Κερδισες !')
    elif user == 'Ψ' and computer == 'Χ':
        print('Κερδισες !')
    else:
        print('Εχασες !')


def play_game():
    epilogespc = ''.join(random.choice(charaktires) for i in range(mikosleksisypologisti))
    while True:
        for char in epilogespc:
            xristis = user_choise()
            print(f"O υπολογιστης επιλεξε \"{char}\" και εσυ \"{xristis}\"")
            evaluate_winner(xristis, char)


play_game()
