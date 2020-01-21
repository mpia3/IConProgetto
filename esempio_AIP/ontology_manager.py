# -*- coding: utf-8 -*-

import owlready2 as owl


#owl.onto_path.append("D:\\raffaele\\UNIVERSITA\\3_anno\\IC\\syn_and_dis")
#onto = owl.get_ontology("tm-signs-and-sympts.owl")
#
#onto.load()


    
    
    
owl.onto_path.append("D:\\raffaele\\UNIVERSITA\\3_anno\\IC\\esempio_AIP")
ext = owl.get_ontology("D:\\raffaele\\UNIVERSITA\\3_anno\\IC\\esempio_AIP\\ext.owl")

ext.load()
doid = owl.get_ontology("D:\\raffaele\\UNIVERSITA\\3_anno\\IC\\esempio_AIP\\doid.owl")
doid.load()


for p in doid.properties():
    print(p)


for c in doid.classes():
    sym = list(c.has_symptom)
    print(c.label ,"->",sym)
    if len(sym)!=0:
        print("*"*30)
        print(sym)
        print("*"*30)
        import os
        os.system("PAUSE")