from tkinter import Tk, Label, PhotoImage

text1 = "Create a new Makefile in the bin folder, edit it and then type in the following into the Makefile:"
text2 = "The include folder needs to have your raylib.h file."
text3 = "The lib folder needs to have your libraylib.a file."
text4 = "The src folder needs to have your .cpp, .h files." 
window = Tk()
window.title('The Raylib Makefile Guide')
window.resizable(False, False)
window.geometry("1200x800")
window.config(bg="white")
image0 = PhotoImage(file="image0.png")
image1 = PhotoImage(file="image1.png")
note = Label(window,text="NOTE:THIS WILL ONLY WORK IF YOU ARE WORKING WITH RAYLIB AND C++ !!!")
note.pack()
tlabel8 = Label(window,text="                   ")
tlabel8.pack()
tlabel8 = Label(window,text="                   ")
tlabel8.pack()
tlabel8 = Label(window,text="                   ")
tlabel8.pack()

tlabel3 = Label(window,text="This is how your projects structure should look like(If it's not then this wont work!):")
tlabel3.pack()
label2 = Label(window,image=image1)
label2.pack()
tlabel4 = Label(window,text=text2)
tlabel4.pack()
tlabel5 = Label(window,text=text3)
tlabel5.pack()
tlabel6 = Label(window,text=text4)
tlabel6.pack()
tlabel7 = Label(window,text="                   ")
tlabel7.pack()
tlabel = Label(window,text=text1)
tlabel.pack()
label1 = Label(window,image=image0)
label1.pack()
rayliblogo = PhotoImage(file="rayliblogo.png")
label8 = Label(window,image=rayliblogo)
label8.pack()

window.mainloop()

