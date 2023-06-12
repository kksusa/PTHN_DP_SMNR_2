import CheckNumbers

def show_hex(number):
    quotient = None
    result = []
    while number != 0:
        quotient = number % 16
        match quotient:
            case 10:
                result.append("a")
            case 11:
                result.append("b")
            case 12:
                result.append("c")
            case 13:
                result.append("d")
            case 14:
                result.append("e")
            case 15:
                result.append("f")
            case _:
                result.append(str(quotient))
        number //= 16
    return result


number = CheckNumbers.integer("Введите целое число:")
if number < 0:
    number *= -1
    print('Шестнадцетиричное представление числа:\n-0x' + ''.join(show_hex(number))[::-1])
elif number == 0:
    print('Шестнадцетиричное представление числа:\n0x0')
else:
    print('Шестнадцетиричное представление числа:\n0x' + ''.join(show_hex(number))[::-1])
