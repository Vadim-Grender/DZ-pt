a = [int(i) for i in input('Введите номер билета: ')]
if sum(a[:3]) == sum(a[3:]):
    print('Счастливый')
else:
    print('Не счастливый')