from graph import Graph


class FitnessFunction:
    def __init__(self, graph):
        self.__graph = graph

    def f(self, path):
        if not self.__graph.checkPermutation(path):
            return 1000000
        score = 0
        for i in range(0, len(path) - 1):
            score += self.__graph.getWeight(path[i], path[i + 1])

        return score
