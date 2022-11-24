def ln(x):
    if x > 0:
        value = 10 ** 8 * ((x ** (1 / 10 ** 8)) - 1)
        return value
    else:
        return None


def log(x, base):
    if x > 0 and base > 0:
        value = ln(x) / ln(base)
        return value
    else:
        return None

k = int(input("В каком модуле хотите выполнять вычисления:\n1. Простые вычисление.\nВаш выбор - "))
print("---------------\n")
if k == 1:
    print("---------------\n")
    c = int(input("Что хотите сделать:\n1. Сложение.\n2. Вычитание.\n3. Умножение.\n4. Деление.\n5. Возведение в степень."
                  "\n6. Извлечение из под корня.\n7. Вычислить натуральный логарифм.\n8. Логарифм.\nВаш выбор -  "))
    if c == 1:
        a = int(input("Введите первое число - "))
        b = int(input("Введите второе число - "))
        print("---------------\n")
        print("Результат - ", a + b)
    if c == 2:
        a = int(input("Введите первое число - "))
        b = int(input("Введите второе число - "))
        print("---------------\n")
        print("Результат - ", a - b)
    if c == 3:
        a = int(input("Введите первое число - "))
        b = int(input("Введите второе число - "))
        print("---------------\n")
        print("Результат - ", a * b)
    if c == 4:
        a = int(input("Введите первое число - "))
        b = int(input("Введите второе число - "))
        print("---------------\n")
        print("Результат - ", a / b)
    if c == 5:
        a = int(input("Введите число - "))
        b = int(input("Введите степень - "))
        print("---------------\n")
        print("Результат - ", a ** b)
    if c == 6:
        a = int(input("Введите первое число - "))
        b = int(input("Введите степень корня - "))
        print("---------------\n")
        print("Результат - ", (a)**(1/b))
    if c == 7:
        a = int(input("Введите число - "))
        print("---------------\n")
        print("Результат - ", ln(a))
    if c == 8:
        a = int(input("Введите основание логарифма - "))
        b = int(input("Введите число логарифма - "))
        print("---------------\n")
        print("Результат - ", f"{log(b, a):.3f}")


print("Спасибо за использование нашего калькулятора")
input()
