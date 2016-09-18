'''
Created on Aug 31, 2016

@author: johan
'''

class Primes():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        
        '''
        


    def forNumber(self, number):
        if (number < 2):
            return []
        
        factors = []         
        potentialPrime = 2
        while (potentialPrime <= number):
            number = self.appendFactorsOf(number, factors, potentialPrime)
            potentialPrime+=1
            
                        
        return factors

    def isDivisibleBy(self, number, potentialPrime):
        return number % potentialPrime == 0

    def appendFactorsOf(self, number, factors, potentialPrime):
        while self.isDivisibleBy(number, potentialPrime) and number > 1:
            factors.append(potentialPrime)
            number = number / potentialPrime
        
        return number