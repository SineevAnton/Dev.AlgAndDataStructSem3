import matplotlib as plt

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


catBox = LinkedCats()
for i in range(10):
    catBox.addCat(i)
# catBox.addCat(2)
# catBox.addCat(3)
# catBox.addCat(4)
# catBox.addCat(5)

catBox.showCats(catBox.head)
catBox.reverse()
catBox.showCats(catBox.head)
#print(catBox)
