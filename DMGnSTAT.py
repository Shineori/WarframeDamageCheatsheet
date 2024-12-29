import tkinter as tk
from tkinter import ttk

root = tk.Tk()
firstPanedWindow = ttk.PanedWindow(root, orient=tk.HORIZONTAL, height=405, width=300)
firstPanedWindow.pack(fill=tk.BOTH, expand=True)

frame1 = ttk.Frame(firstPanedWindow, border=5, relief=tk.SUNKEN)
frame2 = ttk.Frame(firstPanedWindow, relief=tk.SUNKEN)

firstPanedWindow.add(frame1, weight=1)
firstPanedWindow.add(frame2, weight=1)

text_widget1 = tk.Text(frame1, wrap=tk.WORD, height=5, width=50, padx=2, bd=6, relief=tk.SUNKEN)
text_widget1.pack(fill=tk.BOTH)

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

text_widget1.tag_configure('green_bold', foreground='green', font=('Helvetica', 8, 'bold'))
text_widget1.tag_configure('red_bold', foreground='red', font=('Helvetica', 8, 'bold'))

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

# Aligning buttons to the left in frame1
grineer_button = ttk.Button(frame1, text="Grineer", command=grineer)
grineer_button.pack(anchor='n', padx='5')

kuvagrineer_button = ttk.Button(frame1, text="Kuva Grineer", command=kuvagrineer)
kuvagrineer_button.pack(anchor='n', padx='5')

corpus_button = ttk.Button(frame1, text="Corpus", command=corpus)
corpus_button.pack(anchor='n', padx='5')

infested_button = ttk.Button(frame1, text="Infested", command=infested)
infested_button.pack(anchor='n', padx='5')

deimosinfested_button = ttk.Button(frame1, text="Deimos Infested", command=deimosinfested)
deimosinfested_button.pack(anchor='n', padx='5')

corrupted_button = ttk.Button(frame1, text="Corrupted", command=corrupted)
corrupted_button.pack(anchor='n', padx='5')

sentient_button = ttk.Button(frame1, text="Sentient", command=sentient)
sentient_button.pack(anchor='n', padx='5')

narmer_button = ttk.Button(frame1, text="Narmer", command=narmer)
narmer_button.pack(anchor='n', padx='5')

murmur_button = ttk.Button(frame1, text="Murmur", command=murmur)
murmur_button.pack(anchor='n', padx='5')

zariman_button = ttk.Button(frame1, text="Zariman", command=zariman)
zariman_button.pack(anchor='n', padx='5')

scaldra_button = ttk.Button(frame1, text="Scaldra", command=scaldra)
scaldra_button.pack(anchor='n', padx='5')

techrot_button = ttk.Button(frame1, text="Techrot", command=techrot)
techrot_button.pack(anchor='n', padx='5')



# Adding a text box to frame2
text_widget2 = tk.Text(frame2, wrap=tk.WORD, height=5, width=50, padx=2, bd=6, relief=tk.SUNKEN)
text_widget2.pack(fill=tk.BOTH)

# Adding buttons to frame2
def example1():
    text_widget2.config(state=tk.NORMAL)
    text_widget2.delete(1.0, tk.END)
    text_widget2.insert(tk.END, "Example 1 text")
    text_widget2.config(state=tk.DISABLED)

def example2():
    text_widget2.config(state=tk.NORMAL)
    text_widget2.delete(1.0, tk.END)
    text_widget2.insert(tk.END, "Example 2 text")
    text_widget2.config(state=tk.DISABLED)

example1_button = ttk.Button(frame2, text="Example 1", command=example1)
example1_button.pack(anchor='n', padx='5')

example2_button = ttk.Button(frame2, text="Example 2", command=example2)
example2_button.pack(anchor='n', padx='5')

root.mainloop()