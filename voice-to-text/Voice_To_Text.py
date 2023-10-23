import ttkbootstrap as tb
import Text_config
import threading
from tkinter import messagebox
import speech_recognition as sr

def start():
    def new_thread():
        text_area.delete("1.0", tb.END)
        progress_bar["value"] = 0
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                progress_bar.start()
                w.update_idletasks()
                audio = r.listen(source)
                text = r.recognize_google(audio)
                text_area.insert("1.0", text)
                progress_bar.stop()
                progress_bar["value"] = 100
                w.update_idletasks()

        except sr.UnknownValueError:
            err = "Sorry, I could not understand what you said"
            progress_bar.stop()
            progress_bar["value"] = 0
            w.update_idletasks()
            messagebox.showerror(title="Voice_To_Text", message=err)

        except sr.RequestError as e:
            err = "Could not request results from Google Speech Recognition service; {0}".format(e)
            progress_bar.stop()
            progress_bar["value"] = 0
            w.update_idletasks()
            messagebox.showerror(title="Voice_To_Text", message=err)

    thread = threading.Thread(name="new_thread", target=new_thread, daemon=True)
    thread.start()

w = tb.Window(themename="cyborg")
w.title("Speech-To-Text-Converter")
# CENTER WINDOW
win_width = 1000
win_height = 640
screen_width = w.winfo_screenwidth()
ycreen_height = w.winfo_screenheight()
x = int((screen_width / 2) - (win_width / 2))
y = int((ycreen_height / 2) - (win_height / 2))
w.geometry("{}x{}+{}+{}".format(win_width, win_height, x, y))
w.resizable(width=False, height=False)

version_number = tb.Label(w, text=Text_config.version_number,
                          font=("Impact", 13),
                          bootstyle="success").place(x=0, y=0)

title = tb.Label(w, text="Speech To Text",
                 font=("Impact", 25),
                 bootstyle="warning").pack()

enter_text = tb.Label(w,
                      text="Dont enter text as the computer will write what you said",
                      font=("Aerial", 17),
                      bootstyle="white")
enter_text.pack(pady=10)

text_area = tb.Text(w, width=160, height=10, fg="white", font=("Aerial", 20))
text_area.pack(pady=20)

text_B_style = tb.Style()
text_B_style.configure("success.TButton", font=("Aerial", 16))

text_B = tb.Button(w,
                   text="Press To Speak", bootstyle="success",
                   style="success.TButton",
                   width=20,
                   command=start)
text_B.pack(pady=5)

progress_bar = tb.Progressbar(w, value=0, maximum=100, bootstyle="success")
progress_bar.pack(pady=30, fill=tb.X, padx=50)

enter_text = tb.Label(w,
                      text="You need internet connection for this",
                      font=("Aerial", 17),
                      bootstyle="white")
enter_text.pack(pady=4)
w.mainloop()