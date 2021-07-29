from tkinter import *

main_window = Tk()

#Text input area
screen=Entry(
    main_window,
    width = 50,
    borderwidth=4
)
screen.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=5,
    pady=10
)

list_of_numbers=[]

#function to get numbers

def number_input(number):
    current_value = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current_value)+str(number))

def clear_values():
    list_of_numbers.clear()
    screen.delete(0, END)

def sum_of_values():
    num1=screen.get()
    list_of_numbers.append(num1)
    screen.delete(0, END)

def equals():
    num1 = screen.get()
    list_of_numbers.append(int(num1))
    screen.delete(0, END)

    sum=0
    for values in list_of_numbers:
        sum+=int(values)
    screen.insert(0,str(sum))



#buttons 9-0,clear,equal,add,sub,multiplier
button_9=Button(
    main_window,
    text="9",
    bg="green",
    padx=50,
    pady=30,
    command= lambda : number_input(9)

).grid(row=1 ,column=2 )

button_8=Button(
    main_window,
    text="8",
    bg="green",
    padx=50,
    pady=30,
    command=lambda : number_input(8)

).grid(row=1 ,column=1 )

button_7=Button(
    main_window,
    text="7",
    bg="green",
    padx=50,
    pady=30,
    command= lambda : number_input(7)

).grid(row=1 ,column=0 )

button_6=Button(
    main_window,
    text="6",
    bg="green",
    padx=50,
    pady=30,
    command= lambda : number_input(6)

).grid(row=2 ,column=2 )

button_5=Button(
    main_window,
    text="5",
    bg="green",
    padx=50,
    pady=30,
    command= lambda : number_input(5)

).grid(row=2,column=1 )

button_4=Button(
    main_window,
    text="4",
    bg="green",
    padx=50,
    pady=30,
    command= lambda : number_input(4)

).grid(row=2 ,column=0 )

button_3=Button(
    main_window,
    bg="green",
    text="3",
    padx=50,
    pady=30,
    command= lambda : number_input(3)

).grid(row=3 ,column=2 )

button_2=Button(
    main_window,
    text="2",
    bg="green",
    padx=50,
    pady=30,
    command= lambda : number_input(2)

).grid(row= 3,column=1 )

button_1=Button(
    main_window,
    text="1",
    bg="green",
    padx=50,
    pady=30,
    command= lambda : number_input(1)

).grid(row=3 ,column=0 )

button_0=Button(
    main_window,
    text="0",
    bg="green",
    padx=50,
    pady=30,
    command= lambda : number_input(0)

).grid(row=4 ,column=0 )

#button function
button_add=Button(
    main_window,
    text="+",
    bg="yellow",
    padx=50,
    pady=30,
    command= sum_of_values

).grid(row=1 ,column=3 )

'''button_sub=Button(
    main_window,
    text="-",
    padx=40,
    pady=20,
    command=

).grid(row=1 ,column=3 )

button_product=Button(
    main_window,
    text="*",
    padx=40,
    pady=20,
    command=

).grid(row=2 ,column=3 )'''

button_clear=Button(
    main_window,
    text="clr",
    bg="yellow",
    padx=50,
    pady=30,
    command= clear_values

).grid(row=4 ,column=1 )

button_equal=Button(
    main_window,
    text="=",
    bg="red",
    padx=100,
    pady=30,
    command= equals

).grid(row=4 ,column=2 , columnspan=2)


main_window.mainloop()
