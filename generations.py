'''not actually a cracking the coding interview question, but this seems relevant.
The relevant challenge is to take a group of people and calculate how long it takes before there is only one last name remaining
'''
import random

class Person:

    def __init__(self, lastname, generation):
        self.lastname = lastname
        self.gender = random.randint(0, 1)
        self.generation = generation
        self.paired = False


def create_pairings(people_list):
    '''returns a list of paired sets of people, male and female
    input = list of people (one generation)
    output = paired list of people
    '''
    #added shuffle to the list so that if the initial created list is ordered it doesn't mess up the stats
    random.shuffle(people_list)
    #creates an empty list to add to
    output_list = []
    for person1 in people_list:
        if person1.gender == 0 and person1.paired == False:
            for person2 in people_list:
                if person2.gender == 1 and person2.paired == False:
                    output_list.append([person1, person2])
                    person1.paired = True
                    person2.paired = True
    return output_list

    #notes: consider adding a tracker for when the last person of gender 1 was used. It will allow you to run at less than n squared
    #though it will add a bit of complexity up front.

def next_generation(paired_list):
    '''takes a list of paired lists and creates a number of children (between 0 and 3) each 
    containing the last name of the first individual in the pair and with a randomly assigned gender
    inputs: list of lists
    outputs: list of person objects'''
    output = []
    for pair in paired_list:
        for i in range(random.randint(0, 3)):
            output.append(Person(pair[0].lastname, pair[0].generation + 1))
    return output
