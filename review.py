import tkinter as tk
from tkinter import messagebox
import openai

# Define the function to generate the game review
def generate_review():
    game_name = game_name_entry.get()
    review_type = ''
    
    if positive_var.get() == 1:
        review_type = "positive"
    elif negative_var.get() == 1:
        review_type = "negative"
    
    if game_name == '':
        messagebox.showerror('Error', 'Please enter a game name.')
        return
    
    if review_type == '':
        messagebox.showerror('Error', 'Please select a review type.')
        return
    
    openai.api_key = api_key_entry.get()
    
    prompt = f"I am writing a {review_type} review for the game '{game_name}'. Interpret the following summary for me and write a new, in-detail review from it. Only talk about the parts that are mentioned in the summary: {review_summary_label}"

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    generated_review = response.choices[0].text.strip()
    review_text.delete('1.0', tk.END)
    review_text.insert(tk.END, generated_review)

# Create the main window
window = tk.Tk()
window.title('Game Review Generator')

# Create API key input field
api_key_label = tk.Label(window, text='API Key:')
api_key_label.pack()
api_key_entry = tk.Entry(window, show='*')
api_key_entry.pack()

# Create review summary input field
review_summary_label = tk.Label(window, text='')
review_summary_label.pack()
review_summary_entry = tk.Entry(window)
review_summary_entry.pack()

# Create game name input field
game_name_label = tk.Label(window, text='Game Name:')
game_name_label.pack()
game_name_entry = tk.Entry(window)
game_name_entry.pack()

# Create review type checkboxes
positive_var = tk.IntVar()
positive_checkbox = tk.Checkbutton(window, text='Positive', variable=positive_var)
positive_checkbox.pack()

negative_var = tk.IntVar()
negative_checkbox = tk.Checkbutton(window, text='Negative', variable=negative_var)
negative_checkbox.pack()

# Create generate review button
generate_button = tk.Button(window, text='Generate Review', command=generate_review)
generate_button.pack()

# Create review output field
review_text = tk.Text(window, height=10, width=50)
review_text.pack()

# Start the main loop
window.mainloop()