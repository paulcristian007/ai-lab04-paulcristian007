

class Repository:
    def __init__(self, inputFile, outputFile):
        self.__inputFile = inputFile
        self.__outputFile = outputFile
        self.readGraph()

    def readGraph(self):
        file = open(self.__inputFile, 'r')

        line = file.readline()
        numbers = line.split()
        n = int(numbers[0])

        matrix = []
        for i in range(0, n):
            currLine = []
            line = file.readline()
            numbers = line.split()
            for j in range(0, n):
                currLine.append(int(numbers[j]))

            matrix.append(currLine)

        file.close()
        return matrix




    