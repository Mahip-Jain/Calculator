only_numbers = "Sorry, you are only allowed to enter numbers"

maxquestions = 10

correct_ans = "You gave the correct answer"

incorrect_ans = "You gave the incorrect answer"

correct_ans_is = "\nThe Correct answer is"

enter_age = "Enter your age:"

enter_name = "Enter you name:"

welcome = "\nWelcome to MATH PROBLEM GENERATOR,"

if_level_easy = "If you want to do level EASY than enter 1"

if_level_medium = "If you want to do level MEDIUM than enter 2"

if_level_hard = "If you want to do level HARD than enter 3"

ans = "Answer:"

which_level = "\nWhich level do you want:"

only_num_123 = "Sorry, you are only aloud to enter the number 1,2 or 3"

start_test = "\nI will start your test now"

not_num = "Not a number! Try again."

raw_inp_quotient = "Quotient:"

raw_inp_remainder = "Remainder:"

multiply = "x"

divide = "/"

add = "+"

minus = "-"

seperator2 = "*" * 100

correct_quotient = "\nThe Correct quotient is "

correct_remainder = "\nThe Correct remainder is "

final_score = "Your score is "


def printcenter(abc):
    print abc.center(150)

def banner():
    design_for_game_name = "########################"
    game_name = "#MATH PROBLEM GENERATOR#"
    design_for_my_name = "***********************"
    my_name = "*Created by Mahip Jain*"
    seperator_for_game_name = "-" *100
    description = "This is an educational game made for kids to improve their mathematical skills. There are 3 levels, Easy, Medium and Hard. There is a set of ten questions for\neach level and a timer for each question. I hope you enjoy using this game.\n"
    printcenter(design_for_game_name)
    printcenter(game_name)
    printcenter(design_for_game_name)
    printcenter(seperator_for_game_name)
    printcenter(design_for_my_name)
    printcenter(my_name)
    printcenter(design_for_my_name)
    print description


def get_age():
    age = raw_input(enter_age)

    return int(age)


def get_name():
    name = raw_input(enter_name)
    return name


def info_for_level(name):
    print welcome + " " + str(name) + " " + "!!\n"
    print if_level_easy
    print if_level_medium
    print if_level_hard

    while 1:
        level = raw_input(which_level)
        if level.isdigit():
            if int(level) != 1 and int(level) != 2 and int(level) != 3:
                print only_num_123
            else:
                break
        else:
            print only_numbers

    print start_test
    return int(level)


def run_problem_generator(age, level):
    import random

    def get_userinput(message):
        while True:
            try:
                userInput = int(input(message))
            except:
                print(not_num)
                continue
            else:
                return userInput
                break

    a = 1
    random1 = 0
    random2 = ""
    random3 = 0
    score = 0
    lst2 = [add]
    minimum = 1
    if age <= 7:
        maximum = 9
    elif age == 8 or age == 9:
        maximum = 99
    else:
        maximum = 999

    def level1():
        lst2.append(minus)

    def level2():
        lst2.append(minus)
        lst2.append(multiply)

    def level3():
        lst2.append(minus)
        lst2.append(multiply)
        lst2.append(divide)

    if level == 1:
        level1()
    elif level == 2:
        level2()
    else:
        level3()
    printcenter(seperator2)

    while a < maxquestions + 1:

        random1 = random.randint(minimum,maximum)
        random2 = random.choice(lst2)
        random3 = random.randint(minimum, maximum)
        print random1, random2, random3, "\n"
        answer = 0
        if random2 == add or random2 == minus or random2 == multiply:
            answer = get_userinput(ans)

        if random2 == add:
            if answer == random1 + random3:
                print correct_ans
                score += 1
            else:
                print incorrect_ans
                print correct_ans_is, random1 + random3
        elif random2 == minus:
            if answer == random1 - random3:
                print correct_ans
                score += 1
            else:
                print incorrect_ans
                print correct_ans_is, random1 - random3
        elif random2 == multiply:
            if answer == random1 * random3:
                print correct_ans
                score += 1
            else:
                print incorrect_ans
                print correct_ans_is, random1 * random3
        else:
            quotient = get_userinput(raw_inp_quotient)
            remainder = get_userinput(raw_inp_remainder)
            if quotient == random1 / random3 and remainder == random1 - quotient * random3:
                print correct_ans
                score += 1

            else:
                print incorrect_ans
                print correct_quotient, random1 / random3, correct_remainder, random1 - quotient * random3

        print "score =", score, divide, a
        a += 1
    print final_score, score, divide, maxquestions


def main():
    banner()
    age = get_age()
    name = get_name()
    while True:
        level = info_for_level(name)
        run_problem_generator(age, level)
        print "Do you want to continue?"
        if_want_to_quit = raw_input("Type yes or no:")
        if if_want_to_quit == "no" or if_want_to_quit == "No":
            break



main()

