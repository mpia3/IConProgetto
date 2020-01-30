
import tkinter as tk
import ontology_manager as om

def selectSymptom():
    stringS = varCheck.get()
    if stringS != "null":
        consoleArea.insert(tk.INSERT, stringS+"-")

def send_symptom():
    input = consoleArea.get("1.0", "end-2c")#legge da linea uno, carattere zero, -2c cancella 2 caratteri(- e newline)
    input = input.split("-")
    #da qui aggiungere le funzioni per l'elaborazione della malattia

idoid = om.owl.get_ontology("D:\\utente\\Documents\\IConProgetto\\esempio_AIP\\inferred_doid")
idoid.load()
map_disease_symptom = om.build_map(idoid) #dizionario malattie,sintomi
symptoms = om.list_symptoms(map_disease_symptom)
_KB = om.create_KB(map_disease_symptom) #KB con clausole malattia(tetsa) e sintomi(corpo)

window = tk.Tk()
window.geometry("400x400")
window.resizable(0,0)
window.title("Human disease diagnosis")

frame = tk.Frame(window)
frame.pack()

mb =  tk.Menubutton (frame, text="Select symptoms", font=12, relief=tk.RIDGE, pady=10, padx=10, activebackground="light grey")
mb.pack(padx=10, pady=10)
mb.menu =  tk.Menu (mb)
mb["menu"] =  mb.menu
varCheck = tk.StringVar()
for i in symptoms:
    mb.menu.add_checkbutton(label=i, onvalue=i, offvalue = "null", command=selectSymptom, variable=varCheck)

buttomSubmit = tk.Button(frame, text = "Submit", font=12, activebackground="light grey", relief=tk.RIDGE, command=send_symptom)
buttomSubmit.pack(padx=10, pady=10)

labelConsole = tk.Label(frame, text="Console area:")
labelConsole.pack(anchor=tk.W)
consoleArea = tk.Text(frame, wrap=tk.WORD)
consoleArea.pack()

window.mainloop()

"""
if __name__ == "__main__":
    
    window = user_window(symptoms)
    window.mainloop()
"""
