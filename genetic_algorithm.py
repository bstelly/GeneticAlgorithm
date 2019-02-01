from random import randint
import copy

class GeneticAlgorithm:
    def __init__(self):
        self.equation = Equation()
        self.population = []
        self.time = 0

    def initialize_population(self, size):
        for x in range(0, size):
            solution = ''
            for x in range(0, len(self.equation.variables)):
                solution += str(randint(0, 1))

            self.population.append(Gene(solution))
            
    def fitness_selection(self):
        parent_one = None
        parent_two = None

        fitness_sum = 0
        for x in self.population:
            fitness_sum += x.fitness

        for x in range(0, 2):
            number = randint(0, fitness_sum)

            partial_sum = 0
            for x in self.population:
                partial_sum += x.fitness
                if partial_sum > number:
                    if parent_one is None:
                        parent_one = x
                    else:
                        parent_two = x
                    break
        return (parent_one, parent_two)

    def crossover(self, parents, pivot):
        offspring_one = ""
        offspring_two = ""
        length = len(parents[0].solution)

        for x in range(0, length):
            if x < pivot:
                offspring_one += parents[1].solution[x]
            else:
                offspring_one += parents[0].solution[x]
            if x >= pivot:
                offspring_two += parents[1].solution[x]
            else:
                offspring_two += parents[0].solution[x]
        parents[0].solution = offspring_one
        parents[1].solution = offspring_two

    def mutate(self, parents, rate):
        gene_one = list(parents[0].solution)
        gene_two = list(parents[1].solution)
        parents[0].solution = ''
        parents[1].solution = ''
        
        itr = 0
        for x in gene_one:
            if randint(0, 100) <= rate:
                gene_one[itr] = '1' if x is '0' else '0'
            itr += 1
        itr = 0
        for y in gene_two:
            if randint(0, 100) <= rate:
                 gene_two[itr]= '1' if x is '0' else '0'
            itr += 1
        parents[0].solution = parents[0].solution.join(gene_one)
        parents[1].solution = parents[1].solution.join(gene_two)


        
            
                

    def run(self):
        self.equation.load_file('equation.txt')
        self.equation.find_variables()

        #set time t = 0
        self.time = 0
        #initialize population
        self.initialize_population(5)
        
        #while termination condition is not met, do
        while self.time != 5:
            #evaluate the fitness of each gene
            for gene in self.population:
                gene.calc_fitness(self.equation)
            
            #Select members from the population based on fitness
            parents = self.fitness_selection()

            #produce the offspring of these pairs using genetic operators
            self.crossover(parents, (len(self.population[0].solution) * .5))
            self.mutate(parents, 20)
            self.time += 1
            

        


class Equation:
    def __init__(self):
        self.problem = ''
        self.variables = []

    def load_file(self, filename):
        with open(filename, 'r') as myFile:
            self.problem = myFile.read()
        myFile.close()

    def find_variables(self):
        for x in self.problem:
            if x is not ' ' and x is not '(' and x is not ')' and x is not '!' and x is not '*' and x is not '+':
                if not self.variables.__contains__(x):
                    self.variables.append(x)
        self.variables.sort()

    def replace_symbols(self):
        self.problem = self.problem.replace("!", str("not "))
        self.problem = self.problem.replace("+", str("or"))
        self.problem = self.problem.replace("*", str("and"))



class Gene:
    def __init__(self, solution):
        self.solution = solution
        self.fitness = 0
        
    def calc_fitness(self, equation):
        self.fitness = 0
        eq = copy.deepcopy(equation)
        
        for i in range(0, len(eq.variables)):
            eq.problem = eq.problem.replace(eq.variables[i], self.solution[i])

        eq.replace_symbols()
        clauses = eq.problem.split("and")

        count = 0
        for x in clauses:
            if eval(x) is True or eval(x) is 1:
                count += 1
        self.fitness = count
            


algorithm = GeneticAlgorithm()
algorithm.run()
