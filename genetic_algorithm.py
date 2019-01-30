class GeneticAlgorithm:
    def __init__(self):
        self.equation = ''
        self.population = []
        self.time = 0

    def initialize_population(self, size):
        for x in range(0, size):
            


    def run(self):
        #set time   t = 0
        #initialize population
        #While the termination condition is not met, do
            #begin
                #evaluate the fitness of each gene
                #Select members from the population based on fitness
                #produce the offspring of these pairs using genetic operators
                #replace based on fitness, candidates of population, with these offspring
                #set time += 1
            #end
        #end
        time = 0


class Equation:
    def __init__(self):
        self.clauses = []
        self.variables = []



class Gene:
    def __init__(self, solution, fitness):
        self.solution = solution
        self.fitness = fitness
        
    def calc_fitness(self, equation):
        self.fitness = 0
        count = 0

        for x in equation.clauses:
            for y in variable_values:
                equation = equation.replace(x[0], x[1])
            