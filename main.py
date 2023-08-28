import random
from random import sample
import tkinter as tk
from english_words import get_english_words_set
import os.path

timer = 60
init = False
wps_over = False
word_counter = 0
typed_word = ''
words_file = 'words.txt'
root = tk.Tk()

root.title('Words Per minute')
root.geometry('600x400')


def run_word_per_minute(key):
    global typed_word, word_counter
    typed_word += key.char
    label_word = word_challenge.cget('text')

    if typed_word.strip() == label_word.strip():
        word_counter += 1
        typed_word = ''
        new_word = get_random_word()
        word_challenge.config(text=new_word)
        input_area.delete(0, tk.END)


def clear_text():
    global typed_word
    typed_word = ''
    input_area.delete(0, tk.END)


def create_word_library():
    with open(words_file, 'w') as file:
        words_set = []
        words = get_english_words_set(['web2'], lower=True)
        for i, word in enumerate(sample(list(words), 350)):
            words_set.append(word)
        file.write(' '.join(words_set))


def get_random_word():
    with open(words_file) as file:
        words = file.read().split(' ')
    return random.choice(words)


def start_timer():
    global timer, word_counter, init
    if not init:
        word_challenge.config(text=get_random_word())
        input_area.config(state='normal')

    if timer:
        init = True
        minutes, seconds = divmod(timer, 60)
        timer_text = f'{seconds:02d}'
        timer_label.config(text=timer_text)
        timer -= 1
        root.after(1000, start_timer)

    if not timer:
        timer_label.config(text='Done')
        input_area.config(state='disabled')
        word_challenge.config(text=f"Your result: {word_counter}/min")


if not os.path.isfile(words_file):
    create_word_library()

word = get_random_word()

word_challenge = tk.Label(root, text='', font=('Arial', 20, 'bold'))
word_challenge.pack()

input_area = tk.Entry(root, width=50, justify='center', state='disabled')
input_area.pack()
input_area.bind("<KeyRelease>", run_word_per_minute)

start_button = tk.Button(root, width=10, text='Start', command=start_timer)
start_button.pack()

clear_button = tk.Button(root, width=10, text='Clear', command=clear_text)
clear_button.pack()

timer_label = tk.Label(root, text='')
timer_label.pack()

root.mainloop()
