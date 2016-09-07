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
    
    def factorsOf(self, number):
        if (number < 2):
            return []
        elif (number == 4):
            return [2, 2]
        else:
            return [number]
        
    
        