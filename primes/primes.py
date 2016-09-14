'''
Created on Aug 31, 2016

@author: johan
'''

class Primes(object):
    smallestPrime = 2
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        
        '''
    



    def isDivisibleBy(self, number, potentialPrime):
        return number % potentialPrime == 0

    def addOccurencesOfPotentialPrime(self, number, result, potentialPrime):
        while self.isDivisibleBy(number, potentialPrime) and number >= self.smallestPrime:
            result.append(potentialPrime)
            number = number / potentialPrime
        
        return number

    def factorsOf(self, number):
        result = []
            
        for potentialPrime in range(self.smallestPrime, number+1):
            number = self.addOccurencesOfPotentialPrime(number, result, potentialPrime)
                
        if (number > self.smallestPrime):
            prime = number
            result.append(prime)
            
        return result
    
    
        
