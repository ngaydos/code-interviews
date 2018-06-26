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
    output_list = []
    for person1 in people_list:
        if person1.gender == 0 and person1.paired == False:
            for person2 in people_list:
                if person2.gender == 1 and person2.paired == False:
                    output_list.append({person1, person2})
                    person1.paired = True
                    person2.paired = True
    return output_list
    