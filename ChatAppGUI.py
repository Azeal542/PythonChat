import tkinter as tk
from tkinter import ttk
import ChatApp

class ChatAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        self.mainframe = ttk.Frame(root, padding="10")
        self.mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.chat_display = tk.Text(self.mainframe, height=20, width=50, state='disabled')
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.message_entry = ttk.Entry(self.mainframe, width=40)
        self.message_entry.grid(row=1, column=0, padx=5, pady=5)
        self.message_entry.bind("<Return>", self.send_message)
        self.send_button = ttk.Button(self.mainframe, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=5, pady=5)
        
        self.chat_reload = ttk.Button(self.mainframe, text="Reload", command=self.reload_chat)
        self.chat_reload.grid(row=2, column=1, padx=5, pady=5)

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"[{Username}]: {message}\n")
            message = f"[{Username}]: {message}"
            ChatApp.Chatapp(message)
            self.chat_display.config(state='disabled')
            self.message_entry.delete(0, tk.END)
            #data = ChatApp.Receive(Username)
            #self.chat_display.config(state='normal')
            #self.chat_display.insert(tk.END, str(data))
            #self.chat_display.config(state='disabled')

    def reload_chat(self, event=None):
        data = ChatApp.Receive()
        self.chat_display.config(state='normal')
        self.chat_display.delete('1.0', tk.END)
        self.chat_display.insert(tk.END, str(data))
        self.chat_display.config(state='disabled')

class Setup:
    def __init__(self, root):
        self.root = root
        self.root.title("Setup")

        self.mainframe = ttk.Frame(root, padding="10")
        self.mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.chat_display = tk.Text(self.mainframe, height=20, width=50, state='disabled')
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.message_entry = ttk.Entry(self.mainframe, width=40)
        self.message_entry.grid(row=1, column=0, padx=5, pady=5)
        self.message_entry.bind("<Return>", self.initial_setup)
        self.send_button = ttk.Button(self.mainframe, text="Set", command=self.initial_setup)
        self.send_button.grid(row=1, column=1, padx=5, pady=5)

        self.chat_display.config(state='normal')
        self.chat_display.delete('1.0', tk.END)
        self.chat_display.insert(tk.END, "Welcome to Chat App!\n")
        self.chat_display.insert(tk.END, "Please enter your username and press enter\nto start chatting.\n")

    def initial_setup(self, event=None):
        global Username
        Username = self.message_entry.get()
        if Username:
            ChatAppGUI(root)
        else:
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, "Please enter a username.\n")
            self.chat_display.config(state='disabled')
        #username = self.message_entry.get()
        self.chat_display.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    Setup(root)
    root.mainloop()