import tkinter as tk

root = tk.Tk()
root.title("Training Program")
root.geometry("500x300")

root.configure(bg='skyblue')


label1 = tk.Label(root, text="Smart Attendance System", 
font=("Courier New", 24), bg="blue", fg="white") 
label1.pack()

button1 = tk.Button(root, text="Select Excel File",width=20,
height=2,bg="#B4A3D8",activebackground="grey",
activeforeground="white",state=tk.NORMAL)  #adding state of the button

#possible value for state: tk.NORMAL, tk.DISABLED, tk.ACTIVE, tk.HIDDEN

button1.config(highlightbackground = "black",highlightthickness=3)
button1.pack()

root.mainloop()
