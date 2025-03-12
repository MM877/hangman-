import random
import tkinter as tk
from tkinter import messagebox

# Hangman stages (graphical representation)
hangman_stages = [
    """
      ------
      |    |
      |    
      |    
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |    
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |    |
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |    
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |    
    =====
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |    
    =====
    """
]

word_list = ['camel', 'lion', 'joy', 'tiger', 'zebra', 'cheetah']


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x500")

        self.letter_buttons = []
        self.reset_game()

        self.hangman_label = tk.Label(root, text=hangman_stages[self.attempts], font=("Courier", 12))
        self.hangman_label.pack(pady=10)

        self.word_label = tk.Label(root, text=" ".join(self.placeholder), font=("Helvetica", 20))
        self.word_label.pack()

        self.create_letter_buttons()

        self.reset_button = tk.Button(root, text="Restart", command=self.reset_game, bg="red", fg="white")
        self.reset_button.pack(pady=10)

    def reset_game(self):
        self.choosen_word = random.choice(word_list)
        self.placeholder = ['_' for _ in self.choosen_word]
        self.attempts = 0
        self.used_letters = set()
        if hasattr(self, 'hangman_label'):
            self.hangman_label.config(text=hangman_stages[self.attempts])
        if hasattr(self, 'word_label'):
            self.word_label.config(text=" ".join(self.placeholder))
        for btn in self.letter_buttons:
            btn.config(state=tk.NORMAL)

    def create_letter_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for letter in "abcdefghijklmnopqrstuvwxyz":
            btn = tk.Button(frame, text=letter.upper(), width=4, height=2,
                            command=lambda l=letter: self.guess_letter(l))
            btn.grid(row=(ord(letter) - ord('a')) // 6, column=(ord(letter) - ord('a')) % 6)
            self.letter_buttons.append(btn)

    def guess_letter(self, letter):
        if letter in self.used_letters:
            return

        self.used_letters.add(letter)
        correct_guess = False

        # Disable the button for this letter
        for btn in self.letter_buttons:
            if btn['text'] == letter.upper():
                btn.config(state=tk.DISABLED)

        for i, char in enumerate(self.choosen_word):
            if char == letter:
                self.placeholder[i] = letter
                correct_guess = True

        self.word_label.config(text=" ".join(self.placeholder))

        if not correct_guess:
            self.attempts += 1
            self.hangman_label.config(text=hangman_stages[self.attempts])

        if "_" not in self.placeholder:
            messagebox.showinfo("Hangman", "You Win!")
            self.reset_game()
        elif self.attempts == len(hangman_stages) - 1:
            messagebox.showinfo("Hangman", f"You Lost! The word was: {self.choosen_word}")
            self.reset_game()


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()