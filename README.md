# IConProgetto
Disease diagnosis project


Progettazione:

1) Acquisizione delle malattie dall'ontologia DOID.

2) Per ogni malattia acquisita trovare le sue cause dal Linked Open Data (LOD) Wikidata.

3) Costruire un Dizionario di malattie-cause (Key = malattia, Values = cause), il values potrebbe essere una lista di cause.

4) Costruzione dell Knowledge Base (KB) attraverso proposizioni logiche della forma: m <-- s1 ^ s2 ^ ... ^ sn
   con m = malattia, si = sintomo.

5) Acquisizione dei sintomi da parte dell'utente con successiva formulazione di una query (es. ask s1 ^ s2 ^ ... ^ sn).

6) Si tenta di derivare la query come conseguenza logica della KB per risalire alla malattia associata.


Si consiglia di visionare questo file dopo il ricevimento (dopo le ore 14.00 del 21/01/2020)
