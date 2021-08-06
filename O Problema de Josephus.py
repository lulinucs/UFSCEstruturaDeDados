class ListaCircular:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._tail = None
        self._killer = None
        self._size = 0

    def __str__(self):
        if self.is_empty():
            return str([list])
        to_print = []
        pivot = self._tail._next
        while pivot != self._tail:
            to_print.append(pivot._element)
            pivot = pivot._next
        to_print.append(pivot._element)
        return str(to_print)

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def push(self, elem):
        new_node = self._Node(elem, None)
        if self.is_empty():
            self._tail = new_node
            self._tail._next = self._tail
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
            self._tail = self._tail._next
        self._size += 1

    def cleanlist(self):
        self._tail = None
        self._killer = None
        self._size = 0

    def insertsoldiers(self, quant):
        for x in range(quant):
            x += 1
            self.push(x)

    def removefirst(self, m):
        pivot = self._tail._next
        idx = 1
        while idx < m:
            pivot = pivot._next
            idx += 1
        if pivot._next == self._tail:
            self._tail = pivot
        elif pivot._next == self._tail._next:
            pivot = pivot._next
        dead = pivot._next._element
        pivot._next = pivot._next._next
        self._killer = pivot._next
        '''print(f'Soldado 1 matou o soldado {dead}. Soldado {self._killer._element} é o próximo a matar!')'''
        self._size -= 1

    def remove(self, m):
        pivot = self._killer
        killer = self._killer._element
        idx = 1
        while idx < m:
            pivot = pivot._next
            idx += 1
        if pivot._next == self._tail:
            self._tail = pivot
        if pivot._next == self._killer:
            pivot = pivot._next
        dead = pivot._next._element
        pivot._next = pivot._next._next
        self._killer = pivot._next
        '''if self._size < 3:
            print(f'Soldado {killer} matou o soldado {dead} e soldado {killer} é o último sobrevivente!')
        else:            
            print(f'Soldado {killer} matou o soldado {dead}. Soldado {self._killer._element} é o próximo a matar!')'''
        self._size -= 1
        return self._killer._element

    def startthekilling(self, m):
        self.removefirst(m)
        result = 1
        while self._size > 1:
            result = self.remove(m)
        return result

    def solveJosephus(self, n, m):
        self.cleanlist()
        self.insertsoldiers(n)
        result = self.startthekilling(m)
        print(f'Usando n={n}, m={m}, resultado={result}')
        return result


circulo = ListaCircular()

casos = int(input())
n = []
m = []

for x in range(casos):
    n.append(int(input()))
    m.append(int(input()))

for x in range(casos):
    circulo.solveJosephus(n[x], m[x])
