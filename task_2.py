from fractions import Fraction


def CheckFraction(param):
    while True:
        str = input(f"{param} ")
        if str.count("/") == 1:
            list = str.split("/")
            try:
                a = int(list[0])
                b = int(list[1])
                return (a, b)
            except:
                print("В дроби находятся не числа.")
        else:
            print("Вы ввели не дробь.")


def FracSum(frac1, frac2):
    print(Fraction(frac1[0], frac1[1]) + Fraction(frac2[0], frac2[1]))
    generalDenominator = frac1[1] * frac2[1]
    generalNumerator = int(frac1[0] * generalDenominator / frac1[1] + frac2[0] * generalDenominator / frac2[1])
    return (generalNumerator, generalDenominator)


def FracMult(frac1, frac2):
    print(Fraction(frac1[0], frac1[1]) * Fraction(frac2[0], frac2[1]))
    generalDenominator = frac1[1] * frac2[1]
    generalNumerator = frac1[0] * frac2[0]
    return (generalNumerator, generalDenominator)


frac1 = CheckFraction("Введите первую дробь:")
frac2 = CheckFraction("Введите вторую дробь:")
genSum = FracSum(frac1, frac2)
if genSum[0] == genSum[1]:
    print(f"{frac1[0]}/{frac1[1]} + {frac2[0]}/{frac2[1]} = 1")
else:
    print(f"{frac1[0]}/{frac1[1]} + {frac2[0]}/{frac2[1]} = {genSum[0]}/{genSum[1]}")
genMult = FracMult(frac1, frac2)
if genMult[0] == genMult[1]:
    print(f"{frac1[0]}/{frac1[1]} * {frac2[0]}/{frac2[1]} = 1")
else:
    print(f"{frac1[0]}/{frac1[1]} * {frac2[0]}/{frac2[1]} = {genMult[0]}/{genMult[1]}")
