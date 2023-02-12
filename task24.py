n = int(input('Ведите кол-во кустов: '))
berries = []
for i in range(n):
    num = int(input("Введите кол-во ягод на кусте: "))
    berries.append(num)
berries_count = []
for i in range(len(berries) - 1):
    berries_count.append(berries[i - 1] + berries[i] + berries[i + 1])
berries_count.append(berries[-2] + berries[-1] + berries[0])    
print(max(berries_count))