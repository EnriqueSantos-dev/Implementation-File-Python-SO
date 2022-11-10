from node import Node

class LinkedList:
    def __init__(self):
        self.size = None
        self.head = None
        self.vector = []
        self.heads = []

    def bootStrapList(self, quant):
        self.size = quant
        for i in range(0, quant):
            self.vector.append(None)
        return

    def viewList(self):
       for i in self.vector:
            if i is not None:
                print(f"[ {i} ] \n")
                print("⤵")
            else:
                print(f"[ {i} ]")


    def getLength(self):
        count = 0
        for i in range(0, len(self.vector)):
            if self.vector[i] is not None and self.vector[i].char is not None:
                count += 1
        return count

    def addWord(self, word):
        if len(word.strip()) == 0:
            raise Exception("Not possible to add empty word")

        elif self.size - self.getLength() < len(word):
            raise Exception("Low memory")

        array = []
        for char in word:
            word = Node(char)
            array.append(word)

        for node in range(0, len(array)):
            if node == len(array) - 1:
                array[node].next = None
            else:
                array[node].next = array[node + 1]

        self.heads.append(array[0])

        for x in range(0, len(array)):
            for i in range(0, len(self.vector)):
                if self.vector[i] is None or self.vector[i].char is None:
                    self.vector[i] = array[x]
                    break
        return

    def popWord(self, word):
        current_word = ""
        pointers = []
        pointerHead = None

        for i in self.heads:
            current_word += i.char
            pointers.append(i)
            pointer = i.next
            pointers.append(pointer)
            while pointer.next:
                current_word += pointer.char
                pointer = pointer.next
                pointers.append(pointer)
            if pointer.next is None:
                current_word += pointer.char
            if current_word == word:
                current_word = ""
                pointerHead = i
                break
            else:
                current_word = ""
                pointers = []

        if len(pointers) > 0:
            for p in pointers:
                p.char = None
                p.next = None

            pointers = []
            self.heads.remove(pointerHead)
            return

    def readWord(self, word):
        current_word = ""

        for i in range(len(self.heads)):
            if self.heads[i].char == word[0]:
                pointer = self.heads[i].next
                current_word += self.heads[i].char
                while pointer:
                    current_word += pointer.char
                    pointer = pointer.next

                if current_word == word:
                    return (f"The word {current_word} was found")
                else:
                    raise ValueError("this word not exist in list")

    def getAllWords(self):
        for i in self.heads:
            pointer = i.next
            print(f"[ {i.char} ]\n")
            print("⤵")
            while pointer:
                print(f"[ {pointer.char} ]\n")
                print("⤵")
                pointer = pointer.next


list = LinkedList()
list.bootStrapList(32)

list.addWord("Pernambuco")
list.addWord("São Paulo")
list.addWord("Alagoas")

list.popWord("São Paulo")
list.addWord("Santa Catarina")
list.viewList()
