from scipy import rand
from charles import Individual
from random import randint, uniform, sample



def single_point_crossover(parent1,parent2):  
    """ function implementing single point crossover, creating two offspring from the two parent inputs"""

    co_point = randint(1, len(parent1)-2) 
    
    # spliting lists at the crossover point and merging the resulting lists
    children1 = parent1[:co_point] + parent2[co_point:]
    children2 = parent2[:co_point] + parent1[co_point:]
    


    return children1, children2



def multi_point_crossover(parent1,parent2):    
    """ function implementing multi point crossover, creating two offspring from the two parent inputs
        https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0 """
    
    # randomly choosing the 2 indexes of the list
    co_points = sample(range(len(parent1)), 2)
    co_points.sort()   

    # alternating segments are swapped to get new off-springs.
    children1 = parent1[:co_points[0]] + parent2[co_points[0]:co_points[1]] + parent1[co_points[1]:]
    children2 = parent2[:co_points[0]] + parent1[co_points[0]:co_points[1]] + parent2[co_points[1]:]

    return children1, children2



def uniform_crossover(parent1,parent2):
    """  function performing uniform crossover where information between parents is exchanged at the indexes where probability is less than the threshold (0.5)
        https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_crossover.htm 
        https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0"""

    # creating a list of probabilities of the swap occuring
    prob_list = [uniform(0,1) for _ in range(len(parent1))]

    children1 = parent1
    children2 = parent2

    for i, value in enumerate(prob_list):

        # when the probability is less than 0.5 the swap happens
        if value < 0.5:   
            temp = children1[i]
            children1[i] = children2[i]
            children2[i] = temp
    
    return children1, children2


