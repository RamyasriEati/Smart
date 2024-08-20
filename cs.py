import tkinter as tk
import random
from tkinter import messagebox

# List of states and their capitals
states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

class QuizApp:
    def _init_(self, root):
        self.root = root
        self.root.title("State Capitals Quiz")
        self.score = 0
        self.total_questions = 0
        
        self.label = tk.Label(root, text="Click 'Start Quiz' to begin!", font=('Helvetica', 16))
        self.label.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=('Helvetica', 14))
        self.question_label.pack(pady=20)

        self.entry = tk.Entry(root, font=('Helvetica', 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_answer)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=('Helvetica', 14))
        self.submit_button.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, font=('Helvetica', 14))
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=('Helvetica', 14))
        self.result_label.pack(pady=20)

    def start_quiz(self):
        self.total_questions = 0
        self.score = 0
        self.ask_question()

    def ask_question(self):
        self.state = random.choice(list(states_and_capitals.keys()))
        self.question_label.config(text=f"What is the capital of {self.state}?")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.total_questions += 1

    def check_answer(self, event=None):
        capital = states_and_capitals[self.state]
        user_answer = self.entry.get().strip()
        if user_answer.lower() == capital.lower():
            self.score += 1
            self.result_label.config(text=f"Correct! Your score: {self.score}/{self.total_questions}")
        else:
            self.result_label.config(text=f"Incorrect! The capital of {self.state} is {capital}. Your score: {self.score}/{self.total_questions}")
        
        if self.total_questions < 10:  # Adjust the number of questions as needed
            self.ask_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Quiz Finished!\nYour final score is: {self.score}/{self.total_questions}")
            self.question_label.config(text="Quiz Finished!")
            self.start_button.config(text="Restart Quiz")
            self.result_label.config(text="")

if _name_ == "_main_":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
