import random

class Generator:
    def __init__(self, filepath, n_min, n_max):
        self.__filepath = filepath
        self.__n_min = n_min
        self.__n_max = n_max

    def createRandomGraph(self):
        n = random.randint(self.__n_min, self.__n_max)
        m = int(n * (n - 1) / 2)

        neighbors = []
        nodes = []
        for i in range(0, n):
            neighbors.append([])
            nodes.append(i)
            for j in range(0, n):
                if i != j:
                    neighbors[i].append(j)

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for _ in range(0, m):
            i = nodes[random.randint(0, len(nodes) - 1)]
            j = neighbors[i][random.randint(0, len(neighbors[i]) - 1)]
            k = random.randint(1, 9)
            matrix[i][j] = k
            matrix[j][i] = k
            neighbors[i].remove(j)
            neighbors[j].remove(i)

            if len(neighbors[i]) == 0:
                nodes.remove(i)
            if len(neighbors[j]) == 0:
                nodes.remove(j)


        return matrix

    def writeToFile(self):
        matrix = self.createRandomGraph()
        n = len(matrix)

        self.__filepath(open)
        self.__filepath.write(str(n) + '\n')
        for i in range(0, n):
            for j in range(0, n):
                self.__filepath.write(str(matrix[i][j]) + " ")
            self.__filepath.write('\n')

        source = random.randint(0, n)
        destination = random.randint(0, n)

        self.__filepath.write(str(source) + '\n')
        self.__filepath.write(str(destination) + '\n')

        self.__filepath.close()

