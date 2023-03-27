import copy
import random


class Chromosome:
    def __init__(self, DNA, fct, representation):
        self.__representation = representation
        self.__fct = fct
        self.__n = len(DNA)
        self.__DNA = DNA

    def getDNA(self):
        return self.__DNA


    def score(self):
        return self.__fct.f(self.__DNA)

    def fitter(self, other):
        return self.score() < other.score()

    def decode(self):
        return self.__fct.getCommunities(self.__DNA)


    def mutation(self):
        i = random.randint(1, self.__n - 2)
        j = random.randint(1, self.__n - 2)
        self.__DNA[i], self.__DNA[j] = self.__DNA[j], self.__DNA[i]



    def crossover(self, other):
        offspringDNA = []

        k1 = random.randint(1, self.__n - 2)
        k2 = random.randint(k1, self.__n - 2)

        permutation = [i for i in range(1, self.__n - 1)]

        for i in range(0, self.__n):
            if i < k1 or k2 < i:
                offspringDNA.append(self.__DNA[i])
            else:
                offspringDNA.append(other.__DNA[i])
            if offspringDNA[i] in permutation:
                permutation.remove(offspringDNA[i])


        cnt = [0] * (self.__n - 1)
        for i in range(1, self.__n - 1):
            cnt[offspringDNA[i]] += 1
            if cnt[offspringDNA[i]] > 1:
                offspringDNA[i] = permutation[0]
                permutation.remove(permutation[0])


        offspring = Chromosome(offspringDNA, self.__fct, self.__representation)
        return offspring
