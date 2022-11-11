from linkedList import LinkedList

list = LinkedList(32)
list.bootStrap_list()

list.add_word("Pernambuco")
list.add_word("São Paulo")
list.add_word("Alagoas")

list.pop_word("São Paulo")
list.add_word("Santa Catarina")
list.view_list()