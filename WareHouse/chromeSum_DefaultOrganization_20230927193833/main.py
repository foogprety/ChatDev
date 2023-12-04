'''
This is the main file of the chrome extension app.
'''
import tkinter as tk
import requests
import openai
from openai_helper import summarize_article
class ChromeExtensionApp:
    def __init__(self):
        self.api_key = ""
        self.window = tk.Tk()
        self.window.title("Chrome Extension App")
        self.api_key_label = tk.Label(self.window, text="API Key:")
        self.api_key_label.pack()
        self.api_key_entry = tk.Entry(self.window)
        self.api_key_entry.pack()
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_api_key)
        self.submit_button.pack()
        self.window.mainloop()
    def submit_api_key(self):
        self.api_key = self.api_key_entry.get()
        self.window.destroy()
        self.summarize_article()
    def summarize_article(self):
        article = "Sample article"  # Replace with the actual article content
        summary = summarize_article(self.api_key, article)
        # Implement the logic to display the summary to the user
        print(summary)  # Example: Print the summary to the console
if __name__ == "__main__":
    app = ChromeExtensionApp()