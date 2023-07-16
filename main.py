import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
BROWN = "#7D7463"
RED = "#FE0000"
GREY = "#A8A196"
BEIGE = "#F4E0B9"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
one_check = "✅"
two_check = "✅✅"
three_check = "✅✅✅"
four_check = "✅✅✅✅"
timer = None


# ---------------------------- WINDOW PUP UP ------------------------------- #
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    title_text.config(text="Timer", fg=BROWN)
    canvas.itemconfig(timer_text, text="00:00")
    start_button["state"] = "active"
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button["state"] = "disabled"
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 6

    if reps % 2 != 0:
        window.bell()
        countdown(work_sec)
        focus_window("off")
        title_text.config(text="Work!!", fg=RED)
    elif reps % 2 == 0:
        window.bell()
        focus_window("on")
        countdown(short_break_sec)
        title_text.config(text="Take a small break.", fg=BROWN)
        if reps == 2:
            check_marks.config(text=one_check)
        if reps == 4:
            check_marks.config(text=two_check)
        if reps == 6:
            check_marks.config(text=three_check)
    elif reps == 8:
        window.bell()
        countdown(long_break_sec)
        focus_window("off")
        title_text.config(text="Long break time. Good job! Click reset after the time is done to start again.")
        check_marks.config(text=four_check)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Window & Background set up
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BEIGE)

canvas = tk.Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Buttons & Header & Checkmarks
start_button = tk.Button(text="Start", command=start_timer, font=FONT_NAME, bg=BEIGE, highlightbackground=BEIGE)
start_button.grid(column=1, row=4)

reset_button = tk.Button(text="Reset", command=reset, font=FONT_NAME, bg=BEIGE, highlightbackground=BEIGE)
reset_button.grid(column=3, row=4)

title_text = tk.Label(text="Timer", font=(FONT_NAME, 44), fg=BROWN, bg=BEIGE, highlightbackground=BEIGE)
title_text.grid(column=2, row=1)

check_marks = tk.Label(bg=BEIGE, highlightbackground=BEIGE)
check_marks.grid(column=2, row=5)

window.mainloop()
