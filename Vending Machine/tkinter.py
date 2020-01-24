from tkinter import *

def gui():
    window = Tk()
    label = Label(window,text = "Product")

    if list1[1][i] == 'Lays':
        label1 = Label(window,text = "Lays")
        photo = PhotoImage(file = "image/1.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()

    elif list1[1][i] == 'Kurkure':
        label1 = Label(window,text = "Kurkure")
        photo = PhotoImage(file = "image/2.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'A3':
        label1 = Label(window,text = "Snickers")
        photo = PhotoImage(file = "image/3.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'A4':
        label1 = Label(window,text = "Coca Cola")
        photo = PhotoImage(file = "image/4.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'A5':
        label1 = Label(window,text = "Ding Dong")
        photo = PhotoImage(file = "image/5.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'A6':
        label1 = Label(window,text = "Doritos")
        photo = PhotoImage(file = "image/6.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'A7':
        label1 = Label(window,text = "M&Ms")
        photo = PhotoImage(file = "image/7.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'A8':
        label1 = Label(window,text = "KitKat")
        photo = PhotoImage(file = "image/8.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
    elif item== 'A9':
        label1 = Label(window,text = "Sprite")
        photo = PhotoImage(file = "image/9.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'A10':
        label1 = Label(window,text = "Oreo")
        photo = PhotoImage(file = "image/10.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B1':
        label1 = Label(window,text = "Red Bull")
        photo = PhotoImage(file = "image/11.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B2':
        label1 = Label(window,text = "Twitch")
        photo = PhotoImage(file = "image/12.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B3':
        label1 = Label(window,text = "Ruffles")
        photo = PhotoImage(file = "image/13.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B4':
        label1 = Label(window,text = "Milk Treat")
        photo = PhotoImage(file = "image/14.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B5':
        label1 = Label(window,text = "Water")
        photo = PhotoImage(file = "image/15.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B6':
        label1 = Label(window,text = "Milo")
        photo = PhotoImage(file = "image/16.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B7':
        label1 = Label(window,text = "Cheetos")
        photo = PhotoImage(file = "image/17.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B8':
        label1 = Label(window,text = "Dairy Milk")
        photo = PhotoImage(file = "image/18.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B9':
        label1 = Label(window,text = "Biscuit")
        photo = PhotoImage(file = "image/19.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    elif item== 'B10':
        label1 = Label(window,text = "Skittles")
        photo = PhotoImage(file = "image/20.gif")
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1,image = photo).pack()
        
    window.mainloop()
