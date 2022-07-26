from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os
from tkinter import messagebox
import webbrowser

root = Tk()
root.geometry("650x700")
root.title("Html Editor")   
root.configure(background='gray10')

open_img = ImageTk.PhotoImage(Image.open("open.png"))
run_img = ImageTk.PhotoImage(Image.open("run.jpg"),width=23,height=23)
save_img = ImageTk.PhotoImage(Image.open("save.png"))

label_filename = Label(root,text="File Name",bg="gray19",fg="white")
label_filename.place(relx=0.28,rely=0.03,anchor=CENTER)

input_filename = Entry(root,bg="gray19",fg="white")
input_filename.place(relx=0.45,rely=0.03,anchor=CENTER)

text_area = Text(root,height=38,width=80,bg="gray19",fg="white")
text_area.place(relx=0.5,rely=0.55,anchor=CENTER) 

name = ""
file_path = ""

def open_file():
    global name
    global file_path
    input_filename.delete(0,END)
    text_area.delete(1.0,END)
    
    text_file = filedialog.askopenfilename(title="Open text file", filetypes=(("html files","*.html"),))
    file_path = text_file
    name = os.path.basename(text_file)
    formated_name = name.split(".")[0]
    print(name)
    input_filename.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    text_area.insert(END,paragraph)
    text_file.close()

def save_file():
    file_name = input_filename.get()
    file = open(file_name+".html","w")
    html_data = text_area.get("1.0",END)
    print(html_data)
    file.write(html_data)
    text_area.delete(1.0,END)
    input_filename.delete(0,END)
    messagebox.showinfo("Success","The file has been saved")
def run_file():
    global file_path
    webbrowser.open_new("file://" + file_path)
    

open_button = Button(root,image=open_img,text="Open file",command=open_file)
open_button.place(relx=0.05,rely=0.04,anchor=CENTER)

save_button = Button(root,image=save_img,text="Save file",command=save_file)
save_button.place(relx=0.12,rely=0.04,anchor=CENTER)

run_button = Button(root,image=run_img,text="Close",command=run_file)
run_button.place(relx=0.2,rely=0.04,anchor=CENTER)



root.mainloop()