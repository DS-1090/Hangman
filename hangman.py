from tkinter import *
import random
r=Tk()
r.title("Hangman")
r.geometry("600x600")
r.configure(bg='#FEE227')

c=Canvas(r,bg='#B042FF',width=600,height=800)
c.create_line(100,100,100,300,fill='#FEE227',width=7)
c.create_line(100,100,200,100,fill='#FEE227',width=7)
i=0
j=0
guess=0
score=0
l1=Label(r,text="\nenter a word:",bg='#FEE227',font='Arial')
l1.pack()
e1=Entry(r)
e1.pack()
l=Label(r,text="")
e=Entry(r)
l.pack()
e.pack()
m=Message(r,text='')
m.pack()
l.config(text="\nEnter a letter(total 7 guesses):\n",bg='#FEE227',font='Arial')
guessed=[]
def func(event):
    global i,j,guess,guessed,score
    guess=guess+1
    if(guess==8):
        z=Label(r,text="game over please exit",bg='#FEE227',font='Arial')
        z.pack()
        return

    letter=e.get()
    word=e1.get()
    e1.forget()
    l1.forget()

    m.config(text=f"\nguesses done:{guess} \n",bg='#FEE227',font='Arial')


    if(letter in word):
        guessed.append(letter)
        score=score+10

        l.config(text=f"\ncorrect,guessed letters{guessed}\n",bg='#FEE227',font='Arial')
        m.config(text=f"\nscore:{score} \n",bg='#FEE227',font='Arial')

        j=j+1
        if(j==len(word)):
            l.config(text=f"\nYay u guessed-{word}!, close tkinter\n",bg='#FEE227',font='Arial')
            return

    else:
        l.config(text="\nwrong\n",bg='#FEE227',font='Arial')
        i=i+1
        if(i==1):
            c.create_line(200,100,200,150,fill='#FEE227')
        elif(i==2):
            c.create_oval(175,150,225,175,outline='#FEE227')
        elif(i==3):
            c.create_line(200,175,200,225,fill='#FEE227')
        elif(i==4):
            c.create_line(200,225,175,250,fill='#FEE227')
        elif(i==5):
            c.create_line(200,225,225,250,fill='#FEE227')
        elif(i==6):
            c.create_line(200,175,175,200,fill='#FEE227')
        elif(i==7):
            c.create_line(200,175,225,200,fill='#FEE227')
     


    e.delete(0,END)
 
e.bind('<Return>',func)
 


    
c.place(relx=0.5, rely=0.3, anchor=N)

r.mainloop()

