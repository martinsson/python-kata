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
        while number % potentialPrime == 0 and number >= potentialPrime:
            result.append(potentialPrime)
            number = number / potentialPrime
        
        return number

    def factorsOf(self, number):
        result = []
            
        smallestPrime = 2
        potentialPrime = smallestPrime
        number = self.addOccurencesOfPotentialPrime(number, result, potentialPrime)
        
        potentialPrime += 1
        number = self.addOccurencesOfPotentialPrime(number, result, potentialPrime)
        
        potentialPrime += 1
        number = self.addOccurencesOfPotentialPrime(number, result, potentialPrime)
                
        potentialPrime += 1
        number = self.addOccurencesOfPotentialPrime(number, result, potentialPrime)
                
        if (number > smallestPrime):
            prime = number
            result.append(prime)
        return result
    
    
        
