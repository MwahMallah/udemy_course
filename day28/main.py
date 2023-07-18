from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 25
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    screen.after_cancel(timer)
    timer_label.config(fg=GREEN, text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")

    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    reps += 1

    screen.deiconify()
    screen.attributes("-topmost", 1)
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*10)
        timer_label.config(fg=RED, text="Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*10)
        timer_label.config(fg=PINK, text="Break")
    else:
        count_down(WORK_MIN*10)
        timer_label.config(fg=GREEN, text="Work")

    screen.attributes("-topmost", 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):    
    min = math.floor(count / 60)
    sec = int(count % 60)

    if sec < 10:
        sec = f"0{sec}"

    if min < 10:
        min= f"0{min}"

    time = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=time)

    if count < 0:
        start_timer()

        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔️"
        check_mark.config(text=mark)
    else:
        global timer
        timer = screen.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro app")
screen.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, NORMAL))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", bg="white", fg="black", command=start_timer)
start_button.grid(row=2, column=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, NORMAL))
check_mark.grid(row=3, column=1)

reset_button = Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

screen.mainloop()

