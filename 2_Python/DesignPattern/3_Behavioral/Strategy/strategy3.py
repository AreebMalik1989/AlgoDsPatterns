from types import MethodType


class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None) or 'Animal'
        if kwargs.get('walk', None):
            self.walk = MethodType(kwargs.pop('walk'), self)

    def walk(self):
        """
        Cause animal instance to walk.
        Walking functionality is strategy, and is intended to be implemented separately by different types of animals.
        """
        message = f"{self.__class__.__name__} should implement a walk method."
        raise NotImplementedError(message)


def snake_walk(self):
    print(f'I am slithering side to side because I am a {self.name}')


def four_legged_animal_walk(self):
    print(f'I am using all four of my legs to walk because I am a(n) {self.name}')


def two_legged_animal_walk(self):
    print(f'I am standing up on my two legs to walk because I am a {self.name}')


if __name__ == "__main__":

    generic_animal = Animal()
    king_cobra = Animal(name='King Cobra', walk=snake_walk)
    elephant = Animal(name='Elephant', walk=four_legged_animal_walk)
    kangaroo = Animal(name='Kangaroo', walk=two_legged_animal_walk)

    king_cobra.walk()
    elephant.walk()
    kangaroo.walk()

    # This one will raise a NonImplementedError to let the programmer know that the walk method is intended to be used
    # as a strategy
    generic_animal.walk()
