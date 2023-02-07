import math
import time
import matplotlib.pyplot as plt

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

timeCounts = []
inputDataCounts = [10, 100, 1000, 10000, 100000]

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
for i in range(len(timeCounts)):
    timeCounts[i] = (int)(timeCounts[i]*1000000)
print(*timeCounts)

endPoint = max(timeCounts)

inputValuesCount = [i for i in range((int)(endPoint/len(timeCounts)), endPoint+1, (int)(endPoint/len(timeCounts)))]
print(inputValuesCount)
# Классы оценок сложности:
# O(1)
# O(log(n))
# O(n)
# O(n*log(n))
# O(n^2)
# O(n^3)
# O(2^n)

# inputValuesCount = [i for i in range(10, 1000)]
logData = [math.log(i) for i in inputValuesCount]
nData = inputValuesCount
nLogNData = [i*math.log(i) for i in inputValuesCount]
squareData = [i**2 for i in inputValuesCount]
cubeData = [i**3 for i in inputValuesCount]
expData = [2**i for i in inputValuesCount]

fig, ax = plt.subplots()
ax.set_xlim([2000, 15000])

l1 = ax.plot(inputValuesCount, logData, label = "O(log(n))")
l2 = ax.plot(inputValuesCount, nData, label = "O(n)")
l3 = ax.plot(inputValuesCount, nLogNData, label = "O(n*log(n))")
l4 = ax.plot(inputValuesCount, squareData, label = "O(n^2)")
l5 = ax.plot(inputValuesCount, cubeData, label = "O(n^3)")
#l6 = ax.plot(inputValuesCount, expData, label = "O(2^n)")
l7 = ax.plot(inputDataCounts, inputValuesCount, label = "User algorithm")
plt.yscale('log')
ax.legend(shadow=True, fancybox=True)
plt.xlabel("common X")
plt.ylabel("common Y")
plt.show()