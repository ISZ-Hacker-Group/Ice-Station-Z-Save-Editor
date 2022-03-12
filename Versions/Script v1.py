import os.path
import os
import tkinter
from tkinter import *
import random

data_in_byte = b'\x64\x64'
def myClick1():
    message1 = Label(root, text="Data0 (Slot 1): Health Was Set To 9999 - Debugger")
    message1.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(32) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick2():
    message2 = Label(root, text="Data0 (Slot 1): Food Was Set To 9999 - Debugger")
    message2.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(35) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick3():
    message3 = Label(root, text="Data0 (Slot 1): Battery Was Set To 9999 - Debugger")
    message3.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(38) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick4():
    message4 = Label(root, text="Data0 (Slot 1): Water Was Set To 9999 - Debugger")
    message4.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(48) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"
#======================================================================================================#

data_in_byte = b'\x64\x64'
def myClick5():
    message5 = Label(root, text="Data1 (Slot 2): Health Was Set To 9999 - Debugger")
    message5.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(32) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick6():
    message6 = Label(root, text="Data1 (Slot 2): Food Was Set To 9999 - Debugger")
    message6.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(35) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick7():
    message7 = Label(root, text="Data1 (Slot 2): Battery Was Set To 9999 - Debugger")
    message7.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(38) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick8():
    message8 = Label(root, text="Data1 (Slot 2): Water Was Set To 9999 - Debugger")
    message8.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(48) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

#=========================================================================================================#

data_in_byte = b'\x64\x64'
def myClick9():
    message9 = Label(root, text="Data2 (Slot 3): Health Was Set To 9999 - Debugger")
    message9.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(32) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick10():
    message10 = Label(root, text="Data2 (Slot 3): Food Was Set To 9999 - Debugger")
    message10.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(35) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick11():
    message11 = Label(root, text="Data2 (Slot 3): Battery Was Set To 9999 - Debugger")
    message11.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(38) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick12():
    message12 = Label(root, text="Data2 (Slot 3): Water Was Set To 9999 - Debugger")
    message12.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(48) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

root = Tk()
root.geometry("750x450")

myButton1 = Button(root, text="Data0 (Slot 1): 9999 Health", command=myClick1, fg="white", bg="black")
myButton1.pack()

myButton2 = Button(root, text="Data0 (Slot 1): 9999 Food", command=myClick2, fg="white", bg="black")
myButton2.pack()

myButton3 = Button(root, text="Data0 (Slot 1): 9999 Battery", command=myClick3, fg="white", bg="black")
myButton3.pack()

myButton4 = Button(root, text="Data0 (Slot 1): 9999 Water", command=myClick4, fg="white", bg="black")
myButton4.pack()

myButton5 = Button(root, text="Data1 (Slot 2): 9999 Health", command=myClick5, fg="black", bg="white")
myButton5.pack()

myButton6 = Button(root, text="Data1 (Slot 2): 9999 Food", command=myClick6, fg="black", bg="white")
myButton6.pack()

myButton7 = Button(root, text="Data1 (Slot 2): 9999 Battery", command=myClick7, fg="black", bg="white")
myButton7.pack()

myButton8 = Button(root, text="Data1 (Slot 2): 9999 Water", command=myClick8, fg="black", bg="white")
myButton8.pack()

myButton9 = Button(root, text="Data2 (Slot 3): 9999 Health", command=myClick9, fg="blue", bg="black")
myButton9.pack()

myButton10 = Button(root, text="Data2 (Slot 3): 9999 Food", command=myClick10, fg="blue", bg="black")
myButton10.pack()

myButton11 = Button(root, text="Data2 (Slot 3): 9999 Battery", command=myClick11, fg="blue", bg="black")
myButton11.pack()

myButton12 = Button(root, text="Data2 (Slot 3): 9999 Water", command=myClick12, fg="blue", bg="black")
myButton12.pack()

root = Tk()
root.geometry("750x450")

root.mainloop()

#Edit Data in Bytes Code.
data_in_byte = b'\x64\x64' #Bytes to write to file
Data0 = "Data0" #Name of file

with open(Data0, 'rb+') as binary_file: #open file as binary
 binary_file.seek(33) #Move Editing to Offset 33
 binary_file.write(data_in_byte) #Writes the bytes from "data_in_byte"