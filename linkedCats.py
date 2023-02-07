# Импорт нужных библиотек
import math
import time
import matplotlib.pyplot as plt

# Коробки для кошек
class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextCat = None
        self.prevCat = None

# Описание котиков
class LinkedCats:
    def __init__(self):
        self.head = None

    # Переворачиваем котиков
    # В методе всего один цикл, сложность = O(n)
    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prevCat
            current.prevCat = current.nextCat
            current.nextCat = temp
            current = current.prevCat

        if temp is not None:
            self.head = temp.prevCat

    # Проверка наличия котика в списке
    def contains(self, cat):
        lastBox = self.head
        while (lastBox):
            if cat == lastBox.cat:
                return True
            else:
                lastBox = lastBox.nextCat
        return False

    # Добавление котика
    def addCat(self, newCat):
        newBox = Box(newCat)
        newBox.nextCat = self.head
        if self.head is not None:
            self.head.prevCat = newBox
        self.head = newBox


    # Достаем котика по индексу
    def get(self, catIndex):
        lastBox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                return lastBox.cat
            boxIndex = boxIndex + 1
            lastBox = lastBox.nextCat

    # Выставка кошек
    def showCats(self, cat):
        while cat is not None:
            print(cat.cat, end=" ")
            cat = cat.nextCat
        print()

timeCounts = [] # Тут будем хранить значения времени, за которое отработала сортировка
inputDataCounts = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000] # Значения количества входных данных (столько котиков создадим)

# Для каждого значения количества входных параметров создаем соответствующее количество котиков
# переворичиваем их, вычисляя время разворота и записывая его в массив выше
# Строки закомментированы чтобы не засорять консоль большими выводами
for el in inputDataCounts:
    catBox = LinkedCats()
    for i in range(el):
        catBox.addCat(i)

    #catBox.showCats(catBox.head)
    start = time.time()
    catBox.reverse()
    end = time.time()
    #catBox.showCats(catBox.head)
    timeCounts.append(end - start)


print(*timeCounts)
times = timeCounts
# Логика для работы с данными для графиков:
# Суть - линейно преобразовать значения времени, чтобы не осталось значений < 0
# так как для таких значений возведение в степень сломает график
for i in range(len(timeCounts)):
    timeCounts[i] = (int)(timeCounts[i]*1000000)
print(*timeCounts)

endPoint = max(timeCounts) # Эта точка нужна для искуственной генерации данных для построения графиков сложности

# Искуственные данные (точки), ограниченные максимальным временем работы исследуемого алгоритма, используются
# Для построения графиков сложности

SinteticData = [i for i in range((int)(endPoint/len(timeCounts)), endPoint+1, (int)(endPoint/len(timeCounts)))]
print(SinteticData)

# Классы оценок сложности:
# O(1)
# O(log(n))
# O(n)
# O(n*log(n))
# O(n^2)
# O(n^3)
# O(2^n)

# Данные для графиков сложности

logData = [math.log(i) for i in SinteticData]
nData = SinteticData
nLogNData = [i*math.log(i) for i in SinteticData]
squareData = [i**2 for i in SinteticData]
cubeData = [i**3 for i in SinteticData]
expData = [2**i for i in SinteticData]

# Запускаем рисовалку
fig, ax = plt.subplots()
# ax.set_xlim([2000, 15000])

l1 = ax.plot(SinteticData, logData, label = "O(log(n))")
l2 = ax.plot(SinteticData, nData, label = "O(n)")
l3 = ax.plot(SinteticData, nLogNData, label = "O(n*log(n))")
l4 = ax.plot(SinteticData, squareData, label = "O(n^2)")
l5 = ax.plot(SinteticData, cubeData, label = "O(n^3)")
#l6 = ax.plot(inputValuesCount, expData, label = "O(2^n)") # Убрал, так как сильно большие числа
l7 = ax.plot(times, inputDataCounts, label = "User algorithm")
plt.yscale('log') # Нагляднее получается
ax.legend(shadow=True, fancybox=True)
plt.xlabel("Sintetic time (log)")
plt.ylabel("Input data count (log)")
plt.show()