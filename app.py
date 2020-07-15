from tkinter import *
from dbhelper import DBhelper
from tkinter import messagebox
import random



class Login:

    def __init__(self):
        self.db=DBhelper()

        self.root = Tk()

        self.root.title("My Quiz App")

        self.root.configure(background="#00FF00")

        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)

        self.start_gui()





    def start_gui(self):
        self.clear()

        self.label = Label(self.root, text="Quiz Game", bg="#00FF00")
        self.label.configure(font=("Times", 30, "bold"))
        self.label.pack(pady=(10, 10))

        self.label1 = Label(self.root, text="Email: ", bg="#00FF00")
        self.label1.configure(font=("Times", 15, "italic"))
        self.label1.pack(pady=(5, 5))

        self.email = Entry(self.root)
        self.email.pack(pady=(0, 10),ipadx=30,ipady=5)

        self.label2 = Label(self.root, text="Password: ",fg="black", bg="#00FF00")
        self.label2.configure(font=("Times", 15, "italic"))
        self.label2.pack(pady=(5, 5))

        self.password = Entry(self.root,show="*")
        self.password.pack(pady=(0, 10), ipadx=30, ipady=5)

        self.login = Button(self.root, text="Login", bg="#FFFF00", fg="#000",command=lambda: self.btn_click())
        self.login.pack(pady=(5, 10))

        self.label4 = Label(self.root, text="Not a member? Sign up", fg="black", bg="#00FF00")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(pady=(5, 5))

        self.register = Button(self.root, text="Sign Up", bg="#FFFF00", fg="#000", command=lambda: self.register_gui())
        self.register.pack(pady=(5, 10), ipadx=40, ipady=2)

        self.root.mainloop()

    def register_gui(self):
        self.clear()

        self.label0 = Label(self.root, text="Quiz Game", bg="#00FF00")
        self.label0.configure(font=("Times", 30, "bold"))
        self.label0.pack(pady=(10, 10))

        self.label1 = Label(self.root, text="Name: ", bg="#00FF00")
        self.label1.configure(font=("Times", 15, "italic"))
        self.label1.pack(pady=(5, 5))

        self.name = Entry(self.root)
        self.name.pack(pady=(0, 10), ipadx=30, ipady=5)

        self.label2 = Label(self.root, text="Email: ", fg="black", bg="#00FF00")
        self.label2.configure(font=("Times", 15, "italic"))
        self.label2.pack(pady=(5, 5))

        self.email = Entry(self.root)
        self.email.pack(pady=(0, 10), ipadx=30, ipady=5)


        self.label3 = Label(self.root, text="Password: ", fg="black", bg="#00FF00")
        self.label3.configure(font=("Times", 15, "italic"))
        self.label3.pack(pady=(5, 5))

        self.password = Entry(self.root,show="*")
        self.password.pack(pady=(0, 10), ipadx=30, ipady=5)

        self.label4 = Label(self.root, text="Gender: ", fg="black", bg="#00FF00")
        self.label4.configure(font=("Times", 15, "italic"))
        self.label4.pack(pady=(5, 5))

        self.gender = Entry(self.root)
        self.gender.pack(pady=(0, 10), ipadx=30, ipady=5)



        self.login = Button(self.root, text="Sign Up", bg="#FFFF00", fg="#000", command=lambda: self.reg_submit())
        self.login.pack(pady=(5, 10))

        self.label5 = Label(self.root, text="Not a member? Sign up", fg="black", bg="#00FF00")
        self.label5.configure(font=("Times", 15, "italic"))
        self.label5.pack(pady=(5, 5))

        self.register = Button(self.root, text="Login", bg="#FFFF00", fg="#000", command=lambda: self.start_gui())
        self.register.pack(pady=(5, 10), ipadx=40, ipady=2)



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def btn_click(self):
        email=self.email.get()
        password = self.password.get()
        #print(self.email.get())
        data=self.db.check_login(email,password)
        print(data)

        if len(data) > 0:
            # Login sahi hai
            self.clear()
            self.user_id = data[0][0]
            self.user_data = data[0]
            self.load_user_info()
        else:
            messagebox.showerror("Error", "Incorrect Email/Password")


    def load_user_info(self):
        self.main_window(self.user_data)

    def logout(self):
        self.user_id = ''
        self.user_data=''

        self.start_gui()



    def calc(self):
        global indexes, user_answer, correct_answers
        x = 0
        score = 0
        for i in indexes:
            if user_answer[x] == correct_answers[i]:
                score = score + 10
            x += 1
        print(score)
        self.showresult(str(score))

    global indexes #shuffling
    indexes = []

    def gen(self):
        # global indexes
        while (len(indexes) < 10):
            # print(len(indexes))
            x = random.randint(0, 9)
            if x in indexes:
                continue
            else:
                indexes.append(x)
                # print(indexes)

    global user_answer
    user_answer = []

    global ques, qno
    ques = 1
    qno = 1






    def selected(self):
        global radiovar, user_answer, label1
        global labelQuestion, r1, r2, r3, r4
        global ques, qno
        x = radiovar.get()
        # print(x)
        user_answer.append(x)
        radiovar.set(-1)
        if ques < 10:
            # print(ques)
            # self.root.after(1000)
            label1.configure(text=question_number[qno])
            labelQuestion.configure(text=questions[indexes[ques]])
            r1['text'] = answers_choice[indexes[ques]][0]
            r2['text'] = answers_choice[indexes[ques]][1]
            r3['text'] = answers_choice[indexes[ques]][2]
            r4['text'] = answers_choice[indexes[ques]][3]
            ques += 1
            qno += 1
            # print(ques)
        else:
            # print(indexes)
            # print(user_answer)
            self.calc()


    def ALGO_question1(self):
        global questions
        questions = [
            "(A) Any node is the path from the root to the node is called:",
            "(B) Which of the following is not the type of queue ?",
            "(C) A graph is a collection of nodes,called.......And line segments called arcs or.......that connect pair of nodes ",
            "(D) In......, search start at the beginning of the list and check every element in the list.",
            "(E) in the......traversal we process all of a vertex's descendants before we move to an adjacent vertex.",
            "(F) Python scripts (files) have names that end with",
            "(G) What is the proper way to say 'good-bye' to Python ?",
            "(H) A USB memory stick is an example of which of the following components of computer architecture ?",
            "(I) What is the best way to think about a 'Syntax Error' while programming ?",
            "(J) Which of the following variables is the 'most mnemonic' ?",
        ]
        global answers_choice
        answers_choice = [
            ["a. Ancestor node", "b. Successor node", "c. Internal node", "d. None of the above"],
            ["a. Priority queue", "b. Circular queue", "c. Single ended queue", "d. Ordinary queue"],
            ["a. vertices,paths", "b. vertices,edges", "c. graph node,edges", "d. edges,vertices"],
            ["a. Binary search", "b. Hash search", "c. Linear search", "d. Binary Tree search"],
            ["a. Depth Limited", "b. With First", "c. Breadth First", "d. Depth First"],
            ["a. .py", "b. .png", "c. .doc", "d. .exe"],
            ["a. while", "b. // stop", "c. quit()", "d. #EXIT"],
            ["a. Secondary Memory", "b. Central Processing Unit", "c. Output Device", "d. Main Memory"],
            ["a. The computer did not understand the statement that you entered", "b. You will never learn how to program", "c. It is the wrong time of day - wait a few hours and try again", "d. The computer needs to have its software upgraded"],
            ["a. variable_173", "b. x", "c. hours", "d. x1q3z9ocd"]
        ]
        global correct_answers
        correct_answers = [0, 2, 1, 2, 3, 0, 2, 0, 0, 2]

        global question_number
        question_number = [
            "QUESTION NO.1",
            "QUESTION NO.2",
            "QUESTION NO.3",
            "QUESTION NO.4",
            "QUESTION NO.5",
            "QUESTION NO.6",
            "QUESTION NO.7",
            "QUESTION NO.8",
            "QUESTION NO.9",
            "QUESTION NO.10",
        ]

        self.gen()
        self.clear()

        global labelQuestion, r1, r2, r3, r4, label1

        label1 = Label(self.root,text=question_number[0],fg="red",bg="#00FF00")

        label1.configure(font=("Times", 30, "bold italic"))
        label1.pack(pady=(10, 10))

        labelQuestion = Label(
            self.root,
            text=questions[indexes[0]],
            width=500,
            justify="center",
            wraplength=400,
            fg="black",
            bg="#00FF00"
        )

        labelQuestion.configure(font=("Times", 15, "bold italic"))
        labelQuestion.pack(pady=(10, 10))

        global radiovar
        radiovar = IntVar()
        radiovar.set(-1)

        r1 = Radiobutton(
            self.root,
            text=answers_choice[indexes[0]][0],
            font=("Times", 12),
            bg="yellow",
            value=0,
            variable=radiovar,
            command=lambda: self.selected(),
        )
        r1.pack(pady=5)

        r2 = Radiobutton(
            self.root,
            text=answers_choice[indexes[0]][1],
            font=("Times", 12),
            bg="yellow",
            value=1,
            variable=radiovar,
            command=lambda: self.selected(),
        )
        r2.pack(pady=5)

        r3 = Radiobutton(
            self.root,
            text=answers_choice[indexes[0]][2],
            font=("Times", 12),
            bg="yellow",
            value=2,
            variable=radiovar,
            command=lambda: self.selected(),
        )
        r3.pack(pady=5)

        r4 = Radiobutton(
            self.root,
            text=answers_choice[indexes[0]][3],
            font=("Times", 12),
            bg="yellow",
            value=3,
            variable=radiovar,
            command=lambda: self.selected(),
        )
        r4.pack(pady=5)

    def showresult(self, score):
        label1.destroy()
        labelQuestion.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        labelresulttext = Label(self.root,justify="center",fg="red",bg="#00FF00")
        labelresulttext.configure(font=("Times", 30, "bold italic"), text="Your score is " + score)
        labelresulttext.pack(pady=(40, 30), ipadx=10, ipady=5)

        self.select = Button(self.root, text="Logout", fg="black", bg="yellow",command=lambda: self.logout())
        self.select.pack(pady=(5, 10), ipadx=10, ipady=2)


    def main_window(self, data, mode=1, index=None):
        print(data)
        self.clear()

        self.label1 = Label(self.root, text="Name: " + data[1], fg="black", bg="#00FF00")
        self.label1.configure(font=("Times", 25, "bold"))
        self.label1.pack(pady=(10, 10))

        if len(data[2]) != 0:
            self.label2 = Label(self.root, text="Email: " + data[2], fg="black", bg="#00FF00")
            self.label2.configure(font=("Times", 25, "bold"))
            self.label2.pack(pady=(10, 10))

        if len(data[4]) != 0:
            self.label2 = Label(self.root, text ="Gender: " + data[4], fg="black", bg="#00FF00")

            self.label2.configure(font=("Times", 25, "bold"))
            self.label2.pack(pady=(10, 10))

        self.select = Button(self.root, text="Start Your Quiz", fg="black", bg="yellow",command=lambda : self.ALGO_question1())
        self.select.pack(pady=(5, 10), ipadx=10, ipady=2)


        if mode == 2:
            frame = Frame(self.root)
            frame.pack()

            if index != 0:
                previous = Button(frame, text="Start")
                previous.pack(side='left')




    def reg_submit(self):

        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        gender = self.gender.get()
        resposnse = self.db.insert_user(name, email, password, gender)

        if resposnse == 1:
            messagebox.showinfo("Registration Successful", "You may login now!")
        else:
            messagebox.showerror("Error", "Database Error")


obj=Login()