# Найдите сумму цифр трехзначного числа.


number = input('Введите трехзначное число: ')
if len(number) != 3:
    print('Введенное число не трехначное')
else:
    sum = int(number[0]) + int(number[1]) + int(number[2])
    print(f"Сумма цифр числа {number} равна {sum}")
