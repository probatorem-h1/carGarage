import random

class Car (object):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def __str__(self):
        return 'I am a {} {} made in {}.'.format(self.make,self.model,self.year)

    def __repr__(self):
        return "Car('{}','{}','{}')".format(self.make,self.model,self.year)
    
        
class Garage(object):
    'an object that contains cars'

    def __init__(self):
        self.carLst=[]

    def __contains__(self,car):
        'Returns True if the garage contains and car that matches the make, model and year.'
        result = False
        car = '{}, {}, {}'.format(car.getMake(),car.getModel(),car.getYear())
        for i in self.carLst:
            i = '{}, {}, {}'.format(i.getMake(),i.getModel(),i.getYear())
            if car == i:
                result = True
        return result

    def getCarsBasedOnMake(self,make):
        'get a list of all the instances of the car object that match the make'
        self.makeLst=[]
        for c in self.carLst:
            if make in c.getMake():
                self.makeLst.append(c)
        return self.makeLst


    def getRandomCar(self):
        'returns a ranom car from the garage or None if the garage is empty'
        i=random.randrange(0,len(self.carLst))
        return self.carLst[i]

    def add(self,car):
        'add a car to the garage'
        self.carLst.append(car)

    def __len__(self):
        return len(self.carLst)

    def __str__(self):
        return 'There are {} cars in the garage'.format(len(g))
    def __iter__(self):
        return iter(self.carLst)
