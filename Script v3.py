import os.path
import os
import tkinter
from tkinter import *

root1 = Tk()
root1.title('Debugger')
root1.geometry("360x480")

DebugData2 = Tk()
DebugData2.title('Data2 (Save Slot 3) Editor')
DebugData2.geometry("360x240")

DebugData3 = Tk()
DebugData3.title('Data3 (Options) Editor')
DebugData3.geometry("360x240")

DebugData1 = Tk()
DebugData1.title('Data1 (Save Slot 2) Editor')
DebugData1.geometry("360x240")

DebugData0 = Tk()
DebugData0.title('Data0 (Save Slot 1) Editor')
DebugData0.geometry("360x240")

data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4'
def myClick0():
    message0 = Label(root1, text="Data0 (Slot 1): Grey-Base Spawn Point Was Set. - Debugger")
    message0.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x4A\x42\xC7\x79\xE8\x41\xCE\xA7\x35\xC5'
def myClick25():
    message25 = Label(root1, text="Data0 (Slot 1): Oil-Rig Spawn Point Was Set. - Debugger")
    message25.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x4A\x42\xC7\x79\xE8\x41\xCE\xA7\x35\xC5' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x09\x44\x37\x1A\x84\x40\x1D\xC0\xD1\xC4'
def myClick40():
    message40 = Label(root1, text="Data0 (Slot 1): Submarine Spawn Point Was Set. - Debugger")
    message40.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x09\x44\x37\x1A\x84\x40\x1D\xC0\xD1\xC4' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick1():
    message1 = Label(root1, text="Data0 (Slot 1): Health Was Set To 9999 - Debugger")
    message1.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(32) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick2():
    message2 = Label(root1, text="Data0 (Slot 1): Food Was Set To 9999 - Debugger")
    message2.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(36) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick3():
    message3 = Label(root1, text="Data0 (Slot 1): Battery Was Set To 9999 - Debugger")
    message3.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(48) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick4():
    message4 = Label(root1, text="Data0 (Slot 1): Water Was Set To 9999 - Debugger")
    message4.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(40) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"
#======================================================================================================#

data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4'
def myClick20():
    message0 = Label(root1, text="Data1 (Slot 2): Grey-Base Spawn Point Was Set. - Debugger")
    message0.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x4A\x42\xC7\x79\xE8\x41\xCE\xA7\x35\xC5'
def myClick27():
    message27 = Label(root1, text="Data1 (Slot 2): Oil-Rig Spawn Point Was Set. - Debugger")
    message27.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x4A\x42\xC7\x79\xE8\x41\xCE\xA7\x35\xC5' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x09\x44\x37\x1A\x84\x40\x1D\xC0\xD1\xC4'
def myClick41():
    message41 = Label(root1, text="Data1 (Slot 2): Submarine Spawn Point Was Set. - Debugger")
    message41.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x09\x44\x37\x1A\x84\x40\x1D\xC0\xD1\xC4' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick5():
    message5 = Label(root1, text="Data1 (Slot 2): Health Was Set To 9999 - Debugger")
    message5.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(32) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick6():
    message6 = Label(root1, text="Data1 (Slot 2): Food Was Set To 9999 - Debugger")
    message6.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(36) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick7():
    message7 = Label(root1, text="Data1 (Slot 2): Battery Was Set To 9999 - Debugger")
    message7.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(48) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick8():
    message8 = Label(root1, text="Data1 (Slot 2): Water Was Set To 9999 - Debugger")
    message8.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(40) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

#=========================================================================================================#

data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4'
def myClick28():
    message28 = Label(root1, text="Data2 (Slot 3): Grey-Base Spawn Point Was Set. - Debugger")
    message28.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\xE4\x44\x94\x89\xF1\x41\x83\x9E\xC9\xC4' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"


data_in_byte = b'\x4A\x42\xC7\x79\xE8\x41\xCE\xA7\x35\xC5'
def myClick26():
    message26 = Label(root1, text="Data2 (Slot 3): Oil-Rig Spawn Point Was Set. - Debugger")
    message26.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x4A\x42\xC7\x79\xE8\x41\xCE\xA7\x35\xC5' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x09\x44\x37\x1A\x84\x40\x1D\xC0\xD1\xC4'
def myClick42():
    message41 = Label(root1, text="Data2 (Slot 3): Submarine Spawn Point Was Set. - Debugger")
    message42.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x09\x44\x37\x1A\x84\x40\x1D\xC0\xD1\xC4' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(22) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick9():
    message9 = Label(root1, text="Data2 (Slot 3): Health Was Set To 9999 - Debugger")
    message9.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(32) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick10():
    message10 = Label(root1, text="Data2 (Slot 3): Food Was Set To 9999 - Debugger")
    message10.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(36) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick11():
    message11 = Label(root1, text="Data2 (Slot 3): Battery Was Set To 9999 - Debugger")
    message11.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(48) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x0F\x27'
def myClick12():
    message12 = Label(root1, text="Data2 (Slot 3): Water Was Set To 9999 - Debugger")
    message12.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x0F\x27' 
    #Bytes to write to file
    Data2 = "Data2" 
    #Name of file

    with open(Data2, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(40) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

#=========================================================================================================#

#================================================== Data3 ==================================================#

data_in_byte = b'\x00\x00\x80'
def myClick13():
    message13 = Label(root1, text="Data3 (Options): Horizontal Sensitivity Set.")
    message13.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x00\x00\x80' 
    #Bytes to write to file
    Data3 = "Data3" 
    #Name of file

    with open(Data3, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(0) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x00\x00\x80'
def myClick14():
    message14 = Label(root1, text="Data3 (Options): Vertical Sensitivity Set.")
    message14.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x00\x00\x80' 
    #Bytes to write to file
    Data3 = "Data3" 
    #Name of file

    with open(Data3, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(4) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x01'
def myClick15():
    message15 = Label(root1, text="Data3 (Options): Inverted Y Axis")
    message15.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x01' 
    #Bytes to write to file
    Data3 = "Data3" 
    #Name of file

    with open(Data3, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(8) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x01'
def myClick16():
    message16 = Label(root1, text="Data3 (Options): Inverted X Axis")
    message16.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x01' 
    #Bytes to write to file
    Data3 = "Data3" 
    #Name of file

    with open(Data3, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(9) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x01'
def myClick17():
    message17 = Label(root1, text="Data3 (Options): Enable Manual Camera")
    message17.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x01' 
    #Bytes to write to file
    Data3 = "Data3" 
    #Name of file

    with open(Data3, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(10) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes 

data_in_byte = b'\x01'
def myClick18():
    message18 = Label(root1, text="Data3 (Options): Enable C-Stick Aim")
    message18.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x01' 
    #Bytes to write to file
    Data3 = "Data3" 
    #Name of file

    with open(Data3, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(11) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes 

data_in_byte = b'\x01'
def myClick19():
    message19 = Label(root1, text="Data3 (Options): Enable Game Chat")
    message19.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x01' 
    #Bytes to write to file
    Data3 = "Data3" 
    #Name of file

    with open(Data3, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(12) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes 

print('ERROR WINDOW - ERRORS WILL APPEAR HERE.')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')
print('!!!WARNING BACKUP YOUR SAVE DATA BEFORE CONTINUING!!!')


myButton0 = Button(DebugData0, text="Data0 (Slot 1): Spawn-Point At Grey-Base", command=myClick0, fg="white", bg="black")
myButton0.pack()

myButton25 = Button(DebugData0, text="Data0 (Slot 1): Spawn-Point At Oil-Rig", command=myClick25, fg="white", bg="black")
myButton25.pack()

myButton40 = Button(DebugData0, text="Data0 (Slot 1): Spawn-Point At Submarine", command=myClick40, fg="white", bg="black")
myButton40.pack()

myButton1 = Button(DebugData0, text="Data0 (Slot 1): 9999 Health", command=myClick1, fg="white", bg="black")
myButton1.pack()

myButton2 = Button(DebugData0, text="Data0 (Slot 1): 9999 Food", command=myClick2, fg="white", bg="black")
myButton2.pack()

myButton3 = Button(DebugData0, text="Data0 (Slot 1): 9999 Battery", command=myClick3, fg="white", bg="black")
myButton3.pack()

myButton4 = Button(DebugData0, text="Data0 (Slot 1): 9999 Water", command=myClick4, fg="white", bg="black")
myButton4.pack()

myButton20 = Button(DebugData1, text="Data1 (Slot 2): Spawn-Point At Grey-Base", command=myClick20, fg="black", bg="white")
myButton20.pack()

myButton27 = Button(DebugData1, text="Data1 (Slot 2): Spawn-Point At Oil-Rig", command=myClick27, fg="black", bg="white")
myButton27.pack()

myButton41 = Button(DebugData1, text="Data1 (Slot 2): Spawn-Point At Submarine", command=myClick41, fg="black", bg="white")
myButton41.pack()

myButton5 = Button(DebugData1, text="Data1 (Slot 2): 9999 Health", command=myClick5, fg="black", bg="white")
myButton5.pack()

myButton6 = Button(DebugData1, text="Data1 (Slot 2): 9999 Food", command=myClick6, fg="black", bg="white")
myButton6.pack()

myButton7 = Button(DebugData1, text="Data1 (Slot 2): 9999 Battery", command=myClick7, fg="black", bg="white")
myButton7.pack()

myButton8 = Button(DebugData1, text="Data1 (Slot 2): 9999 Water", command=myClick8, fg="black", bg="white")
myButton8.pack()

myButton28 = Button(DebugData2, text="Data2 (Slot 3): Spawn-Point At Grey-Base", command=myClick28, fg="blue", bg="black")
myButton28.pack()

myButton26 = Button(DebugData2, text="Data2 (Slot 3): Spawn-Point At Oil-Rig", command=myClick26, fg="blue", bg="black")
myButton26.pack()

myButton42 = Button(DebugData2, text="Data2 (Slot 3): Spawn-Point At Submarine", command=myClick42, fg="blue", bg="black")
myButton42.pack()

myButton9 = Button(DebugData2, text="Data2 (Slot 3): 9999 Health", command=myClick9, fg="blue", bg="black")
myButton9.pack()

myButton10 = Button(DebugData2, text="Data2 (Slot 3): 9999 Food", command=myClick10, fg="blue", bg="black")
myButton10.pack()

myButton11 = Button(DebugData2, text="Data2 (Slot 3): 9999 Battery", command=myClick11, fg="blue", bg="black")
myButton11.pack()

myButton12 = Button(DebugData2, text="Data2 (Slot 3): 9999 Water", command=myClick12, fg="blue", bg="black")
myButton12.pack()

myButton13 = Button(DebugData3, text="Data3 (Options): Max Horizontal Sensitivity Set", command=myClick13, fg="blue", bg="white")
myButton13.pack()

myButton14 = Button(DebugData3, text="Data3 (Options): Max Vertical Sensitivity Set", command=myClick14, fg="blue", bg="white")
myButton14.pack()

myButton15 = Button(DebugData3, text="Data3 (Options): Invert Y Set", command=myClick15, fg="blue", bg="white")
myButton15.pack()

myButton16 = Button(DebugData3, text="Data3 (Options): Invert X Set", command=myClick16, fg="blue", bg="white")
myButton16.pack()

myButton17 = Button(DebugData3, text="Data3 (Options): Manual Camera Set", command=myClick17, fg="blue", bg="white")
myButton17.pack()

myButton18 = Button(DebugData3, text="Data3 (Options): C-Stick Aim Set", command=myClick18, fg="blue", bg="white")
myButton18.pack()

myButton19 = Button(DebugData3, text="Data3 (Options): Game Chat Set", command=myClick19, fg="blue", bg="white")
myButton19.pack()












message01 = Label(root1, text="Created By: Cracko298")
message01.pack()
message02 = Label(root1, text="DO NOT CLOSE THIS WINDOW!")
message02.pack()
message03 = Label(root1, text="====================================")
message03.pack()

root1.mainloop()
DebugData2.mainloop()
DebugData3.mainloop()
DebugData1.mainloop()
DebugData0.mainloop()