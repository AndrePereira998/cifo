from random import shuffle, choice, sample, random
from operator import attrgetter
from copy import deepcopy
import numpy as np
from random import randint

class Individual:
    def __init__(
        self,
        representation=None,
        size=None,
        replacement=True,
        indiv_array = None
    ):
        if representation is None:
            self.representation = [randint(1,9) for _ in range(size)]
            #print('criar soluçao: ')
            #print(self.representation)
            #print('###################################')
        else:
            self.representation = representation
        
        self.get_fitness(indiv_array)

    def get_fitness(self, indiv_array):
        sol_pos = 0 # auxiliar to move solution array
        indiv_array_aux = indiv_array.copy() # auxiliar to not ruin main array

        # substitute zero with solution values to calc fitness
        for pos, value in enumerate(indiv_array):
            if value == 0: 
                indiv_array_aux[pos] = self[sol_pos]
                sol_pos += 1   
                
        count = 0 
        # in case of necessary change to list use this: 
        # count += len(set(indiv_array_aux.numbers[i:i+9]))  
        
        
        for i in [0,9,18,27,36,45,54,63,72]:    #for each row
            count += len(set(indiv_array_aux[i:i+9]))  
            #print(str(i) + " row "+str(count))

        for i in range(0,9):    #for each column
            count += len(set(indiv_array_aux[i::9]))  
            #print(str(i)+" column "+str(count)) 

        for i in [0,3,6,27,30,33,54,57,60]:  # for each block
            # new_list = indiv_array_aux[i:i+3] + indiv_array_aux[i+9:i+12] + indiv_array_aux[i+18:i+21]
            con = np.concatenate((indiv_array_aux[i:i+3],indiv_array_aux[i+9:i+12],indiv_array_aux[i+18:i+21]))
            count += len(set(con))
            #print(str(i)+" block "+str(count)) 

        self.fitness = count
        #raise Exception("You need to monkey patch the fitness path.")
        return self.fitness

    def get_neighbours(self, func, **kwargs):
        raise Exception("You need to monkey patch the neighbourhood function.")

    def index(self, value):
        return self.representation.index(value)

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}"


class Population:
    def __init__(self, size, full_array,  optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.full_array = full_array
        for _ in range(size):
            print("full array")
            print(full_array)
            print('###################################')
            self.individuals.append(
                Individual(
                    size=full_array[np.where(full_array == 0)].size,
                    replacement=kwargs["replacement"],
                    indiv_array = full_array
                )
            )
    
 

    # correctly done?
    def evolve(self, gens, select, crossover=None, mutate=None, co_p=None, mu_p=None, elitism=False):
        print('entrei')
        for gen in range(gens):
            new_pop = []

            if elitism == True:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

            while len(new_pop) < self.size:
                print('selection')
                parent1, parent2 = select(self), select(self)
                print(parent1, parent2)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2
                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1)
                if random() < mu_p:
                    offspring2 = mutate(offspring2)

                new_pop.append(Individual(representation=offspring1))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2))

            if elitism == True:
                if self.optim == "max":
                    least = min(new_pop, key=attrgetter("fitness"))
                elif self.optim == "min":
                    least = max(new_pop, key=attrgetter("fitness"))
                new_pop.pop(new_pop.index(least))
                new_pop.append(elite)

            self.individuals = new_pop

            if self.optim == "max":
                print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
            elif self.optim == "min":
                print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"

if __name__ == '__main__':
    #my_path = [i for i in range(81)]
    #shuffle(my_path)
    #print(my_path)
    # my_path is an object
    #my_path = Individual(my_path)
    #print(my_path.representation)
    print('hello')