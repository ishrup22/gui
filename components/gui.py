from tkinter import*
root =Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height,screen_width)
root.geometry(f"{screen_width-50}x{screen_height-50}")
root.title("GUI")
root.iconbitmap("./components/editor.ico")

# define images
upload = PhotoImage(file="./components/upload.png")
col = "#d8d9f2"
win = "f8f8f8"

f1=Frame(root,bg="red",width=500)
f1.pack(side=RIGHT,fill=Y)

f2=Frame(root,bg="green",height=650)
f2.pack(side=TOP,fill=X)

f3=Frame(root,bg="orange",width=500)
f3.pack(side=BOTTOM,fill=X)

root.mainloop()