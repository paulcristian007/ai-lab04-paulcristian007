from graph import Graph
from population import Population
from repository import Repository
from fitness import FitnessFunction

def main():
    repo = Repository('testfiles/file6.txt', 'output.txt')
    matrix = repo.readGraph()
    graph = Graph(matrix)
    fitness = FitnessFunction(graph)
    population = Population(200, 30, fitness, graph)
    population.evolutionLoop()


main()