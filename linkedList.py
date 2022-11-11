from node import Node

class LinkedList:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.head = None
        self.vector = []
        self.heads = []

    def bootStrap_list(self):
        for i in range(0, self.max_size):
            self.vector.append(None)
        return

    def view_list(self):
       for i in self.vector:
            if i is not None:
                print(f"[ {i} ] \n")
                print("⤵")
            else:
                print(f"[ {i} ]")


    def get_length(self):
        count = 0
        for i in range(0, len(self.vector)):
            if self.vector[i] is not None and self.vector[i].char is not None:
                count += 1
        return count

    def add_word(self, word):
        if len(word.strip()) == 0:
            raise Exception("Not possible to add empty word")

        elif self.get_length() + len(word) >= self.max_size:
            raise Exception("Low memory")

        nodes = self.transform_letter_to_node(word)

        for x in range(0, len(nodes)):
            for i in range(0, len(self.vector)):
                if self.vector[i] is None or self.vector[i].char is None:
                    self.vector[i] = nodes[x]
                    break
        return

    def transform_letter_to_node(self, word):
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

        return array

    def pop_word(self, word):
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

    def read_word(self, word):
        current_word = ""

        for i in range(len(self.heads)):
            if self.heads[i].char == word[0]:
                pointer = self.heads[i].next
                current_word += self.heads[i].char
                while pointer:
                    current_word += pointer.char
                    pointer = pointer.next

                if current_word == word:
                    print(f"The word {current_word} was found")
                else:
                    raise ValueError("this word not exist in list")

    def get_all_words(self):
        for i in self.heads:
            pointer = i.next
            print(f"[ {i.char} ]\n")
            print("⤵")
            while pointer:
                print(f"[ {pointer.char} ]\n")
                print("⤵")
                pointer = pointer.next


