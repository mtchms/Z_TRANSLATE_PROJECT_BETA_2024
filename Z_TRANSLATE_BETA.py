# Z_TRANSLATE v 3.2 (Leonid Zaporozhets 2024)
import random


def atoi(s, p):
    digit = {char: i for i, char in enumerate("0123456789ABCDEF")}
    a = 0
    for char in s:
        a = a * p + digit[char]
    return a


def itoa(a, p):
    result = ""
    while a:
        result = "0123456789ABCDEF"[a % p] + result
        a //= p
    return result if result else "0"


def generate_number():
    return random.randint(1, 1000)


def generate_number_medium():
    return random.randint(500, 1500)


def generate_number_hard():
    return random.randint(1000, 2500)


def convert_to_base(number, base):
    if base == 2:
        return bin(number)[2:]
    elif base == 8:
        return oct(number)[2:]
    elif base == 10:
        return str(number)
    elif base == 16:
        return hex(number)[2:]
    else:
        return None


def check_answer(number, answer, base):
    converted_number = convert_to_base(number, base)
    return answer == converted_number


def check_number_in_base(number, base_from):
    try:
        int(number, base_from)
        return True
    except ValueError:
        return False


def main():
    while True:
        print("Введите слово 'меню' для выбора режима или 'стоп' для завершения: ")
        user_input = input().lower()

        if user_input == "стоп":
            break
        elif user_input == "меню":
            while True:
                print("Меню:")
                print("1. Режим перевода чисел между системами счисления")
                print(
                    "В этом режиме вы можете ввести своё число, систему этого числа, потом ту систему,")
                print(
                    "куда бы вы хотели его перевести, после чего получите готовый результат.")
                print()
                print("2. Режим тренировки")
                print("В этом режиме вы можете потренироваться с переводом чисел,")
                print(
                    "вам будет предложено число в десятичной системе, после чего вам будет предложена")
                print("та система, в которую нужно перевести данное число.")
                print()
                choice = int(input("Выберите режим (1 или 2): "))

                if choice == 1:
                    while True:
                        number = input(
                            "Введите число (для выхода в главное меню напишите 'стоп'): ")
                        if number == 'стоп':
                            break
                        else:
                            base_from = int(
                                input("Введите начальную систему счисления: "))
                            if base_from == 0:
                                print("Такой системы счисления не существует.")
                                print()
                                break
                            if base_from == 1:
                                print(
                                    "Единичная система счисления не является полноценной, введите другую.")
                                print()
                                break
                            if check_number_in_base(number, base_from) == False:
                                print(
                                    "Такого числа нету в данной системе счисления. ")
                                print("Вы возвращены в меню.")
                                print()
                                break
                            elif check_number_in_base(number, base_from) == True:
                                base_to = int(
                                    input("Введите конечную систему счисления: "))
                                if base_to == 0:
                                    print(
                                        "Такой системы счисления не существует.")
                                    print()
                                    break
                                if base_to == 1:
                                    print(
                                        "Единичная система счисления не является полноценной, введите другую.")
                                    print()
                                    break
                                else:
                                    result = itoa(
                                        atoi(number, base_from), base_to)
                                    print(f"Результат перевода: {result}\n")
                elif choice == 2:
                    user_tr_counter = 0
                    user_tr_counter_1 = 0
                    user_tr_counter_for_res = 0
                    print("Выберите режим:")
                    print(
                        "1. Тест, вам будет предложено 10 вопросов, на которые вам престоит ответить и получить свой счёт решенных верно задач.")
                    print("2. Бесконечный режим, в нем вы сможете бесконечно решать задачи пока не ошибетесь, после чего получите свой счёт решенных верно задач.")
                    choice_1 = int(input("Выберите режим (1 или 2): "))
                    if choice_1 == 1:
                        user_input_dif = input(
                            "Введите сложность, в которой желаете испытать себя (легко, средне, сложно, ваша собственная (Введите 'Z')):\n")
                        if user_input_dif == "Z":
                            user_input_custom_dif_0 = int(input(
                                "Количество цифр в числе. (Введите любое число от 1 до бесконечности): "))
                            user_input_custom_dif_1 = int(input(
                                "Количество вопросов. (Введите любое число от 1 до бесконечности): "))
                            user_min_dig = (
                                int("1" + "0" * (user_input_custom_dif_0 - 1)))
                            user_max_dig = (
                                int("1" + "0" * (user_input_custom_dif_0)) - 1)
                            for i in range(1, user_input_custom_dif_1 + 1):
                                number = random.randint(
                                    user_min_dig, user_max_dig)
                                base = random.choice([2, 8, 16])
                                converted_number = convert_to_base(
                                    number, base)
                                print(
                                    f"{i}.Число {number} в систему счисления {base}:")
                                user_answer = input(
                                    "Введите перевод в другую систему счисления (если в вашем ответе есть буква, то она должна быть в нижнем регистре), либо 'стоп' для выхода в меню: ")
                                if user_answer.lower() == "стоп":
                                    break
                                if check_answer(number, user_answer, base):
                                    user_tr_counter += 1
                                    user_tr_counter_for_res += 1
                                else:
                                    user_tr_counter_for_res += 1
                            if user_tr_counter == 0:
                                print(
                                    f"Ваш результат {user_tr_counter}, но вы можете лучше!!!")
                            elif user_tr_counter > 0 and user_tr_counter <= user_tr_counter_for_res // 2:
                                print(
                                    f"Ваш результат {user_tr_counter}, не мешало бы еще потренироваться.)")
                            elif user_tr_counter > 5 and user_tr_counter <= user_tr_counter_for_res // 100 * 90:
                                print(
                                    f"Ваш результат {user_tr_counter}, очень неплохо.")
                            elif user_tr_counter == user_tr_counter_for_res:
                                print(
                                    f"Ваш результат {user_tr_counter}, вы полностью познали системы счисления.")
                        if user_input_dif == "легко":
                            for i in range(1, 11):
                                number = generate_number()
                                base = random.choice([2, 8, 16])
                                converted_number = convert_to_base(
                                    number, base)
                                print(
                                    f"{i}.Число {number} в систему счисления {base}:")
                                user_answer = input(
                                    "Введите перевод в другую систему счисления (если в вашем ответе есть буква, то она должна быть в нижнем регистре), либо 'стоп' для выхода в меню: ")
                                if user_answer.lower() == "стоп":
                                    break
                                if check_answer(number, user_answer, base):
                                    user_tr_counter += 1
                            if user_tr_counter == 0:
                                print(
                                    f"Ваш результат {user_tr_counter}, но вы можете лучше!!!")
                            elif user_tr_counter > 0 and user_tr_counter <= 5:
                                print(
                                    f"Ваш результат {user_tr_counter}, не мешало бы еще потренироваться.)")
                            elif user_tr_counter > 5 and user_tr_counter <= 9:
                                print(
                                    f"Ваш результат {user_tr_counter}, очень неплохо.")
                            elif user_tr_counter == 10:
                                print(
                                    f"Ваш результат {user_tr_counter}, вы полностью познали системы счисления.")
                        if user_input_dif == "средне":
                            for i in range(1, 16):
                                number = generate_number_medium()
                                base = random.choice([2, 8, 16])
                                converted_number = convert_to_base(
                                    number, base)
                                print(
                                    f"{i}.Число {number} в систему счисления {base}:")
                                user_answer = input(
                                    "Введите перевод в другую систему счисления (если в вашем ответе есть буква, то она должна быть в нижнем регистре), либо 'стоп' для выхода в меню: ")
                                if user_answer.lower() == "стоп":
                                    break
                                if check_answer(number, user_answer, base):
                                    user_tr_counter += 1
                            if user_tr_counter == 0:
                                print(
                                    f"Ваш результат {user_tr_counter}, но вы можете лучше!!!")
                            elif user_tr_counter > 0 and user_tr_counter <= 5:
                                print(
                                    f"Ваш результат {user_tr_counter}, не мешало бы еще потренироваться.)")
                            elif user_tr_counter > 5 and user_tr_counter <= 9:
                                print(
                                    f"Ваш результат {user_tr_counter}, очень неплохо.")
                            elif user_tr_counter == 10:
                                print(
                                    f"Ваш результат {user_tr_counter}, вы полностью познали системы счисления.")
                        if user_input_dif == "сложно":
                            for i in range(1, 21):
                                number = generate_number_hard()
                                base = random.choice([2, 8, 16])
                                converted_number = convert_to_base(
                                    number, base)
                                print(
                                    f"{i}.Число {number} в систему счисления {base}:")
                                user_answer = input(
                                    "Введите перевод в другую систему счисления (если в вашем ответе есть буква, то она должна быть в нижнем регистре), либо 'стоп' для выхода в меню: ")
                                if user_answer.lower() == "стоп":
                                    break
                                if check_answer(number, user_answer, base):
                                    user_tr_counter += 1
                            if user_tr_counter == 0:
                                print(
                                    f"Ваш результат {user_tr_counter}, но вы можете лучше!!!")
                            elif user_tr_counter > 0 and user_tr_counter <= 5:
                                print(
                                    f"Ваш результат {user_tr_counter}, не мешало бы еще потренироваться.)")
                            elif user_tr_counter > 5 and user_tr_counter <= 9:
                                print(
                                    f"Ваш результат {user_tr_counter}, очень неплохо.")
                            elif user_tr_counter == 10:
                                print(
                                    f"Ваш результат {user_tr_counter}, вы полностью познали системы счисления.")
                    elif choice_1 == 2:
                        while True:
                            number = generate_number()
                            base = random.choice([2, 8, 16])
                            converted_number = convert_to_base(number, base)
                            print(
                                f"Число {number} в систему счисления {base}:")
                            user_answer = input(
                                "Введите перевод в другую систему счисления (если в вашем ответе есть буква, то она должна быть в нижнем регистре), либо 'стоп' для выхода в меню: ")
                            if user_answer.lower() == "стоп":
                                break
                            if check_answer(number, user_answer, base):
                                print("Правильно!\n")
                                user_tr_counter_1 += 1
                            else:
                                print(
                                    f"Неправильно. Правильный ответ: {converted_number}\n")
                                print(
                                    f"Вы допустили ошибку, ваш счетчик правильно решенных подряд примеров: {user_tr_counter_1}\n")
                                print("Вы возвращены в главное меню")
                                break
                else:
                    print("Неверный выбор. Попробуйте снова.\n")
        else:
            print("Слово 'меню' не было введено. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
