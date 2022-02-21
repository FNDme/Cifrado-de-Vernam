from tkinter import *
from tkinter import messagebox
from Vernam import *

base = Tk()

base.title('Vernam Cipher')
base.resizable(False, False)
base.geometry('500x400')
base.configure(background='#232426')


Canva = Canvas(base, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
Canva.place(x=0, y=335)

sz = StringVar()
sz.set("Bin size: 0")

def gui_encrypt():

    if auto.get():
        temp = encrypt(inputText.get('1.0', END).rstrip("\n"))
    else:
        if len(txt_to_bin(keyText.get('1.0', END).rstrip("\n"))) != len(txt_to_bin(inputText.get('1.0', END).rstrip("\n"))):
            messagebox.showerror('Error', 'key size and input size must be equal')
            return
        else:
            temp = encrypt(inputText.get('1.0', END).rstrip("\n"), keyText.get('1.0', END).rstrip("\n"))

    sz.set("Bin size: " + str(len(temp['cripted_bin'])))

    outputText.config(state=NORMAL)
    outputText.delete('1.0', END)
    outputText.insert('1.0', temp['cripted_ascii'])
    outputText.config(state=DISABLED)

    outputTextBin.config(state=NORMAL)
    outputTextBin.delete('1.0', END)
    outputTextBin.insert('1.0', temp['cripted_bin'])
    outputTextBin.config(state=DISABLED)

    keyText.delete('1.0', END)
    keyText.insert('1.0', temp['key_ascii'])

    keyTextBin.config(state=NORMAL)
    keyTextBin.delete('1.0', END)
    keyTextBin.insert('1.0', temp['key_bin'])
    keyTextBin.config(state=DISABLED)

    inputTextBin.config(state=NORMAL)
    inputTextBin.delete('1.0', END)
    inputTextBin.insert('1.0', txt_to_bin(inputText.get('1.0', END).rstrip("\n")))
    inputTextBin.config(state=DISABLED)

    return

def gui_decrypt():
    temp = dict()
    temp['cripted_ascii'] = (inputText.get('1.0', END).rstrip("\n"))
    temp['key_ascii'] = (keyText.get('1.0', END).rstrip("\n"))

    sz.set("Bin size: " + str(len(txt_to_bin(temp['cripted_ascii']))))

    inputTextBin.config(state=NORMAL)
    inputTextBin.delete('1.0', END)
    inputTextBin.insert('1.0', txt_to_bin(temp['cripted_ascii']))
    inputTextBin.config(state=DISABLED)

    keyTextBin.config(state=NORMAL)
    keyTextBin.delete('1.0', END)
    keyTextBin.insert('1.0', txt_to_bin(temp['key_ascii']))
    keyTextBin.config(state=DISABLED)

    decrypted = decrypt(temp)

    outputText.config(state=NORMAL)
    outputText.delete('1.0', END)
    outputText.insert('1.0', decrypted)
    outputText.config(state=DISABLED)
    
    outputTextBin.config(state=NORMAL)
    outputTextBin.delete('1.0', END)
    outputTextBin.insert('1.0', txt_to_bin(decrypted))
    outputTextBin.config(state=DISABLED)

    return

def clear():
    inputText.delete('1.0', END)
    
    inputTextBin.config(state=NORMAL)
    inputTextBin.delete('1.0', END)
    inputTextBin.config(state=DISABLED)

    keyText.delete('1.0', END)

    keyTextBin.config(state=NORMAL)
    keyTextBin.delete('1.0', END)
    keyTextBin.config(state=DISABLED)

    outputText.config(state=NORMAL)
    outputText.delete('1.0', END)
    outputText.config(state=DISABLED)

    outputTextBin.config(state=NORMAL)
    outputTextBin.delete('1.0', END)
    outputTextBin.config(state=DISABLED)

inputTextLabel = Label(base, text='Input Text')
inputTextLabel.place(x=30, y=30)
inputTextLabel.configure(background='#232426', foreground='#F2F2F2')

inputTextBinLabel = Label(base, text='Input Text (Bin)')
inputTextBinLabel.place(x=280, y=30)
inputTextBinLabel.configure(background='#232426', foreground='#BFBFBF')

keyTextLabel = Label(base, text='Key')
keyTextLabel.place(x=30, y=130)
keyTextLabel.configure(background='#232426', foreground='#F2F2F2')

keyTextBinLabel = Label(base, text='Key (Bin)')
keyTextBinLabel.place(x=280, y=130)
keyTextBinLabel.configure(background='#232426', foreground='#BFBFBD')

outputTextLabel = Label(base, text='Output Text')
outputTextLabel.place(x=30, y=230)
outputTextLabel.configure(background='#232426', foreground='#BFBFBD')

outputTextBinLabel = Label(base, text='Output Text (Bin)')
outputTextBinLabel.place(x=280, y=230)
outputTextBinLabel.configure(background='#232426', foreground='#BFBFBD')

sizeLabel = Label(base, textvariable=sz)
sizeLabel.place(x=230, y=360)
sizeLabel.configure(background='#2a2b2d', foreground='#BFBFBD')

inputText = Text(base, width=25, height=3)
inputText.place(x=20, y=60)
inputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)

inputTextBin = Text(base, width=25, height=3)
inputTextBin.place(x=270, y=60)
inputTextBin.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)

keyText = Text(base, width=25, height=3)
keyText.place(x=20, y=160)
keyText.configure(background='#04BF68', foreground='#232426', borderwidth=0)

keyTextBin = Text(base, width=25, height=3)
keyTextBin.place(x=270, y=160)
keyTextBin.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)

outputText = Text(base, width=25, height=3)
outputText.place(x=20, y=260)
outputText.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)

outputTextBin = Text(base, width=25, height=3)
outputTextBin.place(x=270, y=260)
outputTextBin.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)

Encrypt = Button(base, text='Encrypt', command=lambda: gui_encrypt())
Encrypt.place(x=30, y=355)
Encrypt.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

Decript = Button(base, text='Decrypt', command=lambda: gui_decrypt())
Decript.place(x=110, y=355)
Decript.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

Clear = Button(base, text='Clear', command=lambda: clear())
Clear.place(x=410, y=355)
Clear.configure(background='#04BF68', foreground='#155939', borderwidth=0, activebackground='#232426', pady=5, padx=10)

auto = BooleanVar()

on = Radiobutton(base, text='Auto', variable=auto, value=1)
on.place(x=320, y=345)
on.configure(background='#2a2b2d', foreground='#BFBFBF', activebackground='#232426', activeforeground='#BFBFBF', selectcolor='#232426')

off = Radiobutton(base, text='Manual', variable=auto, value=0)
off.place(x=320, y=370)
off.configure(background='#2a2b2d', foreground='#BFBFBF', activebackground='#232426', activeforeground='#BFBFBF', selectcolor='#232426')

base.mainloop()