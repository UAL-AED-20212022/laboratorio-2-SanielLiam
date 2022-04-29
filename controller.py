from model import Node
form View import view

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("Lista sem elemento")
            return
        else:
            n =  self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref
                
    
    def Registrar_Pais__Final(self, pais):
        new_node = Node(pais)

        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.view.RPF
        while n.ref is not None:
            n = n.ref
        n.ref = self.view.RPI()


    def Registar_País_Inicial(self, pais):
        new_node = Node(pais)
        new_node.ref = self.view.RPI()
        self.view.RPI = new_node


    def Registrar_País_Depois_Elemento(self, x, pais):
        n = self.view.PRDE
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("País não está na lista")
        else:
            new_node = Node(pais)
            new_node.ref = n.ref
            n.ref = new_node
            print("Pais novo registrado")

    def Registrar_País_Antes_Elemento(self, x, pais):
        if self.start_node is None:
            print("Lista não tem elementos")
            return
        
        if x == self.start_node.item:
            new_node = Node(pais)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.view.RPAE()
        print(n.ref)
        while n.ref is not None:
            if n.ref.item is not None:
                if n.ref.item == x:
                    break 
                n = n.ref

        if n.ref is None:
            print("País não encontrado")
        else:
            new_node = Node(pais)
            new_node.ref = n.ref
            n.ref = new_node
            
    def Registrar_País_índice(self, index, pais):
        if index == 1:
            new_node = Node(pais)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.view.RPII
        while i < index-1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(pais)
            new_node.ref = n.ref
            n.ref = new_node

    def Verificar_Número_Elementos(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0

        while n is not None:
            count += 1
            n = n.ref
        return count
    print("O número de Elemento são {}".format(Verificar_Número_Elementos))
    

    def Verificar_País(self, x):
        if self.view.VP is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("O país {} encontra-se na lista".format(VP))
                return True
            n = n.ref
        print("O país {} não encontra-se na lista".format(VP))
        return False

    def Eliminar_Primeiro_Elemento(self):
        if self.view.EPE() is None:
            print("The list has no element to delete")
            return
        self.start_node = self.view.EPE
        print("O pais {} foi eliminado da lista".format(EPE))

    def Eliminar_Ultimo_Elemento(self):
        if self.start_node is None:
            print("Está lista não tem elemento pra deletar")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref

    def Eliminar_País(self, x):
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.view.EP
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("O pais {} não se encontra na lista".format(EP))

        else:
            n.ref = n.ref.ref
            

lista = LinkedList
lista.RPI 
lista.traverse_list()
lista.RPF 
lista.traverse_list
lista.RPDE 
lista.traverse_list
lista.RPAE
lista.traverse_list
lista.RPII 
lista.traverse_list
lista.Verificar_Número_Elementos
lista.VP 
lista.EPE 
lista.EUE 
lista.EP 
