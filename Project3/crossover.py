from charles import Individual
from random import randint, uniform, sample



def single_point_crossover(parent1,parent2):   # imput são duas listas só de soluçoes  
    """ function implementing single point crossover, creating two offspring from the two parent inputs"""

    co_point = randint(1, len(parent1)-2) 

    # spliting lists at the crossover point and merging the resulting lists
    children1 = parent1[:co_point] + parent2[co_point:]
    children2 = parent2[:co_point] + parent1[co_point:]

    return Individual( representation = children1, indiv_array = parent1.indiv_array ), Individual( representation = children1, indiv_array = parent1.indiv_array )



def multi_point_crossover(parent1,parent2):    # imput são duas listas só de soluçoes 
    """ function implementing multi point crossover, creating two offspring from the two parent inputs
        https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0 """
    
    # randomly choosing the 2 indexes of the list
    co_points = sample(range(len(parent1)), 2)   #### SAI SEMPRE EM ORDEM ASCENDENTE???  

    # alternating segments are swapped to get new off-springs.
    children1 = parent1[:co_points[0]] + parent2[co_points[0]:co_points[1]] + parent1[co_points[1]:]
    children2 = parent2[:co_points[0]] + parent1[co_points[0]:co_points[1]] + parent2[co_points[1]:]

    return Individual( representation = children1, indiv_array = parent1.indiv_array ), Individual( representation = children1, indiv_array = parent1.indiv_array )



def uniform_crossover(parent1,parent2):
    """  function performing uniform crossover where information between parents is exchanged at the indexes where probability is less than the threshold (0.5)
        https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_crossover.htm 
        https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0"""

    # creating a list of probabilities of the swap occuring
    prob_list = sample(range(0, 1), len(parent1))

    children1 = parent1.copy()
    children2 = parent2.copy()

    for i in range(prob_list):
        # when the probability is less than 0.5 the swap happens
        if prob_list[i] < 0.5:   
            temp = children1[i]
            children1[i] = children2[i]
            children2[i] = temp
    
    return Individual( representation = children1, indiv_array = parent1.indiv_array ), Individual( representation = children1, indiv_array = parent1.indiv_array )


