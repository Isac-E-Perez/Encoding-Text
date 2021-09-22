# tkinter import * means that we are importing everything from tkinter library

from tkinter import *
import base64

root = Tk()  # creates the window
root.geometry('500x300')
root.resizable(True, True)  # allowing root window to change. Its size according to the users need
root.title("Encoding Project")

# root.resizable(0,0) means the root window is restricted. not resizable

Label(root, text='Encoding Project',
      fg='navy',
      font='Times 20 italic').pack()

Label(root, text='Isac E Perez',
      fg='navy',
      font='Times 12 italic').place(x=425, y=280)  # horizontal and vertical offset in pixels

# define variables

text = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()


# encode

def Encode(key, message):  # function arguments - key and message
    enc = []  # empty list

    for i in range(len(message)):
        key_c = key[i % len(key)]  # % is divide. The remainder used as an index
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        # ord() - function takes string argument of a single unicode character and returns its integer unicode value
        # chr() - function takes an integer argument and returns the string.

        # Therefore ord(message[i] converts the value of message at index i into an integer value
        # ord(key_c) converts teh key_c value to integer value

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    # base64.urlsafe_b64encode -encode a string
    # join()- joins each element of list, string and tuple by a string separator and returns the
    # glued together string
    # encode() - returns utf-8 encoded message of string
    # decode() - decodes the string
    # return gives the results of the encoded string


# decode

def Decode(key, message):  # function arguments key and message
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)  # returns the results


def Mode():
    if mode.get() == 'e':
        result.set(Encode(private_key.get(), text.get()))  # Returns the current user's text as a string

    elif mode.get() == 'd':
        result.set(Decode(private_key.get(), text.get()))

    else:
        result.set('Wrong Mode')


def Exit():
    root.destroy()  # quit the program by stopping the mainloop


def Reset():
    text.set("")
    private_key.set("")
    mode.set("")
    result.set("")


# set all the variables ot empty string

# label and button options

Label(root,
      font='Times 12 bold',
      fg='navy',
      text='STRING').place(x=60, y=60)
Entry(root,  # entry() widget used to create an input text field
      font='Times 12 italic',
      fg='navy',
      textvariable=text,  # in order to be able to ge the current text from entry widget, we must set this option to an
      # instance of the StringVar class
      bg='ghost white').place(x=120, y=60)

Label(root,
      font="Times 12 bold",
      fg='navy',
      text='KEY').place(x=60, y=90)
Entry(root,
      font='Times 12 italic',
      fg='navy',
      textvariable=private_key,
      bg='ghost white').place(x=120, y=90)

Label(root,
      font='Times 12 bold',
      fg='navy',
      text='MODE').place(x=60, y=120)
Entry(root,
      font='Times 12 italic',
      fg='navy',
      textvariable=mode,
      bg='ghost white').place(x=120, y=120)

Label(root,
      font='Times 12 bold',
      fg='navy',
      text='RESULT').place(x=60, y=150)
Entry(root,
      font='Times 12 italic',
      fg='navy',
      textvariable=result,
      bg='ghost white').place(x=120, y=150)

Button(root,
       font='Times 12 bold',
       fg='navy',
       text='RESULT',
       width=6,
       command=Mode,
       bg='OrangeRed',
       padx=8,  # how many pixels to pad widget
       pady=2).place(x=120, y=180)

Button(root,
       font='Times 12 bold',
       fg='navy',
       text='RESET',
       width=6,
       command=Reset,
       bg='LimeGreen',
       padx=6,
       pady=2).place(x=175, y=180)

Button(root,
       font='Times 12 bold',
       fg='navy',
       text='EXIT',
       width=6,
       command=Exit,
       bg='OrangeRed',
       padx=2,
       pady=2).place(x=225, y=180)

root.mainloop()
