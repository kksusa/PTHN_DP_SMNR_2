import time

import CheckNumbers


def withdraw(sum):
    MIN_COMMISSION = 30
    MAX_COMMISSION = 600
    print("Снятие доступно при сумме на счёте не менее 80 у.е.")
    if 0 <= sum < 80:
        print("Вы не можете снять наличные.")
        return sum
    else:
        print("КОМИССИЯ ЗА СНЯТИЕ 1.5%, НО НЕ МЕНЕЕ 30 И НЕ БОЛЕЕ 600 У.Е.")
        while True:
            answer = CheckNumbers.more("""Введите сумму, кратную 50 у.е.
Для выхода в меню введите 0:""", -1)
            if answer == 0:
                return sum
            if answer > sum:
                print("Вы ввели сумму, превышающую доступный лимит.")
            elif answer % 50 != 0:
                print("Вы ввели сумму, не кратную 50 у.е.")
            else:
                commission = 0.015 * answer
                if commission < MIN_COMMISSION < sum - answer:
                    answer += 30
                elif commission > MAX_COMMISSION and sum - answer > MAX_COMMISSION:
                    answer += 600
                elif sum - answer > commission:
                    answer *= 1.015
                else:
                    print("Превышен лимит снятия.")
                    return sum
                sum -= answer
                print(f"\nВаш баланс: {sum:.2f} у.е.")
                return sum


def deposit(sum):
    while True:
        answer = CheckNumbers.more("""Введите сумму, которую желаете внести, кратную 50 у.е.
Для выхода в меню введите 0:""", -1)
        if answer == 0:
            return sum
        if answer % 50 == 0:
            sum += answer
            print(f"\nВаш баланс: {sum:.2f} у.е.")
            return sum
        else:
            print("Вы ввели сумму, не кратную 50 у.е.")
            continue


count = 0
sum = 0
print(f"\nВаш баланс: {sum:.2f} у.е.")
while True:
    time.sleep(1)
    sum_old = sum
    if sum > 5_000_000:
        sum *= 0.9
        print(f"""\nВаш баланс превышает 5 000 000 у.е., поэтому был списан налог на богатство 10%.
Ваш баланс: {sum:.2f} у.е.""")
    if sum_old != sum:
        count += 1
    if count > 0 and count % 3 == 0:
        sum *= 1.03
        print(f"""\nПоздравляем! Это у Вас {count}-я операция!
Вам начислены 3% от остатка на балансе.
\nВаш баланс: {sum:.2f} у.е.""")
    print("""\nВ банкомате доступно 3 операции:

1. Снятие наличных;
2. Внесение наличных;
3. Выход.\n""")
    selection = CheckNumbers.less_more("Введите номер операции:", 0, 4)
    if selection == 1:
        sum = withdraw(sum)
    elif selection == 2:
        sum = deposit(sum)
    else:
        print("Выход...")
        break
