class Node:
    def __init__(self, char=None, next=None):
        self.char = char
        self.next = next

    def __str__(self):
        return str(self.char)
