import math


class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextCat = None
        self.prevCat = None

class LinkedCats:
    def __init__(self):
        self.head = None

    # Переворачиваем котиков
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

    def showCats(self, cat):
        while cat is not None:
            print(cat.cat, end=" ")
            cat = cat.nextCat
        print()

import matplotlib.pyplot as plt

catBox = LinkedCats()
for i in range(10):
    catBox.addCat(i)
# catBox.addCat(2)
# catBox.addCat(3)
# catBox.addCat(4)
# catBox.addCat(5)

data = [i for i in range(10)]

catBox.showCats(catBox.head)
catBox.reverse()
catBox.showCats(catBox.head)
#print(catBox)

# fig, simpleChart = plt.subplots()
# simpleChart.plot(data)
# plt.show()

# Классы оценок сложности:
# O(1)
# O(log(n))
# O(n)
# O(n*log(n))
# O(n^2)
# O(n^3)
# O(2^n)
inputValuesCount = [i for i in range(10, 1000)]
logData = [math.log(i) for i in inputValuesCount]
nData = inputValuesCount
nLogNData = [i*math.log(i) for i in inputValuesCount]
squareData = [i**2 for i in inputValuesCount]
cubeData = [i**3 for i in inputValuesCount]
expData = [2**i for i in inputValuesCount]

fig, ax = plt.subplots()
ax.set_ylim([0, 1000])

l1 = ax.plot(inputValuesCount, logData, label = "O(log(n))")
l2 = ax.plot(inputValuesCount, nData, label = "O(n)")
l3 = ax.plot(inputValuesCount, nLogNData, label = "O(n*log(n))")
l4 = ax.plot(inputValuesCount, squareData, label = "O(n^2)")
l5 = ax.plot(inputValuesCount, cubeData, label = "O(n^3)")
l6 = ax.plot(inputValuesCount, expData, label = "O(2^n)")
#plt.yscale('log')
ax.legend(shadow=True, fancybox=True)
plt.xlabel("common X")
plt.ylabel("common Y")
plt.show()