from charles import Individual
from random import randint, sample, shuffle



def swap_mutation(Individual):   # input é a lista so com as soluçoes 
    """ function implementing swap mutations on a single individual """

    # generating two random numbers that will serve as indexes of the mutation
    mu_points = sample(range(len(Individual)), 2)    #### SAI SEMPRE EM ORDEM ASCENDENTE???  

    Individual_copy = Individual.copy()

    # switching two elements of the array 
    Individual[mu_points[0]] = Individual_copy[mu_points[1]]
    Individual[mu_points[1]] = Individual_copy[mu_points[0]]

    return Individual



def inversion_mutation(Individual):
    """ function implementing inversion mutation by selecting a subset of the list and inverting it.
        https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_mutation.htm """

    # generating two random numbers that will serve as indexes of the mutation
    mu_points = sample(range(len(Individual)), 2)  #### SAI SEMPRE EM ORDEM ASCENDENTE???  

    sub_list = Individual[mu_points[0]:mu_points[1]]
    sub_list = sub_list[::-1]  # inverting list

    # merging the selected subset with the original list
    Individual = Individual[:mu_points[0]] + sub_list + Individual[mu_points[1]:]

    return Individual



def scramble_mutation(Individual):
    """ function performing scramble mutation by randomly shuffling a subset of the original list.
        For simplicity reasons we will always select a continous subset"""

    mu_points = sample(range(len(Individual)), 2)

    sub_list = Individual[mu_points[0]:mu_points[1]]
    # randomly shffling the list 
    sub_list = shuffle(sub_list)

    Individual = Individual[:mu_points[0]] + sub_list + Individual[mu_points[1]:]

    return Individual