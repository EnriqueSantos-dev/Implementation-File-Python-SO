from linkedList import LinkedList

list = LinkedList(32)
list.bootStrapList()

list.addWord("Pernambuco")
list.addWord("São Paulo")
list.addWord("Alagoas")

list.popWord("São Paulo")
list.addWord("Santa Catarina")
list.viewList()