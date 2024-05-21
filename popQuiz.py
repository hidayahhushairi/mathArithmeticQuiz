import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title("Mathematics Pop Quiz")
root.geometry("400x500")

# Create parent window
root_window = tk.Frame(root)
root_window.pack()

total = 0
current_score = 0
timer = 120  # 2 minutes
def open():
    root_window.destroy()

    ques_window = tk.Toplevel(root)
    ques_window.geometry("400x500")
    ques_window.title('Taking quiz....')

    global current_score, final_score, timer, question_label, answer_entry, result_label, Cscore_label, Fscore_label, timer_label
    current_score = 0
    timer = 120

    question_button = tk.Button(ques_window, text="Question", command=generate_question)
    question_button.pack()

    question_label = tk.Label(ques_window, text="Random number")
    question_label.pack()

    answer_entry = tk.Entry(ques_window)
    answer_entry.pack()

    check_button = tk.Button(ques_window, text="Check", command=check_answer)
    check_button.pack()

    Cscore_label = tk.Label(ques_window, text="Total Score: 0")
    Cscore_label.pack()

    Fscore_label = tk.Label(ques_window, text="")
    Fscore_label.pack()

    result_label = tk.Label(ques_window, text="Result: ")
    result_label.pack()

    timer_label = tk.Label(ques_window, text="Time left: 02:00")
    timer_label.pack()

    generate_question()
    ques_window.after(1000, countdown)  # start the countdown after 1 second
def generate_question():
    global num1, num2, total, operator, answer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    total += 1
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        num1 = num1 * num2  # to ensure division without remainder
        answer = num1 / num2
    question_label.config(text=f"{num1} {operator} {num2}")

def check_answer():
    global current_score, total, final_score, performance
    try:
        user_answer = float(answer_entry.get())
        if user_answer == answer:
            current_score += 1
            final_score = round((current_score/total) * 100)
            result_label.config(text="Result: Excellent, your answer is correct!")
        else:
            result_label.config(text="Result: Oh no, incorrect answer")
        Cscore_label.config(text=f"Total Score: {current_score}")

        if final_score == 100.0:
            performance = "Extraordinary"
        elif final_score >= 50:
            performance = "Great job! Not bad"
        else:
            performance = "Bad score won't last! Try again next time"

        generate_question()
        answer_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

def countdown():
    global timer
    if timer > 0:
        timer -= 1
        timer_label.config(text=f"Time left: {timer//60:02}:{timer%60:02}")
        root.after(1000, countdown)
    else:
        messagebox.showinfo("Out of time", f"Time's up!\nFINAL SCORE: {final_score}%\nPERFORMANCE: {performance}"
                                           f"\nTOTAL CORRECT ANSWER: {current_score}")
        root.quit()

# resize image and label
image = Image.open("mathquiz.png")
resize_img = image.resize((80, 80))
# width,height
img = ImageTk.PhotoImage(resize_img)

labelimage = tk.Label(root_window, image=img)
labelimage.image = img,
labelimage.pack(pady=(40, 0))

labeltext = tk.Label(root_window, text="Mathematics Pop Quiz", font=("Comic sans MS", 16, "bold"))
labeltext.pack(pady=(0, 50))

# resize image and label
image2 = Image.open("start.png")
resize_img2 = image2.resize((90, 40))
img2 = ImageTk.PhotoImage(resize_img2)

btnStart = tk.Button(root_window, image=img2, border=0, command=open)
btnStart.pack()

labelinstruction = tk.Label(root_window, text="Click Start to Answer Quiz", justify="center", font=("Consolas", 11))
labelinstruction.pack(pady=(10, 150))

labelinfo = tk.Label(root_window,
                     text="Pop quiz contains unlimited questions\nYou will be given 2 minutes to answer those questions",
                     width=100, font=("Times", 11), background="#000000", foreground="#FACA2F")
labelinfo.pack()

root.mainloop()
