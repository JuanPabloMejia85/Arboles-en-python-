#la libreria sYs no se utiliza en el codigo, entonces es innecesaria
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 


def getHeight(node):
    if not node:
        return 0
    
    return node.height

def getBalance(node):
    if not node:
        return 0

    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)
        # aqui estaba el error principal del codigo inicial
        # La correcion se hizo a partir de la rotacion, ya que no estaba retornando el nuevo balance y arbol no estaba cambiando

        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node) 
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node) 
        elif balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node) 
        
        return node 
    
    def eliminacion(self, value):
        self.root = self._eliminacion_recursiva(self.root, value)

    def _eliminacion_recursiva(self,node, value):
        if not node:
            return node
        
        if value < node.value:
            node.left = self._eliminacion_recursiva(node.left, value)
        elif value > node.value:
            node.right = self._eliminacion_recursiva(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.MinimumValueNode(node.right)
            node.value = temp.value
            node.right = self._eliminacion_recursiva(node.right, temp.value)

        updateHeight(node)
        balance = getBalance(node)

        # otra vez el balanceo para la eliminacion

        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node)
        if balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node)
        if balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        if balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node)
        
        return node
    
    def MinimumValueNode(self, node):
        if node is None or node.left is None:
            return node
        else:
            return self.MinimumValueNode(node.left)

# dividi las funciones en dos para no tener problemas con la recursividad
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)



    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.value, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value, end=" ")

    #esta es la funcion para la visualizacion 
    def imprimir_arbol(self, node=None, level=0, Y="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + Y + str(node.value))
            if node.left:
                self.imprimir_arbol(node.left, level + 1, "L--- ")
            if node.right:
                self.imprimir_arbol(node.right, level + 1, "R--- ")


avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)


print("Arbol balanceado:")
avl.imprimir_arbol()

print("\nIn-Order:")
avl.inorder()
print("\nPre-Order:")
avl.preorder()
print("\nPost-Order:")
avl.postorder()

print("Eliminando 40")
avl.eliminacion(40)

print("\nArbol despues de eliminar 40:")
avl.imprimir_arbol()