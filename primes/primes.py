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
        factors = [] 
        
        if ( number >= 2):
            while (number % 2 == 0 and number >= 2):
                factors.append(2)
                number = number / 2
                
        if ( number >= 3):
            while (number % 3 == 0 and number >= 3):
                factors.append(3)
                number = number / 3
        
        if (number > 2):
            factors.append(number)
            
        return factors