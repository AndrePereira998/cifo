from charles import Population
from selection import tournament, roulette_wheel, rank
from mutation import swap_mutation, inversion_mutation, scramble_mutation
from crossover import single_point_crossover, multi_point_crossover, uniform_crossover
import numpy as np
from main import load_sudoku


#selection_methods = {'tournament':tournament, 'roulette':roulette_wheel, 'rank':rank}
selection_methods = {'tournament':tournament, 'rank':rank}
mutation_methods = {'swap':swap_mutation, 'inversion':inversion_mutation, 'scramble':scramble_mutation}
crossover_methods = {'single_point':single_point_crossover, 'multi_point':multi_point_crossover, 'uniform':uniform_crossover}


for sel in selection_methods:
    for mut in mutation_methods:
        for cross in crossover_methods:
            if __name__ == '__main__':
                problem = load_sudoku("problem_easy.txt")
                arr = np.array(problem)

                # running each combination of methods several times in order to calculate an average
                for _ in range(1): 
                    pop = Population(
                        size=10,
                        full_array = arr,
                        replacement=True,
                        filename = sel + '_'+ mut+'_'+cross,  
                        folder=r"attempt_",
                        optim="max"
                    )

                    pop.evolve(gens=500,
                            select= selection_methods[sel],
                            crossover=crossover_methods[cross],
                            mutate=mutation_methods[mut],
                            co_p=0.9, mu_p=0.9,
                            elitism=True,
                            conv_param=[200,100,50],
                            full_array_evolve=arr,
                            log = True)