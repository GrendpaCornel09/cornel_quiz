import tkinter as tk
from tkinter import *
from tkinter import ttk,PhotoImage
from tkinter.messagebox import showwarning,showinfo
import re

print('========== CORNEL QUIZ ==========')
print('               v0.1              ')
print('Refer to this console to see the ')
print('            app\'s log           ')
print('')

TITLE_FONT=('Segoe UI Bold', 40)
SUBTITLE_FONT=('Segoe UI Semibold',30)
REGULAR_FONT=('Segoe UI', 15)

class tkinterApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title('Cornel Quiz v0.1')
        
        # container
        container=tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames={}
        
        for F in (main_page, default_landing, default_quiz, make_a_quiz, custom_quiz_list):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky='nsew')
        
        if len(quizzes['custom'])>0:
            self.frames[custom_quiz]=custom_quiz(container,self,quiz_index=0)
            self.frames[custom_quiz].grid(row=0,column=0,sticky='nsew')
        
        self.show_frame(main_page)
    
    def show_frame(self,cont,**kwargs):
        if cont not in self.frames or kwargs:
            container=self.frames[list(self.frames.keys())[0]].master
            self.frames[cont]=cont(container,self,**kwargs)
            self.frames[cont].grid(row=0,column=0,sticky='nsew')
        
        frame=self.frames[cont]
        if cont==custom_quiz_list:
            frame.refresh()
        frame.tkraise()

class Quiz:
    def __init__(self,title,questions):
        self.title=title
        self.questions=questions
        
    def get_question(self,index):
        if 0<=index<len(self.questions):
            return self.questions[index]
        return None

quizzes={
    'default': Quiz(
        'Red Dead Redemption Personality Quiz',
        [
            {
                'question': 'How do you handle betrayal?',
                'options': ['Try to understand their reason', 'Talk it out and move forward', 'Cut them off, no questions   asked', 'Use it against them later'],
                'points': ['1', '3', '5', '6'],
            },
            {
                'question': 'What matters most to you in life?',
                'options': ['Honor and redemption', 'Legacy and vision', 'Family and security', 'Power and control'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'How do you react under pressure?',
                'options': ['Calmly think things through', 'Trust your gut instinct', 'Act fast, fix later', 'Push others to    take the fall'],
                'points': ['5', '3', '4', '6'],
            },
            {
                'question': 'You find a large sum of money. What do you do?',
                'options': ['Give it to someone in need', 'Hide it and plan its use wisely', 'Use it to help your loved ones',  'Keep it all for yourself'],
                'points': ['2', '5', '4', '6'],
            },
            {
                'question': 'What’s your idea of loyalty?',
                'options': ['Standing by someone even when it’s hard', 'Being loyal until they cross you', 'Loyal to those who  earn it', 'Loyalty is just a means to an end'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'You’re in a tough moral situation. What guides your actions?',
                'options': ['Your conscience', 'Your goals', 'The needs of your family', 'Your survival'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'How do you want to be remembered?',
                'options': ['As a man who tried to do right', 'As a visionary', 'As a provider and protector', 'As someone who  outlived them all'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'How do you handle being wrong?',
                'options': ['Admit it and grow', 'Rationalize it', 'Quietly fix your mistake', 'Deny and deflect'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'What do you enjoy doing the most?',
                'options': ['Reflecting on life and journaling', 'Planning the next big move', 'Spending time with family',     'Getting what you want, however you can'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'How do you lead others?',
                'options': ['By example', 'Through vision and persuasion', 'By making practical decisions', 'By manipulation and    force'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'What’s your greatest flaw?',
                'options': ['Guilt and overthinking', 'Pride and delusion', 'Stubbornness', 'Ruthlessness'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'If someone you care about betrays you, how do you respond?',
                'options': ['Hurt but try to forgive', 'Cut ties with a speech', 'Avoid them, let time heal it', 'Plot revenge'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'What would your role in a gang be?',
                'options': ['The loyal right hand', 'The charismatic leader', 'The dependable enforcer', 'The wildcard with his     own rules'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'What’s your relationship with violence?',
                'options': ['Necessary evil', 'Tool to get things done', 'Only when loved ones are at risk', 'Power is power'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'How do you see the law?',
                'options': ['Flawed but necessary', 'Just another obstacle', 'A danger to protect your family from', 'Meant to  be outsmarted'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'You’re in a crisis. What’s your move?',
                'options': ['Look for a peaceful solution', 'Stir up a distraction', 'Protect your own first', 'Exploit the     chaos'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'What drives you forward?',
                'options': ['Redemption', 'Glory', 'Security', 'Self-preservation'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'What do you fear the most?',
                'options': ['Dying without making amends', 'Irrelevance', 'Losing your loved ones', 'Losing control'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'How do you handle success?',
                'options': ['Stay humble', 'Use it to reach higher', 'Build a better life for your family', 'Flaunt it'],
                'points': ['2', '4', '5', '6'],
            },
            {
                'question': 'If you had to pick one value to live by, what would it be?',
                'options': ['Integrity', 'Power', 'Responsibility', 'Dominance'],
                'points': ['2', '4', '5', '6'],
            },
        ]
    ),
    'custom':[]
}

class default_landing(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        # images
        self.morgan_image=PhotoImage(file='images/morgan.png')
        self.marston_image=PhotoImage(file='images/marston.png')
        self.dutch_image=PhotoImage(file='images/dutch.png')
        self.hosea_image=PhotoImage(file='images/hosea.png')
        self.bell_image=PhotoImage(file='images/bell.png')
        
        center_frame=tk.Frame(self)
        center_frame.grid(row=0,column=0,sticky='nsew')
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        
        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_rowconfigure(1, weight=1)
        center_frame.grid_rowconfigure(2, weight=1)
        center_frame.grid_rowconfigure(3, weight=1)
        center_frame.grid_rowconfigure(4, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)
        center_frame.grid_columnconfigure(1, weight=1)
        center_frame.grid_columnconfigure(2, weight=1)
        center_frame.grid_columnconfigure(3, weight=1)
        center_frame.grid_columnconfigure(4, weight=1)
        
        self.main_label=ttk.Label(center_frame,text='Want to know which character you are?',font=SUBTITLE_FONT)
        self.dutch_image_label=ttk.Label(center_frame,image=self.dutch_image)
        self.dutch_text=ttk.Label(center_frame,text='Dutch Van Der Linde',font=REGULAR_FONT)
        self.dutch_description=ttk.Label(center_frame,text='Charismatic, ambitious, unpredictable')
        
        self.hosea_image_label=ttk.Label(center_frame,image=self.hosea_image)
        self.hosea_text=ttk.Label(center_frame,text='Hosea Matthews',font=REGULAR_FONT)
        self.hosea_description=ttk.Label(center_frame,text='Wise, calm, strategic')
        
        self.morgan_image_label=ttk.Label(center_frame,image=self.morgan_image)
        self.morgan_text=ttk.Label(center_frame,text='Arthur Morgan',font=REGULAR_FONT)
        self.morgan_description=ttk.Label(center_frame,text='Loyal, introspective, hardened')
        
        self.marston_image_label=ttk.Label(center_frame,image=self.marston_image)
        self.marston_text=ttk.Label(center_frame,text='John Marston',font=REGULAR_FONT)
        self.marston_description=ttk.Label(center_frame,text='Practical, family-man')
        
        self.bell_image_label=ttk.Label(center_frame,image=self.bell_image)
        self.bell_text=ttk.Label(center_frame,text='Micah Bell',font=REGULAR_FONT)
        self.bell_description=ttk.Label(center_frame,text='Survivor, manipulative, self-sufficient')
        
        self.proceed_button=ttk.Button(center_frame,text='Proceed',command=lambda:controller.show_frame(default_quiz))
        
        
        self.main_label.grid(row=0, column=0, columnspan=5, padx=200, pady=(0, 20), sticky='nsew')
        
        self.dutch_image_label.grid(row=1, column=0, padx=20)
        self.dutch_text.grid(row=2, column=0)
        self.dutch_description.grid(row=3, column=0)
        
        self.hosea_image_label.grid(row=1, column=1)
        self.hosea_text.grid(row=2, column=1)
        self.hosea_description.grid(row=3, column=1)
        
        self.morgan_image_label.grid(row=1, column=2)
        self.morgan_text.grid(row=2, column=2)
        self.morgan_description.grid(row=3, column=2)
        
        self.marston_image_label.grid(row=1, column=3)
        self.marston_text.grid(row=2, column=3)
        self.marston_description.grid(row=3, column=3)
        
        self.bell_image_label.grid(row=1, column=4)
        self.bell_text.grid(row=2, column=4)
        self.bell_description.grid(row=3, column=4)
        
        self.proceed_button.grid(row=4, column=0, columnspan=5, padx=20, pady=20)

class main_page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        center_frame=tk.Frame(self)
        center_frame.grid(row=0,column=0)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        
        label=ttk.Label(center_frame,text='Cornel Quiz',font=TITLE_FONT)
        sub_label=ttk.Label(center_frame,text='Main Page',font=REGULAR_FONT)
        made_by_text=ttk.Label(center_frame,text='Made by GrendpaCornel09 on GitHub',font=REGULAR_FONT)
        default_quiz_button=ttk.Button(center_frame,text='RDR2 Personality Quiz',command=lambda:controller.show_frame(default_landing))
        make_a_quiz_button=ttk.Button(center_frame,text='Make a quiz',command=lambda:controller.show_frame(make_a_quiz))
        custom_quiz_button=ttk.Button(center_frame,text='Take custom quiz',command=lambda:controller.show_frame(custom_quiz_list))
        
        label.grid(row=0,column=0,columnspan=3,pady=(10,0))
        sub_label.grid(row=1,column=0,columnspan=3)
        made_by_text.grid(row=2,column=0,columnspan=3)
        default_quiz_button.grid(row=3,column=0,columnspan=3,padx=10,pady=20)
        make_a_quiz_button.grid(row=4,column=0,columnspan=2,padx=10,pady=20)
        custom_quiz_button.grid(row=4,column=1,columnspan=2,padx=10,pady=20)

class default_quiz(tk.Frame):
    user_base_score=0
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        self.controller=controller
        self.quiz=quizzes['default']
        self.current_question_index=0
        # self.answer_state='incorrect'
        
        center_frame=tk.Frame(self)
        center_frame.grid(row=0,column=0)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        
        self.label=ttk.Label(center_frame,text=self.quiz.title,font=SUBTITLE_FONT)
        self.question_label=ttk.Label(center_frame,text='',font=REGULAR_FONT)
        # self.correct_incorrect_label=ttk.Label(self,text=self.answer_state,font=REGULAR_FONT)
        self.options=[]
        
        for i in range(4):
            button=ttk.Button(center_frame,text='',command=lambda i=i:self.check_answer(i))
            self.options.append(button)
        
        self.score_text=ttk.Label(center_frame,text=f'Base Score: {self.user_base_score}')
        # self.back_button=ttk.Button(center_frame,text='Main page',command=self.go_to_main_page)
        self.back_button=ttk.Button(center_frame,text='Main page',command=lambda:controller.show_frame(main_page))
        
        self.label.grid(row=0,column=0,columnspan=2,padx=10,pady=(10,50))
        self.question_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        for i,button in enumerate(self.options):
            button.grid(row=2+i,column=0,columnspan=2,padx=10,pady=5)
        self.score_text.grid(row=6,column=0,columnspan=3,pady=(40,0))
        self.back_button.grid(row=7,column=0,columnspan=3,pady=(10,20))
        
        self.load_question()
    
    def load_question(self):
        self.you_are_label=ttk.Label(self,text='You are...',font=REGULAR_FONT)
        
        question=self.quiz.get_question(self.current_question_index)
        if question:
            self.question_label.config(text=question['question'])
            for i,option in enumerate(question['options']):
                self.options[i].config(text=option)
        else:
            for button in self.options:
                button.grid_remove()
            self.question_label.config(text='Quiz Complete!')
            self.you_are_label.grid(column=0,row=1,columnspan=2,padx=10,pady=10)
            
            if 20<=int(self.user_base_score)<=40:
                self.morgan_image=PhotoImage(file='images/morgan.png')
                self.morgan_image_label=ttk.Label(self,image=self.morgan_image)
                self.morgan_text=ttk.Label(self,text='Arthur Morgan',font=REGULAR_FONT)
                self.morgan_description=ttk.Label(self,text='Loyal, introspective, hardened')
                self.morgan_image_label.grid(row=2, column=0, columnspan=2)
                self.morgan_text.grid(row=3, column=0, columnspan=2)
                self.morgan_description.grid(row=4, column=0, columnspan=2, pady=(0,20))
            elif 41<=int(self.user_base_score)<=60:
                self.dutch_image=PhotoImage(file='images/dutch.png')
                self.dutch_image_label=ttk.Label(self,image=self.dutch_image)
                self.dutch_text=ttk.Label(self,text='Dutch Van Der Linde',font=REGULAR_FONT)
                self.dutch_description=ttk.Label(self,text='Charismatic, ambitious, unpredictable')
                self.dutch_image_label.grid(row=2, column=0, columnspan=2)
                self.dutch_text.grid(row=3, column=0, columnspan=2)
                self.dutch_description.grid(row=4, column=0, columnspan=2, pady=(0,20))
            elif 61<=int(self.user_base_score)<=80:
                self.marston_image=PhotoImage(file='images/marston.png')
                self.marston_image_label=ttk.Label(self,image=self.marston_image)
                self.marston_text=ttk.Label(self,text='John marston',font=REGULAR_FONT)
                self.marston_description=ttk.Label(self,text='Practical, family-man')
                self.marston_image_label.grid(row=2, column=0, columnspan=2)
                self.marston_text.grid(row=3, column=0, columnspan=2)
                self.marston_description.grid(row=4, column=0, columnspan=2, pady=(0,20))
            elif 81<=int(self.user_base_score)<=100:
                self.hosea_image=PhotoImage(file='images/hosea.png')
                self.hosea_image_label=ttk.Label(self,image=self.hosea_image)
                self.hosea_text=ttk.Label(self,text='Hosea Matthews',font=REGULAR_FONT)
                self.hosea_description=ttk.Label(self,text='Wise, calm, strategic')
                self.hosea_image_label.grid(row=2, column=0, columnspan=2)
                self.hosea_text.grid(row=3, column=0, columnspan=2)
                self.hosea_description.grid(row=4, column=0, columnspan=2, pady=(0,20))
            else:
                self.bell_image=PhotoImage(file='images/bell.png')
                self.bell_image_label=ttk.Label(self,image=self.bell_image)
                self.bell_text=ttk.Label(self,text='Micah bell',font=REGULAR_FONT)
                self.bell_description=ttk.Label(self,text='Survivor, manipulative, self-sufficient')
                self.bell_image_label.grid(row=2, column=0, columnspan=2)
                self.bell_text.grid(row=3, column=0, columnspan=2)
                self.bell_description.grid(row=4, column=0, columnspan=2, pady=(0,20))
    
    def check_answer(self,selected_index):
        question=self.quiz.get_question(self.current_question_index)
        answer_point=question['points'][selected_index] if question else None
        # if question and question['options'][selected_index]==question['answer']:
        #     ttk.Label(self,text='correct :)',font=REGULAR_FONT).grid(row=6,column=0,padx=10,pady=10)
        # else:
        #     ttk.Label(self,text='incorrect :(',font=REGULAR_FONT).grid(row=6,column=0,padx=10,pady=10)
        self.user_base_score=str(int(self.user_base_score)+int(answer_point))
        self.score_text.config(text=f'Base Score: {self.user_base_score}')
        self.current_question_index+=1
        self.load_question()
    
    # def reset_quiz(self):
    #     self.user_base_score=0
    #     self.current_question_index=0
    #     self.score_text.config(text=f'Base Sscore: {self.user_base_score}')
    #     self.load_question()
    
    # def go_to_main_page(self):
    #     self.reset_quiz()
    #     self.controller.show_frame(main_page)

class make_a_quiz(tk.Frame):
    question_count=0
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        center_frame=tk.Frame(self)
        center_frame.grid(row=0,column=0)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        
        # self.question_count=question_count
        self.controller=controller
        self.title_label=ttk.Label(center_frame,text='Create a Custom Quiz',font=TITLE_FONT)
        self.title_entry=ttk.Entry(center_frame)
        self.question_count_label=ttk.Label(center_frame,text=f'Questions: {self.question_count}')
        self.add_question_button=ttk.Button(center_frame,text='Add Question',command=self.add_question)
        self.save_quiz_button=ttk.Button(center_frame,text='Save Quiz',command=self.save_quiz)
        
        self.back_button=ttk.Button(center_frame,text='Main page',command=lambda:controller.show_frame(main_page))
        
        self.title_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
        self.title_entry.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        self.question_count_label.grid(row=2,columnspan=2,padx=10,pady=10)
        self.add_question_button.grid(row=3,column=0,padx=10,pady=10)
        self.save_quiz_button.grid(row=3,column=1,padx=10,pady=10)
        self.back_button.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
        
        self.questions=[]
        
        print(self.questions)
    
    def add_question(self):
        # self.open_question_window()
        if not self.title_entry.get():
            showwarning(title='Warning',message='You need a title for your quiz.')
        else:
            self.open_question_window()

    def save_quiz(self):
        title=self.title_entry.get()
        if title and self.questions:
            quizzes['custom'].append(Quiz(title,self.questions))
            self.questions=[]
            self.title_entry.delete(0,tk.END)
            self.question_count=len(self.questions)
            self.question_count_label.config(text=f'Questions: {self.question_count}')
            print(quizzes['custom'])
            showinfo(title='Quiz saved',message=f"Custom quiz '{title}' has been saved.")
        else:
            showwarning(title='Warning',message='Provide title and questions first.')
    
    def open_question_window(self):
        new_window=Toplevel(self)
        new_window.title('Add a question')
        
        question_label = ttk.Label(new_window, text="Enter your question:", font=REGULAR_FONT)
        question_entry = ttk.Entry(new_window, width=50)
        options_label = ttk.Label(new_window, text="Enter 4 options (comma-separated):", font=REGULAR_FONT)
        options_entry = ttk.Entry(new_window, width=50)
        answer_label = ttk.Label(new_window, text="Enter the correct answer:", font=REGULAR_FONT)
        answer_entry = ttk.Entry(new_window, width=50)
        save_button = ttk.Button(new_window, text="Save Question", command=lambda: self.save_question(new_window, question_entry, options_entry, answer_entry))
        
        question_label.grid(row=0, column=0, padx=10, pady=10)
        question_entry.grid(row=0, column=1, padx=10, pady=10)
        options_label.grid(row=1, column=0, padx=10, pady=10)
        options_entry.grid(row=1, column=1, padx=10, pady=10)
        answer_label.grid(row=2, column=0, padx=10, pady=10)
        answer_entry.grid(row=2, column=1, padx=10, pady=10)
        save_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def save_question(self,window,question_entry,options_entry,answer_entry):
        question=question_entry.get()
        options=[re.sub(r'\s+', '', option) for option in options_entry.get().lower().split(',')]
        answer=re.sub(r'\s+', '', answer_entry.get().lower())
        
        if not question or not options or not answer:
            showwarning(title='Warning',message='Fill out all fields.')
            return
        elif answer not in options:
            showwarning(title='Warning',message='Answer not provided in options.')
            return
        elif len(options)<4 or len(options)>4:
            showwarning(title='Warning',message='There must be 4 options.')
            return

        self.questions.append({
            'question':question,
            'options':options,
            'answer':answer
        })
        
        print(f'Question added:{question}')
        print(f'Options: {options}')
        print(f'Answer: {answer}')
        
        self.question_count+=1
        self.question_count_label.config(text=f'Questions: {self.question_count}')
        
        window.destroy()

class custom_quiz_list(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        center_frame=tk.Frame(self)
        center_frame.grid(row=0,column=0)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        
        self.controller=controller
        
        self.label=ttk.Label(center_frame,text='QUIZ LIST',font=TITLE_FONT)
        self.emptylabel=ttk.Label(center_frame,text='You have no quizzes!',font=REGULAR_FONT)
        self.back_button=ttk.Button(self,text='Main page',command=lambda:controller.show_frame(main_page))
        
        self.label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
        
        self.quiz_buttons=[]
    
    def refresh(self):        
        for button in self.quiz_buttons:
            button.destroy()
        self.quiz_buttons=[]
        
        if len(quizzes['custom'])<1:
            self.emptylabel.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        else:
            self.emptylabel.grid_remove()
            for i,quiz in enumerate(quizzes['custom']):
                quiz_button=ttk.Button(self,text=quiz.title,command=lambda i=i:self.controller.show_frame(custom_quiz,quiz_index=i))
                quiz_button.grid(row=i+1,column=0,columnspan=2,padx=10,pady=5)
        
        self.back_button.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

class custom_quiz(tk.Frame):    
    def __init__(self,parent,controller,quiz_index):
        tk.Frame.__init__(self,parent)
        
        center_frame=tk.Frame(self)
        center_frame.grid(row=0,column=0)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        
        self.controller=controller
        self.quiz_index=quiz_index
        
        if quiz_index>=len(quizzes['custom']):
            self.label=ttk.Label(center_frame,text='Invalid quiz.',font=TITLE_FONT)
            self.label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
            return
        
        self.quiz=quizzes['custom'][self.quiz_index]
        self.current_question_index=0
        # self.answer_state='incorrect'
        
        self.label=ttk.Label(center_frame,text=self.quiz.title,font=TITLE_FONT)
        self.question_label=ttk.Label(center_frame,text='',font=REGULAR_FONT)
        self.options=[]
        
        for i in range(4):
            button=ttk.Button(center_frame,text='',command=lambda i=i:self.check_answer(i))
            self.options.append(button)
        
        self.back_button=ttk.Button(center_frame,text='Main page',command=lambda:controller.show_frame(main_page))
        
        self.label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
        self.question_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        for i,button in enumerate(self.options):
            button.grid(row=2+i,column=0,columnspan=2,padx=10,pady=5)
        self.back_button.grid(row=7,column=0,columnspan=2,padx=10,pady=10)
        
        self.load_question()
    
    def load_question(self):
        question=self.quiz.get_question(self.current_question_index)
        if question:
            self.question_label.config(text=question['question'])
            for i,option in enumerate(question['options']):
                self.options[i].config(text=option)
        else:
            self.question_label.config(text='Quiz Complete!')
            for button in self.options:
                button.grid_remove()
    
    def check_answer(self,selected_index):
        question=self.quiz.get_question(self.current_question_index)
        if question and question['options'][selected_index]==question['answer']:
            ttk.Label(self,text='correct :)',font=REGULAR_FONT).grid(row=6,column=0,padx=10,pady=10)
        else:
            ttk.Label(self,text='incorrect :(',font=REGULAR_FONT).grid(row=6,column=0,padx=10,pady=10)
        self.current_question_index+=1
        self.load_question()

# bottom-most
app=tkinterApp()
app.mainloop()