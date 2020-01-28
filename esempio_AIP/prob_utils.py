# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:59:21 2020

@author: Utente
"""

class ProbItem:
    def __init__(self,name,prob):
        self.name = name
        self.prob = prob
        
    def __str__(self):
        return self.name + " -> " + str(self.prob)
    
    
    def __repr__(self):
        return str(self)
    
    def __lt__(self,item):
        return self.prob<item.prob
    