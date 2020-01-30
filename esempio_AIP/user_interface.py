
import tkinter as tk
import ontology_manager as om

def menuSynptoms(frame,symptoms):
    mb =  tk.Menubutton (frame, text="Secelct symptoms", font=16, relief=tk.RIDGE, pady=10, padx=10, activebackground="light grey")
    mb.pack(padx=10, pady=10)
    mb.menu =  tk.Menu (mb)
    mb["menu"] =  mb.menu
    #file_symptoms = open("D:\\utente\\Documents\\IConProgetto\\esempio_AIP\\menu_sintomi.txt")
    for i in symptoms:
        mb.menu.add_checkbutton(label = i)
    
    return mb


def user_window(symptoms):
    window = tk.Tk()
    window.geometry("400x400")
    window.resizable(0,0)
    window.title("Human disease diagnosis")

    frame = tk.Frame(window)
    frame.pack()

    mb = menuSynptoms(frame,symptoms)
    buttomGo = tk.Button(frame, text = "Submit", font=14, activebackground="light grey", relief=tk.RIDGE)
    buttomGo.pack(padx=10, pady=10)
    
    return window


if __name__ == "__main__":
    idoid = om.owl.get_ontology("D:\\utente\\Documents\\IConProgetto\\esempio_AIP\\inferred_doid")
    idoid.load()
    map_disease_symptom = om.build_map(idoid) #dizionario malattie,sintomi
    symptoms = om.list_symptoms(map_disease_symptom)
    _KB = om.create_KB(map_disease_symptom) #KB con clausole malattia(tetsa) e sintomi(corpo)
    window = user_window(symptoms)
    window.mainloop()