
import tkinter as tk
import ontology_manager as om
import KB_utlis as utils




def selectSymptom(varCheck,interface):
    stringS = varCheck.get()
    if stringS in interface.selected_sym:
        interface.selected_sym.remove(stringS)
    else:
        interface.selected_sym.add(stringS)
    interface.consoleArea.delete("1.0", tk.END)
    for item in interface.selected_sym:
        interface.consoleArea.insert(tk.INSERT, item+"-")

def cancel_console(interface):
    interface.consoleArea.delete("1.0", tk.END)
    interface.selected_sym.clear()
    interface.kb=om.create_KB(interface.map_disease_symptom)

def send_symptom(interface):
    _input = interface.consoleArea.get("1.0", "end-2c")#legge da linea uno, carattere zero, -2c cancella 2 caratteri(- e newline)
    _input = _input.split("-")
    #da qui aggiungere le funzioni per l'elaborazione della malattia
    assumable = [om.lp.Clause(head = item) for item in _input]
    interface.kb.clauses+=assumable 
    model = utils.get_prob_model(interface.kb)
    if model:
        interface.consoleArea.insert(tk.INSERT,"\n-------------RESULT---------\n")
        interface.consoleArea.insert(tk.INSERT,"\ndisease \t\t\t %\n")
        for disease in model:
            interface.consoleArea.insert(tk.INSERT,str(disease.name)+"\t\t\t"+str("{0:.2f}".format(disease.prob*100))+"%"+"\n")
    else:
        from tkinter import messagebox
        messagebox.showinfo(title="Info",message="Cannot find any disease")
    
 
def submitHow(entry,KB):
    res = utils.how(KB,entry)
    from tkinter import messagebox
    if res:
        if not res.body:
            messagebox.showinfo(title = "How result", message = res.head+" is a symptom that you gave me, so it is true by default")
        else:
            messagebox.showinfo(title = "How result", message = "Clause used to proof "+entry+"is : "+str(res))
    else:
        messagebox.showerror(title = "Error",message = "Cannot find anything in the system which proof "+entry)
    
    
class StartInterface():
    def __init__(self,onto_filename):
        self.onto = om.owl.get_ontology(utils.real_filename(onto_filename))
        self.onto.load()
        #om.owl.sync_reasoner()
        self.selected_sym = set()
        self.map_disease_symptom = om.build_map(self.onto)
        self.symptoms = om.list_symptoms(self.map_disease_symptom)
        self.kb = om.create_KB(self.map_disease_symptom)
        
        
        #------------------GRAPHIC----------------------
        self.window= tk.Tk()
        self.window.geometry("400x400")
        self.window.resizable(0,0)
        self.window.title("Human disease diagnosis")
        
        #---------------------Upper---------------------
        self.frameUpper = tk.Frame(self.window)
        self.frameUpper.pack()
        self.mb = tk.Menubutton(self.frameUpper, text= "Select symptoms",font = 12, relief = tk.RIDGE,pady=10,padx=10,activebackground = "light grey")
        self.mb.pack(padx=10, pady=10)
        self.mb.menu =  tk.Menu (self.mb)
        self.mb["menu"]=self.mb.menu
        varCheck = tk.StringVar()
        for i in self.symptoms:
            self.mb.menu.add_checkbutton(label=i, onvalue=i, offvalue = i, command=lambda:selectSymptom(varCheck,self), variable=varCheck)
        
        #-------------------------Middle---------------------------
        self.frameMiddle = tk.Frame(self.window)
        self.frameMiddle.pack()
        
        self.buttomSubmit = tk.Button(self.frameMiddle, text = "Submit", font=11, activebackground="light grey", relief=tk.RIDGE, command=lambda:send_symptom(self))
        self.buttomSubmit.pack(side=tk.LEFT, padx=10)
        self.buttomCancel = tk.Button(self.frameMiddle, text = "Cancel", font=11, activebackground="light grey", relief=tk.RIDGE, command=lambda:cancel_console(self))
        self.buttomCancel.pack(side=tk.LEFT, padx=10)
        
        
        #---------HowFrame--------------------------
        self.frameHow = tk.Frame(self.window)
        self.frameHow.pack()
        
        self.howlabel = tk.Label(self.frameHow,text = "How")
        self.howlabel.pack(side = tk.LEFT, padx = 10)
        self.howQuery = tk.Entry(self.frameHow)
        self.howQuery.pack()
        self.howSubmitButton = tk.Button(self.frameHow, text = "Submit",font = 11,activebackground ="light grey", relief = tk.RIDGE,command = lambda: submitHow(self.howQuery.get(),self.kb))
        self.howSubmitButton.pack(side = tk.LEFT,padx = 10)
        #---------------------------------------- Bottom ----------------------------------------------
        self.frameBottom = tk.Frame(self.window)
        self.frameBottom.pack()
        
        self.labelConsole = tk.Label(self.frameBottom, text="Console area:")
        self.labelConsole.pack(anchor=tk.W)
        self.consoleArea = tk.Text(self.frameBottom, fg="black", wrap=tk.WORD)
        self.consoleArea.pack()
        
        


        
        
        self.window.mainloop()


i = StartInterface("inferred_doid")


