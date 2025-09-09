from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    if masg.strip() == "":
        return
    try:
        textget = change(text=masg, src=s, dest=d)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, textget)
    except Exception as e:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, f"Error: {str(e)}")

def clear_text():
    Sor_txt.delete(1.0, END)
    dest_txt.delete(1.0, END)

def swap_languages():
    current_src = comb_sor.get()
    current_dest = comb_dest.get()
    comb_sor.set(current_dest)
    comb_dest.set(current_src)
    
    # Also swap the text if there's any translation
    if dest_txt.get(1.0, END).strip():
        current_src_text = Sor_txt.get(1.0, END)
        current_dest_text = dest_txt.get(1.0, END)
        Sor_txt.delete(1.0, END)
        Sor_txt.insert(END, current_dest_text)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, current_src_text)

root = Tk()
root.title("Language Translator")
root.geometry("600x750")
root.config(bg="#f0f2f5")
root.resizable(False, False)

# Color scheme
primary_color = "#2D5F7D"
secondary_color = "#4A90E2"
accent_color = "#50C878"
light_bg = "#FFFFFF"
dark_text = "#333333"
light_text = "#FFFFFF"

# Main title
title_frame = Frame(root, bg=primary_color, height=80)
title_frame.pack(fill=X)
title_frame.pack_propagate(False)

lab_txt = Label(title_frame, text="Language Translator", 
                font=("Arial", 24, 'bold'), fg=light_text, bg=primary_color)
lab_txt.pack(expand=True)

# Main content frame
main_frame = Frame(root, bg=light_bg, padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

# Source section
source_label = Label(main_frame, text="Source Text", 
                    font=("Arial", 14, 'bold'), fg=dark_text, bg=light_bg)
source_label.grid(row=0, column=0, sticky=W, pady=(0, 10))

Sor_txt = Text(main_frame, font=("Arial", 12), wrap=WORD, 
               bd=2, relief=SOLID, padx=10, pady=10, 
               highlightthickness=1, highlightcolor=secondary_color,
               highlightbackground="#ddd", height=8)
Sor_txt.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 20))

# Language selection frame
lang_frame = Frame(main_frame, bg=light_bg)
lang_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(0, 20))

# Source language
src_label = Label(lang_frame, text="From:", 
                 font=("Arial", 11, 'bold'), fg=dark_text, bg=light_bg)
src_label.pack(side=LEFT, padx=(0, 10))

list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(lang_frame, values=list_text, 
                       font=("Arial", 11), state="readonly", width=15)
comb_sor.pack(side=LEFT, padx=(0, 20))
comb_sor.set("english")

# Swap button
swap_btn = Button(lang_frame, text="⇄", font=("Arial", 14, 'bold'), 
                 bg=secondary_color, fg=light_text, bd=0,
                 command=swap_languages, cursor="hand2", width=3)
swap_btn.pack(side=LEFT, padx=10)

# Destination language
dest_label = Label(lang_frame, text="To:", 
                  font=("Arial", 11, 'bold'), fg=dark_text, bg=light_bg)
dest_label.pack(side=LEFT, padx=(0, 10))

comb_dest = ttk.Combobox(lang_frame, values=list_text, 
                        font=("Arial", 11), state="readonly", width=15)
comb_dest.pack(side=LEFT)
comb_dest.set("hindi")

# Button frame
btn_frame = Frame(main_frame, bg=light_bg)
btn_frame.grid(row=3, column=0, columnspan=3, pady=(0, 20))

# Translate button
button_change = Button(btn_frame, text="Translate", font=("Arial", 12, 'bold'),
                      bg=accent_color, fg=light_text, bd=0, padx=20, pady=8,
                      command=data, cursor="hand2")
button_change.pack(side=LEFT, padx=(0, 15))

# Clear button
clear_btn = Button(btn_frame, text="Clear", font=("Arial", 12),
                  bg="#E0E0E0", fg=dark_text, bd=0, padx=20, pady=8,
                  command=clear_text, cursor="hand2")
clear_btn.pack(side=LEFT)

# Destination section
dest_label = Label(main_frame, text="Translated Text", 
                  font=("Arial", 14, 'bold'), fg=dark_text, bg=light_bg)
dest_label.grid(row=4, column=0, sticky=W, pady=(0, 10))

dest_txt = Text(main_frame, font=("Arial", 12), wrap=WORD, 
               bd=2, relief=SOLID, padx=10, pady=10,
               highlightthickness=1, highlightcolor=secondary_color,
               highlightbackground="#ddd", height=8)
dest_txt.grid(row=5, column=0, columnspan=3, sticky="ew")

# Footer
footer = Label(root, text="Powered by Google Translate API", 
              font=("Arial", 10), fg="#888888", bg="#f0f2f5")
footer.pack(side=BOTTOM, pady=10)

# Configure grid weights for responsive design
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=0)
main_frame.columnconfigure(2, weight=1)

# Add some padding to all widgets
for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Add hover effects
def on_enter(e):
    e.widget['background'] = '#3B5998' if e.widget == button_change else '#45a049' if e.widget == swap_btn else '#C8C8C8'

def on_leave(e):
    e.widget['background'] = accent_color if e.widget == button_change else secondary_color if e.widget == swap_btn else '#E0E0E0'

button_change.bind("<Enter>", on_enter)
button_change.bind("<Leave>", on_leave)
clear_btn.bind("<Enter>", on_enter)
clear_btn.bind("<Leave>", on_leave)
swap_btn.bind("<Enter>", on_enter)
swap_btn.bind("<Leave>", on_leave)

root.mainloop()