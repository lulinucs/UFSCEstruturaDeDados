class VetorHash ():

    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return(len(self._data))

    def initvetor(self, tam):
        for i in range(tam):
            self._data.insert(i-1, -1)

    def procurapos(self, string):
        pos = len(string)
        if pos > len(self._data):
            while pos > len(self._data):
                pos = pos - len(self._data)
        if pos == len(self._data):
            pos = 0
        return pos

    def inserir(self, string):
        if self._size == len(vetor):
            #print('Vetor cheio.')
            return
        else:
            pos = self.procurapos(string)

            if self._data[pos] == -1 or self._data[pos] == -2:
                self._data[pos] = string
                self._size += 1

            else:
                if pos == len(self._data) - 1 and self._data != -1 and self._data != -2:
                    if self._data[0] == -1 or self._data[0] == -2:
                        self._data[0] = string
                        self._size += 1
                        return
                    else:
                        pos = 0

                while self._data[pos] != -1 and self._data[pos] != -2:
                    if pos + 1 == len(self._data) - 1:
                        if self._data[pos + 1] == -1 or self._data[pos + 1] == -2:
                            self._data[pos + 1] = string
                            self._size += 1
                            return
                        else:
                            pos = -1
                    pos += 1
                    #print(f'incrementa posição {pos}')
                self._data[pos] = string
                self._size += 1

    def remover(self, string):
        if self._size == 0:
            #print('Não há nada para remover aqui.')
            return
        else:
            pos = self.procurapos(string)
            if self._data[pos] == string:
                self._data[pos] = -2
                self._size -= 1
            else:
                while self._data[pos] != string:
                    if pos + 1 == len(self._data) - 1:
                        if self._data[pos + 1] == string:
                            self._data[pos + 1] = -2
                            self._size -= 1
                            return
                        else:
                            pos = -1
                    pos +=1
                self._data[pos] = -2
                self._size -=1


vetor = VetorHash()
entrada = -2

qtd = int(input())
vetor.initvetor(qtd)



while entrada != int(-1):
    entrada = int(input())
    if entrada == 0:
        string = input()
        vetor.inserir(string)
    elif entrada == 1:
        string = input()
        vetor.remover(string)

for i in range(len(vetor)):
    print(vetor._data[i])
