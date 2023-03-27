import random
import copy

class Graph:
    def __init__(self, graph):
        self.__matrix = graph
        self.__n = len(self.__matrix)
        self.__neighbor = self.addNeighbors()


    def getWeight(self, i, j):
        return self.__matrix[i][j]


    def addNeighbors(self):
        ans = []
        for i in range(0, self.__n):
            curr = []
            for j in range(0, self.__n):
                if self.__matrix[i][j] != 0:
                    curr.append(j)
            ans.append(curr)
        return ans


    def getCandidates(self, node, path):
        ans = []
        for nxt in self.__neighbor[node]:
            if nxt not in path:
                ans.append(nxt)
        return ans


    def randomNeighbor(self, node, path):
        candidates = self.getCandidates(node, path)
        k = len(candidates)
        if k == 0:
            return -1
        return candidates[random.randint(0, k - 1)]

    def randomPath(self, source, dest):
        path = []
        finished = False
        while not finished:
            curr = source
            finished = True
            path.clear()
            for i in range(0, self.__n - 1):
                path.append(curr)
                nxt = self.randomNeighbor(curr, path)
                curr = nxt
                if curr == -1:
                    finished = False

            path.append(curr)
            if dest not in self.__neighbor[curr]:
                finished = False

        path.append(dest)
        return path

    def checkPermutation(self, path):
        for i in range(0, len(path)):
            if path.count(path[i]) > 1 and path[i] != 0:
                return False

        for i in range(0, len(path) - 1):
            if self.__matrix[path[i]][path[i + 1]] == 0:
                return False

        return True
