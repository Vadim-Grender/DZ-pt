n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
num_list_1=[]
for i in range(n):
    num = int(input("Введите элементы первого множества: "))
    num_list_1.append(num)
print(num_list_1)
num_list_2 = []
for i in range(m):
    num = int(input("Введите элементы второго множества: "))
    num_list_2.append(num)
print(num_list_2)
num_list3 = num_list_1 + num_list_2
num_list3.sort
for i in set(num_list3):
    if num_list3.count(i) > 1:
        print(i, end = ' ')
