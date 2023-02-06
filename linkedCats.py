class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextCat = None


class LinkedCats:
    def __init__(self):
        self.head = None

    # Проверка наличия котика в списке
    def contains(self, cat):
        lastBox = self.head
        while (lastBox):
            if cat == lastBox.cat:
                return True
            else:
                lastBox = lastBox.nextCat
        return False

    # Добавление котика в конец списка
    def addToEnd(self, newCat):
        newBox = Box(newCat)
        if self.head is None:
            self.head = newBox
            return
        lastBox = self.head
        while (lastBox.nextCat):
            lastBox = lastBox.nextCat
        lastBox.nextCat = newBox

    # Достаем котика по индексу
    def get(self, catIndex):
        lastBox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                return lastBox.cat
            boxIndex = boxIndex + 1
            lastBox = lastBox.nextCat

    # Прогнать котика ((
    def removeCat(self, remCat):
        headCat = self.head

        if headCat is not None:
            if headCat.cat == remCat:
                self.head = headCat.nextCat
                headCat = None
                return
        while headCat is not None:
            if headCat.cat == remCat:
                break
            lastCat = headCat
            headCat = headCat.nextCat
        if headCat == None:
            return
        lastCat.nextCat = headCat.nextCat
        headCat = None

    def showCats(self, cat):
        while cat is not None:
            print(cat.cat)
            cat = cat.nextCat


catBox = LinkedCats()
catBox.addToEnd(2)
catBox.addToEnd(3)
catBox.addToEnd(4)
catBox.addToEnd(5)

catBox.showCats(catBox.head)
#print(catBox)
