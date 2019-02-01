from random import randint
import copy

class GeneticAlgorithm:
    #initialize the GeneticAlgorithm class
    def __init__(self):
        self.equation = Equation()
        self.population = []
        self.current_solution = None

    #fill the population list with genes. The genes each have a random solution
    def initialize_population(self, size):
        for x in range(0, size):
            solution = ''
            for x in range(0, len(self.equation.variables)):
                solution += str(randint(0, 1))

            self.population.append(Gene(solution))
            
    #select two parent genes by using roulette wheel selection
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
                if partial_sum >= number:
                    if parent_one is None:
                        parent_one = x
                    else:
                        parent_two = x
                    break
        return (parent_one, parent_two)

    #A genetic operator that allows two parents to create "children" by combining
    #genetic information
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

    #A genetic operator that helps to maintain genetic diversity by rolling a random
    #number from one to 100 for each bit in both parent's solutions.
    #if the number is less than the rate, then that bit will become a 1 if 0 or a 0 if 1
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
        parents[0].solution = ''.join(str(x) for x in gene_one)
        parents[1].solution = ''.join(str(y) for y in gene_two)

    #checks to see if any genes in the population contain a solution that satisfies
    #the expression
    def check_for_solution(self):
        for x in self.population:
            eq = copy.deepcopy(self.equation)
            for i in range(0, len(eq.variables)):
                eq.problem = eq.problem.replace(eq.variables[i], x.solution[i])
            eq.replace_symbols()
            evaluation = eval(eq.problem)
            if eval(eq.problem) is True or eval(eq.problem) is 1:
                self.current_solution = x
                break

    #runs the genetic algorithm
    def run(self):
        self.equation.load_file('equation.txt')
        self.equation.find_variables()

        #initialize population
        self.initialize_population(5)
        
        #while termination condition is not met continue looping
        while self.current_solution is None:
            #evaluate the fitness of each gene
            for gene in self.population:
                gene.calc_fitness(self.equation)
            
            #Select members from the population based on fitness
            parents = self.fitness_selection()

            #produce the offspring of these pairs using genetic operators
            self.crossover(parents, (len(self.population[0].solution) * .5))
            self.mutate(parents, 20)

            #check to see if a solution is found. If one is found, the algorithm will stop running
            self.check_for_solution()

        print(self.current_solution.solution)
            
        


class Equation:
    #initialize the Equation class
    def __init__(self):
        self.problem = ''
        self.variables = []

    #takes in a string for the file name and loads the contents into a member variable
    def load_file(self, filename):
        with open(filename, 'r') as myFile:
            self.problem = myFile.read()
        myFile.close()

    #finds every unique literal in the expression
    def find_variables(self):
        for x in self.problem:
            if x is not ' ' and x is not '(' and x is not ')' and x is not '!' and x is not '*' and x is not '+':
                if not self.variables.__contains__(x):
                    self.variables.append(x)
        self.variables.sort()

    #replaces operators in the expression, with python logical operators
    def replace_symbols(self):
        self.problem = self.problem.replace("!", str("not "))
        self.problem = self.problem.replace("+", str("or"))
        self.problem = self.problem.replace("*", str("and"))



class Gene:
    #initializes the Gene class
    def __init__(self, solution):
        self.solution = solution
        self.fitness = 0
        
    #calculates the fitness of a gene by checking how many of the expressions
    #clauses are evaluated to true using the gene's solution
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
solution = algorithm.run()

