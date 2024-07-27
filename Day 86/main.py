import tkinter as tk
import time
import random


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        # Setting the background color to blue
        self.root.configure(bg='#1e3c72')

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be or not to be, that is the question.",
            "All that glitters is not gold.",
            "The pen is mightier than the sword."
        ]

        self.current_sentence = random.choice(self.sentences)
        self.start_time = None

        self.sentence_label = tk.Label(root, text=self.current_sentence, font=("Arial", 16), bg='#1e3c72', fg="white",
                                       wraplength=500)
        self.sentence_label.pack(pady=20)

        self.input_text = tk.Text(root, height=5, width=50, font=("Arial", 14), bg="white", fg="black", wrap=tk.WORD,
                                  borderwidth=2, relief="solid")
        self.input_text.pack(pady=20)
        self.input_text.bind("<KeyPress>", self.start_typing)

        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg='#1e3c72', fg="white")
        self.result_label.pack(pady=20)

        self.check_button = tk.Button(root, text="Check Speed", command=self.check_speed, font=("Arial", 14),
                                      bg="#4caf50", fg="white", borderwidth=2, relief="solid", padx=10, pady=5)
        self.check_button.pack(pady=20)

    def start_typing(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_speed(self):
        end_time = time.time()
        input_text = self.input_text.get("1.0", "end-1c")
        time_taken = end_time - self.start_time
        words_per_minute = len(input_text.split()) / (time_taken / 60)

        self.result_label.config(text=f"Time: {time_taken:.2f} seconds\nSpeed: {words_per_minute:.2f} WPM")
        self.start_time = None

        self.current_sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.current_sentence)
        self.input_text.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()