import random
from chromosome import Chromosome


class Population:
    def __init__(self, iterations, popSize, fct, representation):
        self.__popSize = popSize
        self.__iterations = iterations
        self.__fct = fct
        self.__representation = representation
        self.__population = []


    def __createFirstGeneration(self):
        for _ in range(0, self.__popSize):
            DNA = self.__representation.randomPath(0, 0)
            self.__population.append(Chromosome(DNA, self.__fct, self.__representation))

    def __bestChromosome(self):
        pos = 0
        for i in range(1, self.__popSize):
            if self.__population[i].fitter(self.__population[pos]):
                pos = i

        return pos

    def __worstChromosome(self):
        pos = 0
        for i in range(1, self.__popSize):
            if not(self.__population[i].fitter(self.__population[pos])):
                pos = i

        return pos

    def __selection(self):
        # We generate randomly 2 individuals that will compete with each other
        x = self.__population[random.randint(0, self.__popSize - 1)]
        y = self.__population[random.randint(0, self.__popSize - 1)]

        # the fittest one will win the selection contest
        if x.fitter(y):
            return x
        return y


    def __steadyState(self):
        bestOffspring = None
        for _ in range(0, self.__popSize):
            chr1 = self.__selection()
            chr2 = self.__selection()

            offspring = chr1.crossover(chr2)
            offspring.mutation()
            if bestOffspring is None:
                bestOffspring = offspring
            if offspring.fitter(bestOffspring):
                bestOffspring = offspring

        worst = self.__worstChromosome()
        if bestOffspring.fitter(self.__population[worst]):
            self.__population[worst] = bestOffspring

    def __oneGeneration(self):
        newPop = []
        for _ in range(self.__popSize):
            p1 = self.__selection()
            p2 = self.__selection()
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop


    def evolutionLoop(self):
        self.__createFirstGeneration()
        bestScore = 100000000
        bestChromosome = None
        for iteration in range(0, self.__iterations):
            self.__steadyState()
            scores = []
            for chr in self.__population:
                score = chr.score()
                scores.append(score)
                if score < bestScore:
                    bestScore = score
                    bestChromosome = chr

            print(scores)

        DNA = bestChromosome.getDNA()
        file = open('output.txt', 'w')
        file.write(str(len(DNA) - 1) + '\n')

        for gene in DNA:
            file.write(str(gene) + ' ')
        file.write('\n')
        file.write(str(bestScore))

        print(bestScore)
        print(DNA)
        for i in range(0, len(DNA) - 1):
            x = DNA[i]
            y = DNA[i + 1]
            print(x, y, self.__representation.getWeight(x, y))


