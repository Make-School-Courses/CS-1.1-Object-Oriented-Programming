import random
import pytest
# TODO: Import the virus class


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = None
        self.is_alive = True # Boolean
        self.is_vaccinated = None # Boolean
        self.infection = None # Virus or None

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean
        pass


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)

    assert person._id == 1
    assert person.is_alive == True
    assert person.is_vaccinated == True
    assert person.infection == False


def test_not_vacc_person_instantiation():
    person = Person(1, False)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    pass


def test_sick_person_instantiation():
    # import the virus class for the testing
    from virus import Virus
    virus = Virus("Dysentery", 0.7, 0.2)

    # TODO: complete your own assert statements that test
    # the values at each attribute
    person = Person(1, False, virus)
    pass
