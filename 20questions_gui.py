import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkfont

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

def create_mammal_tree():
    root = BinaryTreeNode("Does it have fur?")

    root.left_child = BinaryTreeNode("Is it domesticated?")
    root.left_child.left_child = BinaryTreeNode("Is it a cat?")
    root.left_child.right_child = BinaryTreeNode("Is it a dog?")

    root.right_child = BinaryTreeNode("Is it a large mammal?")
    root.right_child.left_child = BinaryTreeNode("Is it an elephant?")
    root.right_child.right_child = BinaryTreeNode("Is it a dolphin?")

    return root

class TwentyQuestionsGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tree = create_mammal_tree()  # Load the initial mammal tree
        self.current_node = self.tree  # Start at the root of the tree
        self.title("20 Questions Game")
        self.geometry("560x250")

        self.configure(bg="#00C4A9")  # Alice Blue background
        button_font = tkfont.Font(size=12, weight="bold")
        label_font = tkfont.Font(size=22, weight="bold")

        self.label = tk.Label(
            self, text=self.current_node.data, bg="#00C4A9", font=label_font
        )
        self.label.pack(pady=15)

        self.yes_button = tk.Button(
            self, text="Yes", command=self.on_yes, bg="#32CD32", font=button_font, height=2, width=10
        )
        self.no_button = tk.Button(
            self, text="No", command=self.on_no, bg="#FF4500", font=button_font, height=2, width=10
        )
        self.unknown_button = tk.Button(
            self, text="Unknown", command=self.on_unknown, bg="#FFD700", font=button_font, height=2, width=10
        )
        self.maybe_button = tk.Button(
            self, text="Maybe", command=self.on_maybe, bg="#87CEEB", font=button_font, height=2, width=10
        )

        self.yes_button.pack(side=tk.LEFT, padx=10, pady=15)
        self.no_button.pack(side=tk.LEFT, padx=10, pady=15)
        self.unknown_button.pack(side=tk.LEFT, padx=10, pady=15)
        self.maybe_button.pack(side=tk.RIGHT, padx=10, pady=15)

    def on_yes(self):
        if self.current_node.is_leaf():
            guess = self.current_node.data
            answer = messagebox.askyesno("Guess", f"Is it a {guess}?")
            if answer:
                messagebox.showinfo(
                    "Congratulations!", f"🎉 Congratulations! I guessed it! 🎉"
                )
                self.restart_game()
            else:
                self.add_new_mammal()
        else:
            self.current_node = self.current_node.left_child
            self.label.config(text=self.current_node.data)

    def on_no(self):
        if self.current_node.is_leaf():
            guess = self.current_node.data
            answer = messagebox.askyesno("Guess", f"Is it a {guess}?")
            if answer:
                messagebox.showinfo(
                    "Congratulations!", f"🎉 Congratulations! I guessed it! 🎉"
                )
                self.restart_game()
            else:
                self.add_new_mammal()
        else:
            self.current_node = self.current_node.right_child
            self.label.config(text=self.current_node.data)

    def on_unknown(self):
        messagebox.showinfo(
            "Unknown",
            "If you're unsure, let's consider this a 'No' answer for now.",
        )
        if not self.current_node.is_leaf():
            self.current_node = self.current_node.right_child
            self.label.config(text=self.current_node.data)

    def on_maybe(self):
        messagebox.showinfo(
            "Maybe",
            "Since it's a maybe, let's follow the 'Yes' path.",
        )
        if not self.current_node.is_leaf():
            self.current_node = self.current_node.left_child
            self.label.config(text=self.current_node.data)

    def add_new_mammal(self):
        current_guess = self.current_node.data
        new_mammal = simpledialog.askstring("Add New Mammal", "What is the correct answer?")
        new_question = simpledialog.askstring(
            "New Question",
            f"Provide a yes/no question to distinguish {current_guess} from {new_mammal}:"
        )
        correct_answer = messagebox.askyesno(
            "Correct Answer", f"For your mammal, {new_question}?"
        )

        self.current_node.data = new_question
        if correct_answer:
            self.current_node.left_child = BinaryTreeNode(new_mammal)
            self.current_node.right_child = BinaryTreeNode(current_guess)
        else:
            self.current_node.left_child = BinaryTreeNode(current_guess)
            self.current_node.right_child = BinaryTreeNode(new_mammal)

        messagebox.showinfo("Database Updated", f"{new_mammal} has been added to the game.")

        self.restart_game()

    def restart_game(self):
        self.current_node = self.tree
        self.label.config(text=self.current_node.data)

if __name__ == "__main__":
    app = TwentyQuestionsGUI()
    app.mainloop()
