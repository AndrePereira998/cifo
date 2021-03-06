from random import sample, uniform
from operator import attrgetter



def tournament(Population , size = 5 ):    # size is the number of comparisons desired
    """ function implementing tournament selection by selecting a random set
     of individuals from the population and determining the best fitness 

     https://digitalcommons.olivet.edu/cgi/viewcontent.cgi?article=1004&context=csis_stsc"""

    subset_ind = sample(Population.individuals,size)    # random sample of individuals from the population with size equal to 'size'

    # different process for maximization and minization problem
    if Population.optim == 'max':
        return max(subset_ind, key=attrgetter("fitness"))
    elif Population.optim == 'min':
        return min(subset_ind, key=attrgetter("fitness"))
    else:
        raise Exception("Optimization needs to be specified.")



def roulette_wheel(Population):
    """ Roulette Wheel Selection function
     https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm """

    if Population.optim == 'max': # maximization only type of selection 
        
        # calculating the total fitness of the population
        total_fit = 0
        for i in Population:
            total_fit += i.fitness

        # generate number between 0 and total_fit
        fixed_point = uniform(0,total_fit)

        # starting point in the search for the chosen individual with fixed_point
        start = 0
        for individual in Population:
            start += individual.fitness
            if start > fixed_point:
                return individual   # as soon as the start point passes the fixed_point we found the chosen individual
    
    elif Population.optim != 'max':
        raise Exception('Optimization is no maximization.')



def rank(Population):
    """https://www.obitko.com/tutorials/genetic-algorithms/selection.php """
    
    # sorting individuals depending on the otimization 
    if Population.optim == 'max':
        Population.individuals.sort(key=attrgetter('fitness'))
    elif Population.optim == 'min':
        Population.individuals.sort(key=attrgetter('fitness'), reverse = True)

    # sum of the rank of every individual
    sum_rank = sum(range(Population.size + 1))  # + 1 since the last number is not included in the range

    # generating a random number that will decide the individual we choose
    selector = uniform(0, sum_rank)

    # searching for the individual 
    start = 0
    i = 0
    for individual in Population:
        i += 1 
        start += i
        if start > selector:   # once we pass the number generated we end the cycle and return the individual chosen
            return individual

    


