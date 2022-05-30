from random import shuffle, choice, sample, random
from operator import attrgetter
from copy import deepcopy
import numpy as np
from random import randint
import csv
from pathlib import Path

class Individual:
    def __init__(
        self,
        representation=None,
        size=None,
        replacement=True,
        indiv_array = None
    ):
        if representation is None:
            # print(self.indiv_optim)
            self.representation = [randint(1,9) for _ in range(size)]
            
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
            
        for i in range(0,9):    #for each column
            count += len(set(indiv_array_aux[i::9]))   

        for i in [0,3,6,27,30,33,54,57,60]:  # for each block
            con = np.concatenate((indiv_array_aux[i:i+3],indiv_array_aux[i+9:i+12],indiv_array_aux[i+18:i+21]))
            count += len(set(con))

        self.fitness = count

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
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness};"


class Population:
    def __init__(self, size, full_array,  optim, filename=None, folder=None, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.full_array = full_array
        self.folder = folder
        self.filename = filename
        self.gen = 1
        for _ in range(size):
            
            self.individuals.append(
                Individual(
                    size=full_array[np.where(full_array == 0)].size,
                    replacement=kwargs["replacement"],
                    indiv_array = full_array.copy()
                )
            )
    
 


    def evolve(self, gens, select, crossover=None, mutate=None, co_p=None, mu_p=None, elitism=False, full_array_evolve=None,log=False):
        
        for gen in range(gens):
            new_pop = []
            
            if elitism == True:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

            while len(new_pop) < self.size:
                
                parent1, parent2 = select(self), select(self)
    
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1.representation, parent2.representation)
                else:
                    offspring1, offspring2 = parent1.representation, parent2.representation

                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1)
                if random() < mu_p:
                    offspring2 = mutate(offspring2)

                new_pop.append(Individual(representation=offspring1, indiv_array=full_array_evolve))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2, indiv_array=full_array_evolve))

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
            
            if log:
                self.log(gens)
            self.gen += 1

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"

    def log(self, num_gens):
        """ Creation of csv file with best fitness of every generation """
        best_indiv = max(self, key=attrgetter("fitness"))
        i=0
        my_file = Path(fr"./{self.folder}/{self.filename}.csv")

        # Counting the number of lines if the file exists
        if my_file.is_file():
            with open(fr"./{self.folder}/{self.filename}.csv") as f:
                for i, l in enumerate(f):
                    pass

        # Check if first generation is yet to complete
        if i < num_gens - 1:
            with open(fr"./{self.folder}/{self.filename}.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.gen, best_indiv.fitness])
        # if first generation is complete, then add new fitness value to the end of the line
        
        else:
            with open(fr"./{self.folder}/{self.filename}.csv", 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.split(',')[0] == f"{self.gen}":
                        lines[i] = lines[i].strip() + f",{best_indiv.fitness}\n"
                f.seek(0)
                for line in lines:
                    f.write(line)

                    

if __name__ == '__main__':
    print('hello')