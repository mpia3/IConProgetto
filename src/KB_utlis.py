# -*- coding: utf-8 -*-
"""
In this file there are functions useful to handle a KB object 
"""


from logicProblem import KB, Clause
from logicBottomUp import fixed_point
from prob_utils import ProbItem
import os 

def get_disease(kb= KB()):
    """
    Returns all diseases true in the KB fixed point, starting from the synthoms true
    """
    fp = fixed_point(kb)#taking the fixed point of the knowlwdge base
    #watch out because fp is a set of strings
    
    atoms = {c.head for c in kb.clauses if c.isAtom()}#it is sure that none of atoms is a disease
    #atoms = set(atoms)
    
    
    return list(fp.difference(atoms))
    
    


def get_prob_model(kb = KB()):
    """
    La funzione ritorna una lista di oggetti ProbItem che indicano un modello probabilistico che riporta la probabilità
    che il paziente abbia la malattia considerata.
    Ovviamente se non ci sono malattie non ha senso andare ad eseguire tutti i passi.
    Per cui, per ragioni di complessità, si considerano uscite anticipate.
    """
    disease = get_disease(kb)#prendo le malattie vere dalla base di conoscenza
    if len(disease)==0: return [] #non si avvera alcuna malattia
    model = []#istanzio la variabile modello che avrà il ranking delle probabilità associate ad ogni malattia
    for d in disease:
        #appendo un oggetto di tipo ProbItem 
        model.append(ProbItem(d,get_prob(d,kb)))
        
    sumProb = sum(item.prob for item in model )#calcolo la somma delle probabilità (serve per avere poi la somma pari a uno)
    for item in model :
        item.prob = item.prob/sumProb#vado a sostituire la probabilità aggiustata
    model.sort(reverse = True)  #ordino
    return model#restituisco
    
    
        
def get_prob(disease, kb=KB()):
    """
    Restituisce la probabilità che quella malattia sia "vera" 
    Pre-condizione-> la malattia deve avere una clausola associata , con un body diverso da []    
    """
    allSym = len({c.head for c in kb.clauses if c.isAtom()})#prendo il numero dei sintomi che sono veri
    for c in kb.clauses:#cerco la mia malattia
        if c.head == disease:
            return len(c.body)/allSym#restituisco il numero di sintomi che ha su tutti quelli veri    
        
   
    
    
def how(KB,item):
    for c in KB.clauses:
        if c.head == item:
            return c
    return None


    
def real_filename(filename= ""):
    return os.path.realpath(filename)
    
    
    