# -*- coding: utf-8 -*-

import owlready2 as owl
import logicProblem as lp


    
    
"DEFINIZIONE MACRO"
REAL_CLASS_LABEL = 0    #è come se fosse un define in C-> so che il nome vero di una classe (la label) è la prima nella lista
                        #per non starmi a ricordare lo 0 me lo segno come macro

    
    
    
def get_class(ontology,class_name):
    """
        L'ontologia deve essere già caricata e deve esser già stato avviato il reasoner
        La funzione restituisce una lista di sottoclassi della classe che ha come label -class_name-
    """
    
    for c in ontology.classes():
        if class_name in c.label:#se ho trovato la classe target allora cerco tutte le sottoclassi e le restituisco
            res= ontology.search(is_a=c)
            return res


def build_map(ontology):
    """
        L'ontologia deve essere già caricata e deve esser già stato avviato il reasoner
        La funzione restituisce un dizionario <string,list<string>> dove la chiave è il nome della malattia 
            e il valore è la lista dei nomi dei sintomi che causano la malattia
    """
    _map = {} #è il dizionario che conterrà come chiave il nome della malattia e come valore la lista di sintomi che la causa
    dis = get_class(ontology,"disease") #prendo tutte le malattie
    for d in dis:#per ogni malattia
        sym = d.has_symptom #prendo tutti i sintomi coinvolti in tale malattia
        sintomi = []
        for j in sym:
            sintomi.append(j.label[0]) #inserisco le label per i sintomi
        if sym: _map[d.label[REAL_CLASS_LABEL]] = sintomi
        #if sym: _map[dis.label[REAL_CLASS_LABEL]] = [s.label[REAL_CLASS_LABEL] for s in sym]
        #se ci sono sintomi cha causano la malattia:
            #imposto come chiave il nome reale della malattia e come valore la lista dei nomi reali dei sintomi coinvolti nella 
            #malattia
    return _map


def create_KB(map_disease_symptom):
    statements = [] #accoglierà tutte le clausole
    for k in map_disease_symptom.keys(): #intero su tutte le malattie
        defined_clause = lp.Clause(k,map_disease_symptom.get(k)) 
        #costruisce una clausola definita con k(malattia) come testa e sintomi come corpo
        statements.append(defined_clause)
    _KB = lp.KB(statements) #oggetto con tutte le clausole 
    return _KB
        
def list_symptoms(map_disease_symptoms):
    symptoms = []
    for k in map_disease_symptoms.keys():
        symptom = map_disease_symptoms.get(k)
        for i in symptom:
            symptoms.append(i)
    symptoms = list(set(symptoms))
    symptoms.sort()
    return symptoms
    
  
#----------------------------------------------------TEST-------------------------------
"""
if __name__== "__main__":
    
    idoid = owl.get_ontology("D:\\utente\\Documents\\IConProgetto\\esempio_AIP\\inferred_doid")
    idoid.load()
    map_disease_symptom = build_map(idoid) #dizionario malattie,sintomi
    _KB = create_KB(map_disease_symptom) #KB con clausole malattia(tetsa) e sintomi(corpo)
"""    
"""
    for dis in get_class(idoid,"disease"):
        sym = dis.has_symptom
        if sym : print(dis.label,"has symptom ",[s.label for s in sym])
"""      
        
