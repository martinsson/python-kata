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
        

    def appendFactorsOf(self, number, factors, potentialPrime):
        if (number >= potentialPrime):
            while number % potentialPrime == 0 and number >= potentialPrime:
                factors.append(potentialPrime)
                number = number / potentialPrime
        
        return number

    def forNumber(self, number):
        factors = [] 
        
        potentialPrime = 2
        number = self.appendFactorsOf(number, factors, potentialPrime)

        potentialPrime = 3
        while (potentialPrime <= number):
            number = self.appendFactorsOf(number, factors, potentialPrime)
            potentialPrime+=2
            
                        
        return factors