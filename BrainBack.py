from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

def multiple_chr(inpt):
    toret = []
    for i in inpt:
        toret.append(chr(int(i)))
    return "".join(toret)
    
def save_file(event=0):
    f = asksaveasfile(initialfile = 'Untitled.bf',
defaultextension=".bf",filetypes=[("All Files","*.*"),("Brainfuck файли","*.bf")])
    try:
        file = open(f.name,"w")
        file.write(text.get(0.0,END))
        file.close()
        root.title("BrainBack - "+f.name)
    except AttributeError: pass

def new():
    if text.get(0.0,END) != "":
        choice = askyesnocancel("Незбережений файл", "У вас є незбережений файл! Закрити його і натомість відкрити новий?")
        if choice: save_file()
        elif choice == None: return
    text.delete(0.0,END)
    root.title("BrainBack - Безіменний файл")

def open_file(event=0):
    if text.get(0.0,END) != "":
        choice = askyesnocancel("Незбережений файл", "У вас є незбережений файл! Закрити його і натомість відкрити новий?")
        if choice:
            save_file()
        elif choice == None:
            return
    f = askopenfilename(title='Відкрити файл BrainF*ck',initialdir='/',filetypes=(("All Files","*.*"),("Brainfuck файли","*.bf")))
    try:
        file = open(f,"r")
        text.delete(0.0,END)
        text.insert(INSERT,file.read())
        file.close()
        root.title("BrainBack - "+f)
    except: pass
    
def about():
    showinfo("About","BrainBack: free BrainF*ck interpretator")
   
def interpretate_symbol(symbol,string,cur_index,space_used,toret):   
    if symbol == "+":
        string[cur_index] += 1
    elif symbol == "-":
        string[cur_index] -= 1
    elif symbol == ">":
        cur_index += 1
        if cur_index > space_used:
                space_used = cur_index
    elif symbol == "<":
        cur_index -= 1
        if cur_index < 0:
            showerror("Error","Index Error")
    elif symbol == ".":
        toret.append(str(string[cur_index]))
#     elif symbol == "[":
#         for c in range(0,cur_index):
            
    return (string,cur_index,space_used,toret)

def run(event=0):
    string = []
    for i in range(0,30000):
        string.append(0)
    cur_index = 0
    space_used = 0
    toret = []
    for i in text.get(0.0,END):
        string,cur_index,space_used,toret = interpretate_symbol(i,string,cur_index,space_used,toret)
    
    Output.delete(0.0,END)
    if is_ascii.get() == 0:
        Output.insert(0.0,"; ".join(toret))
    else:
        Output.insert(0.0,multiple_chr(toret))

def donothing():
    pass

root = Tk()
root.title("BrainBack - Безіменний файл")
root.bind('<F9>',run)
root.bind('<Control-s>',save_file)
root.bind('<Control-o>',open_file)

is_ascii = IntVar()
language = IntVar()

Output = Text(height=4)
Output.pack(side=BOTTOM)

text = Text(relief='flat')
text.pack(side=LEFT)


# Menu
menubar = Menu(root)

# File Menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Edit menu
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)
# editmenu.add_separator()
# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)
# menubar.add_cascade(label="Edit", menu=editmenu)

langmenu = Menu(menubar,tearoff=0)
langmenu.add_radiobutton(label="Українська мова", variable=language,value=0)
langmenu.add_radiobutton(label="Engilsh language", variable=language,value=1)
menubar.add_cascade(label="Language", menu=langmenu)

runmenu = Menu(menubar, tearoff=0)
runmenu.add_command(label="Run", command=run)
runmenu.add_separator()
runmenu.add_radiobutton(label="Run with numbers",variable=is_ascii,value=0)
runmenu.add_radiobutton(label="Run with ASCII",variable=is_ascii,value=1)
menubar.add_cascade(label="Run", menu=runmenu)

# Help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()