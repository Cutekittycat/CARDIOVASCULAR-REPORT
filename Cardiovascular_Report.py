from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Cardiovascular Report")
root.geometry("600x600")
root.configure(bg="light blue")

q1rb=StringVar(value=0)

q1=Label(root, text = "Do You Experience Shortness Of Breath During Routine Activites?")
q1.pack()
q1radio1=Radiobutton(root, text = "Yes", variable=q1rb, value="Yes")
q1radio1.pack()
q1radio2=Radiobutton(root, text = "No", variable=q1rb, value="No")
q1radio2.pack()

q2rb=StringVar(value=0)

q2=Label(root, text = "Do You Have Swelling In The Feet/Ankles/Legs(Shoes Feel Tighter) Or Abdomen?")
q2.pack()
q2radio1=Radiobutton(root, text = "Yes", variable=q2rb, value="Yes")
q2radio1.pack()
q2radio2=Radiobutton(root, text = "No", variable=q2rb, value="No")
q2radio2.pack()

q3rb=StringVar(value=0)

q3=Label(root, text = "Do You Feel Any Of These Symptoms - Confusion, Disorientation Or Loss Of Memory?")
q3.pack()
q3radio1=Radiobutton(root, text = "Yes", variable=q3rb, value="Yes")
q3radio1.pack()
q3radio2=Radiobutton(root, text = "No", variable=q3rb, value="No")
q3radio2.pack()

q4rb=StringVar(value=0)

q4=Label(root, text = "Do You Experience Persistent Wheezing/Coughing That Produces White Or Pink Blood Tinged Mucus?")
q4.pack()
q4radio1=Radiobutton(root, text = "Yes", variable=q4rb, value="Yes")
q4radio1.pack()
q4radio2=Radiobutton(root, text = "No", variable=q4rb, value="No")
q4radio2.pack()

q5rb=StringVar(value=0)

q5=Label(root, text = "Do You Experience Shortness Of Breath While At Rest/Lying Down?")
q5.pack()
q5radio1=Radiobutton(root, text = "Yes", variable=q5rb, value="Yes")
q5radio1.pack()
q5radio2=Radiobutton(root, text = "No", variable=q5rb, value="No")
q5radio2.pack()

def Cardiovascular_score():
    score = 0
    if q1rb.get()=="Yes":
        score = score+10
        print(score)
    if q2rb.get()=="Yes":
        score = score+10
        print(score)
    if q3rb.get()=="Yes":
        score = score+10
        print(score)
    if q4rb.get()=="Yes":
        score = score+10
        print(score)
    if q5rb.get()=="Yes":
        score = score+10
        print(score)
    
    if score <= 10:
        messagebox.showinfo("Report","You Don't Need To Visit A Doctor.")
    elif score > 10 and score <= 30:
        messagebox.showinfo("Report","You Might Perhaps Have To Visit A Doctor.")
    else :
        messagebox.showinfo("Report","I Strongly Advise You To Visit A Doctor")
btn = Button(root, text= "Click Me", command = Cardiovascular_score)
btn.pack()
root.mainloop()