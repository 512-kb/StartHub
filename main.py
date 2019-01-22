from tkinter import *
import tkinter.messagebox as msg
class portal():
    def __init__(self):
        self.labelfont = ('times', 20 , 'bold')

    #first screen
    def first_screen(self):
        self.first = Tk()
        #configure first screen
        self.first.title("StartHub")
        self.first.geometry("300x300")
        #frame
        self.fhead = Frame(self.first)
        self.bhead = Frame(self.first)
        #heading
        self.head = Label(self.fhead, text = "Welcome to StartHub")
        self.head.configure(font = self.labelfont)
        self.head.grid(row=50, column=400)

        #buttons
        self.copB1 = Button(self.bhead,text = "Corporate SignIn", command = lambda : self.SignIn('c'))
        self.copB1.pack()

        self.copB2 = Button(self.bhead,text = "Corporate SignUp", command = lambda : self.SignUp('c',self.first))
        self.copB2.pack()

        self.inoB1 = Button(self.bhead,text = "Innovator SignIn", command = lambda : self.SignIn('a'))
        self.inoB1.pack()

        self.inoB2 = Button(self.bhead,text = "Innovator SignUp", command = lambda : self.SignUp('a',self.first))
        self.inoB2.pack()

        self.fhead.pack()
        self.bhead.pack()
        self.first.mainloop()


    #Sign in
    def SignIn(self, f):
        self.signin = Tk()
        self.signin.geometry("430x90")
        self.signin.title("Sign In")
        #label
        self.l1 = Label(self.signin, text = "Username")
        self.l2 = Label(self.signin, text = "Password")
        #Entry
        self.e1 = Entry(self.signin)
        self.e2 = Entry(self.signin)
        #button
        self.loginb = Button(self.signin, text="Login", command = lambda : self.check(f))
        #pack
        self.l1.grid(row=0)
        self.e1.grid(row=0, column=1, ipadx = 20)
        self.l2.grid(row=1)
        self.e2.grid(row=1,column=1, ipadx=20)
        self.loginb.grid(row=2,column=1, ipady=4, ipadx=10)
        self.signin.mainloop()

    #sign up
    def SignUp(self, f, r):
        self.signup = Tk()
        self.signup.geometry("450x90")
        self.signup.title("Sign Up")
        #label
        self.l1 = Label(self.signup, text = "Userame")
        self.l2 = Label(self.signup, text = "Password")
        self.l3 = Label(self.signup, text = "Email")

        #Entry
        self.e1 = Entry(self.signup)
        self.e2 = Entry(self.signup)
        self.e3 = Entry(self.signup)
        #button
        self.up = Button(self.signup, text="SignUp", command = lambda: self.commit(self.signup,f))
        #pack
        self.l1.grid(row=0)
        self.e1.grid(row=0, column=1, ipadx = 20)
        self.l2.grid(row=1)
        self.e2.grid(row=1,column=1, ipadx=20)
        self.l3.grid(row=2)
        self.e3.grid(row=2,column=1, ipadx=20)
        self.up.grid(row=3,column=1, ipady=4, ipadx=10)

        self.signup.mainloop()

    def commit(self,root,flag):
        if flag == 'c':
            self.f1 = open("cdata.txt", "a")
        else:
            self.f1 = open("idata.txt", "a")
        if self.e1.get() and self.e2.get() and self.e3.get():
            self.f1.write(self.e1.get() + " " + self.e2.get() + " " + self.e3.get() + "\n")
            msg.showinfo("Success","DataBase Updated")
            self.f1.close()
            root.destroy()

        else:
            msg.showwarning("Warning","Text Field(s) empty")

    #for sign in
    def check(self,f):
        if f == 'c':
            self.f = open("cdata.txt","r")
        else:
            self.f = open("idata.txt","r")
        if self.e1.get() and self.e2.get():
            self.name = self.e1.get()
            self.password = self.e2.get()
            self.fg = 0
            self.str = ""
            for self.x in self.f:
                self.str = self.x.split()
                if self.name in self.str[0] and self.password in self.str[1]:
                    self.fg = 1
                    break
            self.f.close()
            if self.fg == 1:
                self.signin.destroy()
                self.first.destroy()
                if f == 'c':
                    self.Chome()
                else:
                    self.Ihome()
            else:
                msg.showwarning("Incorrect","Wrong Username or Password")
        else:
            msg.showwarning("Error","Text Field(s) empty")


    #Innovator home
    def Ihome(self):
        self.imains = Tk()
        self.imains.geometry("200x200")
        #label
        self.line1 = Label(self.imains, text="Hi " + self.str[0] + "!")
        self.line1.configure(font=('times','15','bold'))
        self.line1.grid(row=0)
        #button
        self.b1 = Button(self.imains,text="ShareYouIdea", command=lambda : self.shareyouridea(self.imains))
        self.b1.grid(row=1)
        self.b3 = Button(self.imains,text="View Problems", command= lambda: self.viewproblems())
        self.b3.grid(row=1, column=100)

        #creating Menu
        self.m = Menu(self.imains)
        self.imains.config(menu=self.m)
        self.s1 = Menu(self.m)
        self.m.add_cascade(label="Options", menu=self.s1)
        self.s1.add_command(label="Logout" , command= lambda: self.reset(self.imains))
        self.s1.add_separator()
        self.s1.add_command(label='Quit', command= lambda: self.Quit(self.imains))

        self.imains.loop()

    #Innovator
    def shareyouridea(self,imain):
        #main window
        self.ihome = Tk()
        self.ihome.geometry("600x500")
        self.ihome.title("Innovator Idea")

        #label
        self.line = Label(self.ihome, text="Hi " + self.str[0] + "! Share your Idea below")
        self.line.configure(font=('times','15','bold'))
        self.line.grid(row=0)

        #button
        self.topicname = Label(self.ihome, text="What your idea is About?")
        self.topicname.grid(row=1)
        self.topic = Entry(self.ihome)
        self.topic.grid(row=2)
        #frame
        self.tframe = Frame(self.ihome)
        #text Field
        self.T = Text(self.tframe, height=20, width=60)
        self.S = Scrollbar(self.tframe)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        self.T.pack()
        self.tframe.grid(row=3)

        #submit button
        self.submit = Button(self.tframe, text="Submit", command= lambda: self.done(imain,self.ihome))
        self.submit.pack()

        #creating Menu
        self.m = Menu(self.ihome)
        self.ihome.config(menu=self.m)
        self.s1 = Menu(self.m)
        self.m.add_cascade(label="Options", menu=self.s1)
        self.s1.add_command(label="Logout" , command= lambda: self.reset(self.ihome))
        self.s1.add_separator()
        self.s1.add_command(label='Quit', command= lambda: self.Quit(self.ihome))



        self.ihome.mainloop()

    #submition done

    def done(self,root,root1):
        if self.topic.get() and self.T.get("1.0",END):
            self.tname = self.topic.get()
            self.input = self.T.get("1.0",END)
            #topic file
            self.ff = open(""+self.tname+".txt", "a")
            self.ff.write(self.input + "\n")
            self.ff.close()
            #idea DataBase
            self.fff = open("ideas.txt","a")
            self.fff.write(self.str[0] + " " + self.tname + ".txt\n")
            self.fff.close()
            msg.showinfo("Success", "Your idea is successfully recorded")
            root.destroy()
            root1.destroy()
            self.Ihome()
        else:
            msg.showwarning("Error","Text field(s) empty")

    def viewproblems(self):
        self.vf = Tk()
        self.vf.title("List Of Problems")
        self.vff = open("problems.txt","r")
        self.z = ""
        self.k = 0
        for self.i in self.vff:
            self.z = self.i.split()
            self.vb = Button(self.vf,text=self.z[1], command=lambda zz=self.z[1]: self.showfile(zz))
            self.vb.grid(row=self.k)
            self.vl = Label(self.vf,text="given by " + self.z[0])
            self.vl.grid(row=self.k, column=1)
            self.k += 1


        self.vf.mainloop()


    def showfile(self,nn):
        self.show = Tk()
        self.sf = open(nn,"r")
        for self.i in self.sf:
            self.showl = Label(self.show, text=self.i)
            self.showl.pack()
        self.sf.close()
        self.show.mainloop()



    #corporate home
    def Chome(self):
        #main window
        self.chome = Tk()
        self.chome.geometry("250x150")
        self.chome.title("Corporator Home")
        #button
        self.shareproblem = Button(self.chome, text="Share Your Problem", command= lambda : self.shareyourproblem(self.chome))
        self.viewall = Button(self.chome, text="Available Ideas", command = lambda: self.viewproblemsc())
        self.shareproblem.grid(row=1)
        self.viewall.grid(row=1, column =100)

        #creating Menu
        self.m = Menu(self.chome)
        self.chome.config(menu=self.m)
        self.s1 = Menu(self.m)
        self.m.add_cascade(label="Options", menu=self.s1)
        self.s1.add_command(label="Logout" , command= lambda: self.reset(self.chome))
        self.s1.add_separator()
        self.s1.add_command(label='Quit', command= lambda: self.Quit(self.chome))

        self.chome.mainloop()

    def showfilec(self,nn):
        self.show = Tk()
        self.sf = open(nn,"r")
        for self.i in self.sf:
            self.showl = Label(self.show, text=self.i)
            self.showl.pack()
        self.sf.close()
        self.show.mainloop()

    def viewproblemsc(self):
        self.vf = Tk()
        self.vf.title("List Of Ideas")
        self.vff = open("ideas.txt","r")
        self.z = ""
        self.k = 0
        for self.i in self.vff:
            self.z = self.i.split()
            self.vb = Button(self.vf,text=self.z[1], command=lambda zz=self.z[1]: self.showfilec(zz))
            self.vb.grid(row=self.k)
            self.vl = Label(self.vf,text=" idea proposed by " + self.z[0])
            self.vl.grid(row=self.k, column=1)
            self.k += 1


        self.vf.mainloop()


    def shareyourproblem(self,root):
        #main window
        self.ihome = Tk()
        self.ihome.geometry("600x500")
        self.ihome.title("Corporator Problem")

        #label
        self.line = Label(self.ihome, text="Hi " + self.str[0] + "! Tell your Problem")
        self.line.configure(font=('times','15','bold'))
        self.line.grid(row=0)

        #button
        self.topicname = Label(self.ihome, text="What your problem is About?")
        self.topicname.grid(row=1)
        self.topic = Entry(self.ihome)
        self.topic.grid(row=2)
        #frame
        self.tframe = Frame(self.ihome)
        #text Field
        self.T = Text(self.tframe, height=20, width=60)
        self.S = Scrollbar(self.tframe)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        self.T.pack()
        self.tframe.grid(row=3)

        #submit button
        self.submit = Button(self.tframe, text="Submit", command= lambda: self.Cdone(root,self.ihome))
        self.submit.pack()

        #creating Menu
        self.m = Menu(self.ihome)
        self.ihome.config(menu=self.m)
        self.s1 = Menu(self.m)
        self.m.add_cascade(label="Options", menu=self.s1)
        self.s1.add_command(label="Logout" , command= lambda: self.reset(self.ihome))
        self.s1.add_separator()
        self.s1.add_command(label='Quit', command= lambda: self.Quit(self.ihome))

        self.ihome.mainloop()

        #for Corporator
    def Cdone(self,root,root1):
        if self.topic.get() and self.T.get("1.0",END):
            self.tname = self.topic.get()
            self.input = self.T.get("1.0",END)
            #topic file
            self.ff = open(""+self.tname+".txt", "a")
            self.ff.write(self.input + "\n")
            self.ff.close()
            #idea DataBase
            self.fff = open("problems.txt","a")
            self.fff.write(self.str[0] + " " + self.tname + ".txt\n")
            self.fff.close()
            msg.showinfo("Success", "Your problem is successfully recorded")
            root.destroy()
            root1.destroy()
            self.Ihome()
        else:
            msg.showwarning("Error","Text field(s) empty")










    #funtion used to quit the portal
    def Quit(self,root):
        #creating a question
        n = msg.askquestion("Quit","Do you really want to Quit!")
        if n == 'yes':
            root.destroy()


    #used to logout
    def reset(self,root):
        root.destroy()
        self.first_screen()



if __name__ == '__main__':
    p = portal()
    p.first_screen()
