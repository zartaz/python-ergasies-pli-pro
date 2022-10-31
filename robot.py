robot_x = 0
robot_y = 0


def ask_matrix_length():
    while True:
        try:
            length = int(input("Δώσε το μήκος του πίνακα: "))
            if length <= 0:
                print("Το μήκος του πίνακα πρέπει να είναι θετικός αριθμός")
            else:
                return length
        except ValueError:
            print("Το μήκος του πίνακα πρέπει να είναι ακέραιος αριθμός")


def robot_move(length):
    global robot_x, robot_y
    while True:
        move = input("Δώσε την κίνηση του ρομπότ: ")
        if move == "":
            print('Το πρόγραμμα τερματίστηκε,το ρομποτ θα αυτοκαταστραφεί')
            break
        if len(move) < 2:
            print("η κινηση πρεπει να αποτελειται απο τουλαχιστον δυο χαρακτηρες πχ 'l3' ή 'r2'")
            continue
        direction = move[:1]
        steps = move[1:]
        if direction.upper() not in ["L", "R", "U", "D"]:
            print("η κινηση πρεπει να ειναι τυπου '(l)3' ή '(r)2' ή '(u)1' Η '(d)4'")
            continue
        if not steps.isdigit():
            print("το βημα πρεπει να ειναι ακεραιος αριθμος πχ 'l(3)' η r(20)")
            continue
        steps = int(steps)
        if steps not in range(1, length):
            print(f"το βημα πρεπει να ειναι μεταξυ 1 και του οριου του πινακα({length-1})")
            continue
        if direction.upper() == "L":
            if robot_x - steps < 0:
                print("Το ρομπότ θα βγει από τον πίνακα")
                continue
            else:
                robot_x = robot_x - steps
        elif direction.upper() == "R":
            if robot_x + steps >= length:
                print("Το ρομπότ θα βγει από τον πίνακα")
                continue
            else:
                robot_x = robot_x + steps
        elif direction.upper() == "U":
            if robot_y - steps < 0:
                print("Το ρομπότ θα βγει από τον πίνακα")
                continue
            else:
                robot_y = robot_y - steps
        elif direction.upper() == "D":
            if robot_y + steps >= length:
                print("Το ρομπότ θα βγει από τον πίνακα")
                continue
            else:
                robot_y = robot_y + steps

        print(f"Το ρομπότ βρίσκεται στη θέση ({robot_x},{robot_y})")


def main():
    length = ask_matrix_length()
    robot_move(length)


main()










