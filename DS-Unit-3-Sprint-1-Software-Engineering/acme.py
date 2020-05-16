from random import randint


class Product(object):
    '''
    Represents Acme Corp. products
    '''

    def __init__(self, name: str=None, price: int=10,
                 weight: int=20, flammability: float=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        # random.randint(): Return a random integer N such that a <= N <= b.
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        '''
        Calculates the stealability, and then returns a summary message.

        Parameters:
        None

        Returns:
        str: highly scientific stealability score
        '''
        stealability = (self.price / self.weight)
        if stealability < 0.5:
            return "Not so stealable..."
        elif stealability >= 0.5 and stealability < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        '''
        Tries to detonate the product based on flammability and weight.

        Parameters:
        None

        Returns:
        str
        '''
        explodability = (self.flammability * self.weight)
        if explodability < 10:
            return "...fizzle."
        elif explodability >= 10 and explodability < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    '''
    A subclass of Product that doesn't explode, and can punch!
    '''
    def __init__(self, name: str=None, price: int=10,
                 weight: int=10, flammability: float=0.5):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability)

    def explode(self):
        '''
        Always returns "...its a glove."

        Parameters:
        None

        Returns:
        str
        '''
        return "...its a glove."

    def punch(self):
        '''
        Make the Boxing Glove punch- be careful!

        Parameters:
        None

        Returns:
        str
        '''
        if self.weight < 0.5:
            return "That tickles."
        elif self.weight > 5.0 and self.weight < 15.0:
            return "Hey that hurt!"
        else:
            return "OUCH!"
