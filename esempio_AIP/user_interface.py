
import tkinter as tk

def menuSynptoms(frame):
    mb =  tk.Menubutton (frame, text="Secelct symptoms", font=16, relief=tk.RIDGE, pady=10, padx=10, activebackground="light grey")
    mb.pack(padx=10, pady=10)
    mb.menu =  tk.Menu (mb)
    mb["menu"] =  mb.menu
    file_symptoms = open("D:\\utente\\Documents\\IConProgetto\\esempio_AIP\\menu_sintomi.txt")
    simptoms = file_symptoms.readlines()
    for i in simptoms:
        mb.menu.add_checkbutton(label = i)
    file_symptoms.close()
    return mb


def user_window():
    window = tk.Tk()
    window.geometry("400x400")
    window.resizable(0,0)
    window.title("Human disease diagnosis")

    frame = tk.Frame(window)
    frame.pack()

    mb = menuSynptoms(frame)
    buttomGo = tk.Button(frame, text = "Submit", font=14, activebackground="light grey", relief=tk.RIDGE)
    buttomGo.pack(padx=10, pady=10)
    
    return window


if __name__ == "__main__":

    window = user_window()
    window.mainloop()