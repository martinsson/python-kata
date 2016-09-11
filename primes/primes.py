'''
Created on Aug 31, 2016

@author: johan
'''

class Primes(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        
        '''
    


    def addOccurencesOfPotentialPrime(self, number, result, potentialPrime):
        while number % potentialPrime == 0 and number > potentialPrime:
            result.append(potentialPrime)
            number = number / potentialPrime
        
        return number

    def factorsOf(self, number):
        result = []
        if (number < 2):
            return result
            
        potentialPrime = 2
        number = self.addOccurencesOfPotentialPrime(number, result, potentialPrime)
        
        potentialPrime = 3
        number = self.addOccurencesOfPotentialPrime(number, result, potentialPrime)
        
        potentialPrime = 5
        number = self.addOccurencesOfPotentialPrime(number, result, potentialPrime)
                
        result.append(number)
        return result
    
    
        