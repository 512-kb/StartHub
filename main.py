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
        self.first.geometry("1080x780")
        #adding background image
        self.img = PhotoImage(file="images/bg.gif")
        self.background = Label(self.first,image=self.img)
        self.background.place(x=0,y=0)
        
        #description label
        self.des = "A problem sharing portal that connects corporator to innovator and vise versa\n to exchange problems and to get their solutions"
        self.description = Label(self.first,text=self.des)
        self.description.config(font=self.labelfont)
        self.description.place(x=50,y=250)
        
        #other lables
        self.corp = Label(self.first,text="Corporator Section")
        self.inno = Label(self.first,text="Innovator Section")
        self.corp.place(x=40,y=350)
        self.corp.config(font=('times',20,'bold'))
        self.inno.place(x=750,y=350)
        self.inno.config(font=('times',20,'bold'))
        #buttons
        self.copB1 = Button(self.first,text = "Corporator SignIn", command = lambda : self.SignIn('c',self.first))
        self.copB1.config(font=('times',13,'bold'))
        self.copB1.place(x=80,y=400)

        self.copB2 = Button(self.first,text = "Corporator SignUp", command = lambda : self.SignUp('c',self.first))
        self.copB2.place(x=80,y=450)
        self.copB2.config(font=('times',13,'bold'))

        self.inoB1 = Button(self.first,text = "Innovator SignIn", command = lambda : self.SignIn('a',self.first))
        self.inoB1.place(x=790,y=400)
        self.inoB1.config(font=('times',13,'bold'))

        self.inoB2 = Button(self.first,text = "Innovator SignUp", command = lambda : self.SignUp('a',self.first))
        self.inoB2.place(x=790,y=450)
        self.inoB2.config(font=('times',13,'bold'))

        self.first.mainloop()


    #Sign in
    def SignIn(self, f,root):
        root.destroy()
        self.signin = Tk()
        self.signin.geometry("762x380")
        self.signin.title("Sign In")
        #adding background image
        self.img = PhotoImage(file="images/starthub.gif")
        self.imglabel = Label(self.signin, image=self.img)
        self.imglabel.place(x=0,y=0)
        #label
        self.l1 = Label(self.signin, text = "Username")
        self.l2 = Label(self.signin, text = "Password")
        self.l1.config(font=('times',20,'bold'))
        self.l2.config(font=('times',20,'bold'))
        #Entry
        self.e1 = Entry(self.signin)
        self.e2 = Entry(self.signin)
        #button
        self.loginb = Button(self.signin, text="Login", command = lambda : self.check(f))
        self.loginb.config(font=('times',15,'bold'))
        self.back = Button(self.signin, text="GoBack", command = lambda : self.go_back('f',self.signin))
        self.back.config(font=('times',15,'bold'))
        #Entry)
        #pack
        self.l1.grid(row=0)
        self.e1.grid(row=0, column=1, ipadx = 20)
        self.l2.grid(row=1)
        self.e2.grid(row=1,column=1, ipadx=20)
        self.loginb.grid(row=2,column=1, ipady=4, ipadx=10)
        self.back.grid(row=2,column=3,ipady=4, ipadx=10)
        self.signin.mainloop()

    def go_back(self,flag,root):
        if flag == 'f':
            root.destroy()
            self.first_screen()
        elif flag == 'i':
            root.destroy()
            self.Ihome()
        elif flag == 'c':
            root.destroy()
            self.Chome()
    
    #sign up
    def SignUp(self, f, r):
        r.destroy()
        self.signup = Tk()
        self.signup.geometry("762x380")
        self.signup.title("Sign Up")
        #adding background image
        self.img = PhotoImage(file="images/starthub.gif")
        self.imglabel = Label(self.signup, image=self.img)
        self.imglabel.place(x=0,y=0)
        #label
        self.l1 = Label(self.signup, text = "Userame")
        self.l2 = Label(self.signup, text = "Password")
        self.l3 = Label(self.signup, text = "Email")
        self.l1.config(font=('times',20,'bold'))
        self.l2.config(font=('times',20,'bold'))
        self.l3.config(font=('times',20,'bold'))
        #Entry
        self.e1 = Entry(self.signup)
        self.e2 = Entry(self.signup)
        self.e3 = Entry(self.signup)
        #button
        self.up = Button(self.signup, text="SignUp", command = lambda: self.commit(self.signup,f))
        self.up.config(font=('times',15,'bold'))
        self.back = Button(self.signup, text="GoBack", command = lambda : self.go_back('f',self.signup))
        self.back.config(font=('times',15,'bold'))
        #pack
        self.l1.grid(row=0)
        self.e1.grid(row=0, column=1, ipadx = 20)
        self.l2.grid(row=1)
        self.e2.grid(row=1,column=1, ipadx=20)
        self.l3.grid(row=2)
        self.e3.grid(row=2,column=1, ipadx=20)
        self.up.grid(row=3,column=1, ipady=4, ipadx=10)
        self.back.grid(row=3,column=3, ipady=4, ipadx=10)

        self.signup.mainloop()

    def commit(self,root,flag):
        if flag == 'c':
            self.f1 = open("data/c_login/cdata.txt", "a")
        else:
            self.f1 = open("data/i_login/idata.txt", "a")
        if self.e1.get() and self.e2.get() and self.e3.get():
            self.f1.write(self.e1.get() + " " + self.e2.get() + " " + self.e3.get() + "\n")
            msg.showinfo("Success","DataBase Updated")
            self.f1.close()
            root.destroy()
            self.first_screen()
        else:
            msg.showwarning("Warning","Text Field(s) empty")

    #for sign in
    def check(self,f):
        if f == 'c':
            self.f = open("data/c_login/cdata.txt","r")
        else:
            self.f = open("data/i_login/idata.txt","r")
        if self.e1.get() and self.e2.get():
            self.name = self.e1.get()
            self.password = self.e2.get()
            self.fg = 0
            self.str = ""
            for self.x in self.f:
                self.fg = 0
                self.str = self.x.split()
                if self.name == self.str[0] and self.password == self.str[1]:
                    self.fg = 1
                    break
            self.f.close()
            if self.fg == 1:
                self.signin.destroy()
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
        self.imains.geometry("965x682")
        #adding background image
        self.img = PhotoImage(file="images/bg2.gif")
        self.imglabel = Label(self.imains, image=self.img)
        self.imglabel.place(x=0,y=0)
        #label
        self.line1 = Label(self.imains, text="Hi " + self.str[0]+ "!")
        self.line1.configure(font=('times','15','bold'))
        self.line1.place(x=70,y=30)
        #welcome line
        self.stt = "Here You Can Share your problem or can view Innovator's solutions"
        self.line = Label(self.imains, text=self.stt)
        self.line.configure(font=('times','15','bold'))
        self.line.place(x=70,y=80)
        #button
        self.b1 = Button(self.imains,text="ShareYouIdea", command=lambda : self.shareyouridea(self.imains))
        self.b1.config(font=('times','15','bold'))
        self.b1.place(x=150,y=150)
        self.b3 = Button(self.imains,text="View Problems", command= lambda: self.viewproblems())
        self.b3.config(font=('times','15','bold'))
        self.b3.place(x=400,y=150)

        #creating Menu
        self.m = Menu(self.imains)
        self.imains.config(menu=self.m)
        self.s1 = Menu(self.m)
        self.m.add_cascade(label="Options", menu=self.s1)
        self.s1.add_command(label="Logout" , command= lambda: self.reset(self.imains))
        self.s1.add_separator()
        self.s1.add_command(label='Quit', command= lambda: self.Quit(self.imains))

        self.imains.mainloop()

    #Innovator
    def shareyouridea(self,imain):
        imain.destroy()
        #main window
        self.ihome = Tk()
        self.ihome.geometry("965x682")
        self.ihome.title("Innovator Idea")
        #adding background image
        self.img = PhotoImage(file="images/bg2.gif")
        self.imglabel = Label(self.ihome, image=self.img)
        self.imglabel.place(x=0,y=0)
        #label
        self.line = Label(self.ihome, text="Hi " + self.str[0] + "! Share your Idea below")
        self.line.configure(font=('times','20','bold'))
        self.line.place(x=100,y=10)

        #button
        self.topicname = Label(self.ihome, text="What your idea is About?")
        self.topicname.config(font=('times',15))
        self.topicname.place(x=100,y=80)
        self.topic = Entry(self.ihome)
        self.topic.place(x=320,y=80)
        self.back = Button(self.ihome, text="GoBack", command = lambda : self.go_back('i',self.ihome))
        self.back.config(font=('times',15))
        self.back.place(x=650,y=230)

        #text Field
        self.T = Text(self.ihome, height=20, width=60)
        self.S = Scrollbar(self.ihome)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        self.T.place(x=80,y=120)

        #submit button
        self.submit = Button(self.ihome, text="Submit", command= lambda: self.done(self.ihome))
        self.submit.config(font=('times',15))
        self.submit.place(x=650,y=170)

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

    def done(self,root):
        if self.topic.get() and self.T.get("1.0",END):
            self.tname = self.topic.get()
            self.input = self.T.get("1.0",END)
            #topic file
            self.ff = open("data/i_topic/"+self.tname+".txt", "a")
            self.ff.write(self.input + "\n")
            self.ff.close()
            #idea DataBase
            self.fff = open("data/i_idea/ideas.txt","a")
            self.fff.write(self.str[0] + " " + self.tname + ".txt\n")
            self.fff.close()
            msg.showinfo("Success", "Your idea is successfully recorded")
            root.destroy()
            self.Ihome()
        else:
            msg.showwarning("Error","Text field(s) empty")

    def viewproblems(self):
        self.vf = Tk()
        self.vf.title("List Of Problems")
        self.vff = open("data/c_problem/problems.txt","r")
        self.z = ""
        self.k = 0
        for self.i in self.vff:
            self.z = self.i.split()
            self.vb = Button(self.vf,text=self.z[1], command=lambda zz=self.z[1]: self.showfile(zz))
            self.vb.config(font=('times','15'))
            self.vb.grid(row=self.k)
            self.vl = Label(self.vf,text="given by " + self.z[0])
            self.vl.config(font=('times','15'))
            self.vl.grid(row=self.k, column=1)
            self.k += 1


        self.vf.mainloop()


    def showfile(self,nn):
        self.show = Tk()
        self.sf = open("data/c_topic/"+nn,"r")
        for self.i in self.sf:
            self.showl = Label(self.show, text=self.i)
            self.showl.config(font=('times',20,'bold'))
            self.showl.pack()
        self.sf.close()
        self.show.mainloop()



    #corporate home
    def Chome(self):
        #main window
        self.chome = Tk()
        self.chome.geometry("965x682")
        self.chome.title("Corporator Home")
        #adding background image
        self.img = PhotoImage(file="images/bg2.gif")
        self.imglabel = Label(self.chome, image=self.img)
        self.imglabel.place(x=0,y=0)
        #line
        self.line1 = Label(self.chome, text="Hi " + self.str[0] +"!")
        self.line1.configure(font=('times','20','bold'))
        self.line1.place(x=70,y=30)
        #welcome line
        self.stt = "Here You Can Share your ideas or can view Corporator's problem"
        self.line = Label(self.chome, text=self.stt)
        self.line.configure(font=('times','15','bold'))
        self.line.place(x=70,y=80)
        #button
        self.shareproblem = Button(self.chome, text="Share Your Problem", command= lambda : self.shareyourproblem(self.chome))
        self.shareproblem.config(font=('times','15','bold'))
        self.viewall = Button(self.chome, text="Available Ideas", command = lambda: self.viewproblemsc())
        self.viewall.config(font=('times','15','bold'))
        self.shareproblem.place(x=150,y=150)
        self.viewall.place(x=400,y=150)

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
        self.sf = open("data/i_topic/"+nn,"r")
        for self.i in self.sf:
            self.showl = Label(self.show, text=self.i)
            self.showl.config(font=('times',20,'bold'))
            self.showl.pack()
        self.sf.close()
        self.show.mainloop()

    def viewproblemsc(self):
        self.vf = Tk()
        self.vf.title("List Of Ideas")
        self.vff = open("data/i_idea/ideas.txt","r")
        self.z = ""
        self.k = 0
        for self.i in self.vff:
            self.z = self.i.split()
            self.vb = Button(self.vf,text=self.z[1], command=lambda zz=self.z[1]: self.showfilec(zz))
            self.vb.grid(row=self.k)
            self.vb.config(font=('times','15'))
            self.vl = Label(self.vf,text=" idea proposed by " + self.z[0])
            self.vl.config(font=('times','15'))
            self.vl.grid(row=self.k, column=1)
            self.k += 1


        self.vf.mainloop()


    def shareyourproblem(self,root):
        root.destroy()
        #main window
        self.ihome = Tk()
        self.ihome.geometry("965x682")
        self.ihome.title("Corporator Problem")
        #adding background image
        self.img = PhotoImage(file="images/bg2.gif")
        self.imglabel = Label(self.ihome, image=self.img)
        self.imglabel.place(x=0,y=0)
        #label
        self.line = Label(self.ihome, text="Hi " + self.str[0] + "! Tell your Problem")
        self.line.configure(font=('times','15','bold'))
        self.line.place(x=100,y=10)

        #button
        self.topicname = Label(self.ihome, text="What your problem is About?")
        self.topicname.config(font=('times',15))
        self.topicname.place(x=100,y=80)
        self.topic = Entry(self.ihome)
        self.topic.place(x=350,y=80)
        
        #text Field
        self.T = Text(self.ihome, height=20, width=60)
        self.S = Scrollbar(self.ihome)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        self.T.pack()
        self.T.place(x=80,y=120)

        #submit button
        self.submit = Button(self.ihome, text="Submit", command= lambda: self.Cdone(self.ihome))
        self.submit.config(font=('times',15))
        self.submit.place(x=650,y=170)
        self.back = Button(self.ihome, text="GoBack", command = lambda : self.go_back('c',self.ihome))
        self.back.config(font=('times',15))
        self.back.place(x=650,y=230)

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
    def Cdone(self,root):
        if self.topic.get() and self.T.get("1.0",END):
            self.tname = self.topic.get()
            self.input = self.T.get("1.0",END)
            #topic file
            self.ff = open("data/c_topic/"+self.tname+".txt", "a")
            self.ff.write(self.input + "\n")
            self.ff.close()
            #idea DataBase
            self.fff = open("data/c_problem/problems.txt","a")
            self.fff.write(self.str[0] + " " + self.tname + ".txt\n")
            self.fff.close()
            msg.showinfo("Success", "Your problem is successfully recorded")
            root.destroy()
            self.Chome()
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