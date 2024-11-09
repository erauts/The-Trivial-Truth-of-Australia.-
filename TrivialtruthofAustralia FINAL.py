import tkinter as tk
from tkinter import messagebox

# Class contains all the necessary information needed for the quiz application such as questions and answers
class QuizApp:
    def __init__(self, root):
        # The main window that is opened upon running the code
        self.root = root
        self.root.title("The Trivial Truth of Australia")

        #Set the size of the main window to make sure all text is easily viewable
        self.root.geometry ("900x300")

        # Using a dictionary, it creates a location for the quiz question, answer options and correct answers to be kept
        self.questions = [
            {"Question": "1. What does Terra Nullius mean?", "Options": ["A. Australia", "B. Everybody's land", "C. Nobody's land", "D. Unknown Southern land"],
             "Answer": "C. Nobody's land", "Points" : 10},
            {"Question":"2. When did the First Fleet arrive in Australia?", "Options": ["A. 22nd August 1770", "B. 18th January 1788", "C. 26th January 1788", "D. 20th January 1789"],
             "Answer": "B. 18th January 1788", "Points" : 10},
            {"Question": "3. What was the most deadly disease that was brought to Australia by the First Fleet?", "Options": ["A. Tuberculosis", "B. Small Pox", "C. Measles", "D. Influenza"],
             "Answer": "B. Small Pox", "Points" : 10},
            {"Question": " 4. Was Barangaroo, wife of Bennelong, supportive of her husbands endeavors with Captain Phillip",
             "Options": ["A. Supportive", "B. Unsupportive","C. Supportive at first", "D. Unsupportive at first"],
             "Answer": "B. Unsupportive", "Points" : 10},
            {"Question": "5. What was the estimated Indigenous population before British arrival?", "Options" : ["A. 750,000", "B. 1,000,000", "C. 500,000", "D. 315,000"],
             "Answer" : "A. 750,000", "Points" : 10},
            {"Question": "6. When the British arrived to Australia, did they initiate a treaty with the Indigenous clans of Sydney?",
             "Options" : ["A. Yes", "B. No","C. It was rejected", "C. Indigenous intiated a treaty to the British"], "Answer": "B. No", "Points" : 10},
            {"Question": "7. What was the date & year of the first documented ‘Australia Day’?", "Options" : ["A. 18th January 1788","B. 30th July 1915", "C. 1st January 1901", "D. 26th January 1994"],
             "Answer" : "B. 30th July 1915", "Points" : 10},
            {"Question": "8. What year was it when Aboriginal and Torres Strait Islander peoples were allowed to vote?", "Options" : ["A. 1788", "B. 1843", "C. 1962", "D. 1984"],
             "Answer" : "C. 1962", "Points" : 10},
            {"Question" : "9. Why was Eddie Mabo such a pioneer for the Indigenous civil rights movement?",
             "Options" : ["A. The campaign for a right to vote",
                          "B. The campaign for census recognition",
                          "C. The campaign for the stolen generation",
                          "D. The campaign for native title"],
             "Answer" : "D. The campaign for native title", "Points" : 10},
            {"Question" : "10. What state in Australia currently has the highest Indigenous population?", "Options" : ["A. Tasmania", "B. Northern Territory", "C. New South Wales", "D. Queensland"],
             "Answer" : "C. New South Wales", "Points" : 10},
            {"Question" : "11. Prior to the First Fleet's arrival there were 250 languages, how many language groups do you think are in 2024?",
             "Options" : ["A. 150", "B. 250", "C. 50", "D. 10"], "Answer" : "A. 150", "Points" : 10}
            ]

        # Initializing the index for the current question 
        self.current_question = 0
        self.score = 0

        # Creates a label to display the current questions
        self.question_label = tk.Label(self.root, text=self.questions[self.current_question]["Question"], font=("Arial", 16,"bold"))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        #Centre the answer options in the window
        options_frame = tk.Frame (self.root)
        options_frame.pack(pady=20)


        #Create buttons for each options, and align them in the centre of the screen
        self.option_buttons = []
        for option in self.questions [self.current_question]["Options"]:
            button = tk.Radiobutton(options_frame, text=option, variable=self.var, value=option, font=("Arial",14))
            button.pack(side='top', pady = 5)
            self.option_buttons.append(button)

        # Next button to submit answer and move to the next question
        self.submit_button = tk.Button(self.root, text="Next Question", command=self.check_answer, font=("Arial", 14,"bold"))
        self.submit_button.pack(pady=20)

    # Checking if the user has answered the question correctly
    def check_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.current_question]["Answer"]
        points = self.questions[self.current_question]["Points"]

        # If the answer is correct, increment the score
        if selected_answer == correct_answer:
            self.score += points

        # Move to the next question
        self.current_question +=1

        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_result()  

    # Update the question label and options for the next question
    def update_question(self):
        
    # Update the question label with the current question text
        self.question_label.config(text=self.questions[self.current_question]["Question"])

        # Reset the radio button selection
        self.var.set("")

        # Update the options for the current question
        for i, option in enumerate(self.questions[self.current_question]["Options"]):
            self.option_buttons[i].config(text=option)

    # Show the final score at the end of the quiz
    def show_result(self):
        messagebox.showinfo("Well Done, Quiz is Completed!", f"Well Done, Quiz is Completed!{self.score}/{len(self.questions)}")
    #Close the window when the quiz is finished
        self.root.quit() 

#Create the main window
root = tk.Tk()

#Create an instance of the QuizApp class and pass the root window to it
quiz_app = QuizApp(root)

#Start the Tkinter event loop
root.mainloop()
