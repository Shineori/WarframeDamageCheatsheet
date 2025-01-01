import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)  # Disable window resizing

firstPanedWindow = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
firstPanedWindow.pack(fill=tk.BOTH, expand=True)

frame1 = ttk.Frame(firstPanedWindow)
frame2 = ttk.Frame(firstPanedWindow, relief=tk.SUNKEN)

firstPanedWindow.add(frame1, weight=2)
firstPanedWindow.add(frame2, weight=1)

text_widget1 = tk.Text(frame1, wrap=tk.WORD, height=5, width=50, padx=7, bd=2, relief=tk.SUNKEN)
text_widget1.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

text_widget2 = tk.Text(frame2, wrap=tk.WORD, height=5, width=50, padx=7, bd=2, relief=tk.SUNKEN)
text_widget2.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

def format_text(text):
    text_widget1.config(state=tk.NORMAL)
    text_widget1.delete(1.0, tk.END)
    parts = text.split('\n')
    for part in parts:
        if "+50% Damage" in part:
            text_widget1.insert(tk.END, part, 'green_bold')
        elif "-50% Damage" in part:
            text_widget1.insert(tk.END, part, 'red_bold')
        else:
            text_widget1.insert(tk.END, part)
        text_widget1.insert(tk.END, '\n')
    text_widget1.config(state=tk.DISABLED)

def format_text2(text):
    text_widget2.config(state=tk.NORMAL)
    text_widget2.delete(1.0, tk.END)
    parts = text.split('\n')
    for part in parts:
        if "+50% Damage" in part:
            text_widget2.insert(tk.END, part, 'green_bold')
        elif "Effect" in part:
            text_widget2.insert(tk.END, part, 'red_bold')
        else:
            text_widget2.insert(tk.END, part)
        text_widget2.insert(tk.END, '\n')
    text_widget2.config(state=tk.DISABLED)

text_widget1.tag_configure('green_bold', foreground='green', font=('Helvetica', 8, 'bold'))
text_widget1.tag_configure('red_bold', foreground='red', font=('Helvetica', 8, 'bold'))

text_widget2.tag_configure('green_bold', foreground='green', font=('Helvetica', 8, 'bold'))
text_widget2.tag_configure('red_bold', foreground='red', font=('Helvetica', 8, 'bold'))

##__Creating the buttons__##
def grineer():
    format_text("+50% Damage:\nImpact and Corrosive")

def kuvagrineer():
    format_text("+50% Damage:\nImpact and Corrosive\n-50% Damage: \nHeat")

def corpus():
    format_text("+50% Damage:\nPuncture and Magnetic")

def infested():
    format_text("+50% Damage:\nSlash and Heat")

def deimosinfested():
    format_text("+50% Damage:\nBlast and Gas\n-50% Damage:\nViral")

def corrupted():
    format_text("+50% Damage:\nPuncture and Viral\n-50% Damage:\nRadiation")

def sentient():
    format_text("+50% Damage:\nSlash and Toxin\n-50% Damage:\nImpact")

def narmer():
    format_text("+50% Damage:\nSlash and Magnetic\n-50% Damage:\nImpact")

def murmur():
    format_text("+50% Damage:\nSlash and Corrosive\n-50% Damage:\nImpact")

def zariman():
    format_text("+50% Damage:\nSlash and Viral\n-50% Damage:\nImpact")

def scaldra():
    format_text("+50% Damage:\nSlash and Radiation\n-50% Damage:\nImpact")

def techrot():
    format_text("+50% Damage:\nSlash and Gas\n-50% Damage:\nImpact")

# Aligning buttons in a 3-row setup using grid with reduced padding
grineer_button = ttk.Button(frame1, text="Grineer", command=grineer)
grineer_button.grid(row=1, column=0, padx=1, pady=1, sticky="nw")

kuvagrineer_button = ttk.Button(frame1, text="Kuva Grineer", command=kuvagrineer)
kuvagrineer_button.grid(row=1, column=1, padx=1, pady=1, sticky="nw")

corpus_button = ttk.Button(frame1, text="Corpus", command=corpus)
corpus_button.grid(row=1, column=2, padx=1, pady=1, sticky="nw")

infested_button = ttk.Button(frame1, text="Infested", command=infested)
infested_button.grid(row=2, column=0, padx=1, pady=1, sticky="nw")

deimosinfested_button = ttk.Button(frame1, text="Deimos Infested", command=deimosinfested)
deimosinfested_button.grid(row=2, column=1, padx=1, pady=1, sticky="nw")

corrupted_button = ttk.Button(frame1, text="Corrupted", command=corrupted)
corrupted_button.grid(row=2, column=2, padx=1, pady=1, sticky="nw")

sentient_button = ttk.Button(frame1, text="Sentient", command=sentient)
sentient_button.grid(row=3, column=0, padx=1, pady=1, sticky="nw")

narmer_button = ttk.Button(frame1, text="Narmer", command=narmer)
narmer_button.grid(row=3, column=1, padx=1, pady=1, sticky="nw")

murmur_button = ttk.Button(frame1, text="Murmur", command=murmur)
murmur_button.grid(row=3, column=2, padx=1, pady=1, sticky="nw")

zariman_button = ttk.Button(frame1, text="Zariman", command=zariman)
zariman_button.grid(row=4, column=0, padx=1, pady=1, sticky="nw")

scaldra_button = ttk.Button(frame1, text="Scaldra", command=scaldra)
scaldra_button.grid(row=4, column=1, padx=1, pady=1, sticky="nw")

techrot_button = ttk.Button(frame1, text="Techrot", command=techrot)
techrot_button.grid(row=4, column=2, padx=1, pady=1, sticky="nw")

# Adding buttons to frame2
def impact():
    format_text2("+50% Damage:\nGrineer, Kuva Grineer, Scaldra\nEffect:\nStaggers and chance to Mercy")

def puncture():
    format_text2("+50% Damage:\nCorpus, Corrupted\nEffect:\n-80% Damage Output, Increased Crit Chance (25%)")

def slash():
    format_text2("+50% Damage:\nInfested and Narmer\nEffect:\nBleed DoT(6s) up to 10")

impact_button = ttk.Button(frame2, text="Impact", command=impact)
impact_button.grid(row=1, column=0, padx=1, pady=1, sticky="nw")

puncture_button = ttk.Button(frame2, text="Puncture", command=puncture)
puncture_button.grid(row=1, column=1, padx=1, pady=1, sticky="nw")

slash_button = ttk.Button(frame2, text="Slash", command=slash)
slash_button.grid(row=1, column=2, padx=1, pady=1, sticky="nw")

root.mainloop()