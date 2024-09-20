import sys
from tkinter import *
from tkinter import messagebox
import random


guess = random.randint(1, 100)
guessLives = 10
guesses = 1
def click():
    global guessLives
    try:
        choice = int(entry.get())
    except ValueError:
        messagebox.showerror(title="Invalid", message=f"'{entry.get()}' is not an Integer!")
    else:
        global guesses
        if choice > 100 or choice < 1:
            messagebox.showerror(title="Invalid Input", message="Please, enter only a number between 1 and 100")
        elif guessLives == 1:
            jumpscare()
        elif guessLives < 0:
            sys.exit()
        elif choice < guess:
            guessLives -= 1
            guesses += 1
            match guessLives:

                case 9:
                    label7.config(text="Very Low, try again human")
                case 8:
                    label7.config(text="Too Low, Go try again")
                case 7:
                    label7.config(text="Your Guess is Low, Human!")
                case 6:
                    label7.config(text="Too Low, Try Again!")
                case 5:
                    label7.config(text="Too Low!")
                case 4:
                    label7.config(text="Still Low, your luck is running out")
                case 3:
                    label7.config(text="Your guess is Loooowwwwwwwww!!!")
                case 2:
                    label7.config(text="Low! Imma bout to Eat you ")
                case 1:
                    label7.config(text="Still Low, Hide Now!")
        elif choice > guess:
            guessLives -= 1
            guesses += 1
            match guessLives:
                case 9:
                    label7.config(text="Very High, try again human")
                case 8:
                    label7.config(text="Too High, Just try")
                case 7:
                    label7.config(text="Your Guess is High, Human!")
                case 6:
                    label7.config(text="Too High, Try Again!")
                case 5:
                    label7.config(text="Too High!")
                case 4:
                    label7.config(text="Still High, your luck is running out")
                case 3:
                    label7.config(text="Your guess is Highhhh!!!")
                case 2:
                    label7.config(text="High! Imma bout to Eat you ")
                case 1:
                    label7.config(text="Still High, Hide Now!")

        elif choice == guess:
            messagebox.showinfo(title="Congrats", message=f"You have Survived in just {guesses} attempts")
            sys.exit()
        label6.config(text=f"Chances: {guessLives}")

def leave():
    sys.exit()
def jumpscare():
    jumpscarewindow = Tk()
    jumpscarewindow.geometry('200x200')
    jumpscarewindow.attributes('-fullscreen', True)
    jumpscarewindow.config(background='black')

    label = Label(jumpscarewindow,font=('Arial',15,'bold') ,background='black', foreground='red' ,text="""               
             ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⠀            ⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣖⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠟⠻⠿⠩⠓⠛⠉⠛⠩⠝⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⡭⢍⠓⡙⠃⠃⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⢄⠉⠃⠉⢽⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡽⣷⣿⣿⣿⠙⠆⠱⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠈⢉⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⣞⣯⢟⡧⢿⣿⣄⠣⠈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠐⠀⡀⠀⠀⠐⢠⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡞⣧⢻⡜⣮⢻⣼⣿⣿⠡⠄⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⠀⠀⠃⠀⠀⠀⠀⠀⠈⠘⢹⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠳⢮⡙⣎⣧⢻⢼⣻⣟⣿⡏⠐⠄⡐⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⣞⣏⢧⡹⢮⡝⣿⣿⣿⣿⠛⠀⠀⠄⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⡀⢧⡿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⢽⣧⡟⣾⣹⢧⡟⣿⢺⣽⡿⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡧⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⢎⣿⢾⡿⣱⣿⣧⡿⠾⠟⢁⠂⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡗⣧⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⢿⣾⣟⣿⣿⣿⠿⡐⠌⡌⠀⡀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⣷⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⣯⣿⣳⡽⣞⣿⣯⣷⡐⢈⠰⢀⠁⠀⠠⠐⡈⠄⠠⢀⠐⠈⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⢀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣳⢯⣷⣻⣿⣿⣿⣿⣿⣿⣶⣧⣌⢠⠑⣠⠂⠜⡐⢠⠈⢂⠡⠀⠌⠀⡐⢀⡀⢀⠢⢀⠚⢒⣲⣶⣿⣿⣷⣿⣿⣿⣿⣷⣶⣀⠀⠀⠀⠚⢿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡿⣽⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡥⢧⡌⣃⠆⠡⢂⠰⣐⡎⠽⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠆⠀⠘⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠿⣧⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⢿⣳⢞⡶⣭⣧⣈⣼⣃⣯⡟⣽⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⡿⢂⣀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡿⢯⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡽⣟⣾⣿⠆⠡⢼⣿⣿⣟⡶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠿⢿⣿⣿⣿⣿⡾⢍⠆⠀⠀⢸⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣟⢧⣻⣽⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⠀⠀⠈⢹⣿⣯⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣶⣸⣿⣿⣿⣿⣯⣍⣰⣶⣿⢹⣿⣿⣿⠻⠿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡿⣜⣣⢏⡿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢂⠄⣂⣃⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠿⠈⢉⣤⣉⡹⠛⠉⠉⠶⠂⠸⣿⣿⣿⡻⣝⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⣴⣯⢿⣽⣿⣯⣿⣻⡟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⣈⠂⠀⣨⡄⠀⡏⠒⣿⣿⣿⣿⣿⣿⣽⣿⣭⣤⣤⣶⣶⢿⠋⣭⠹⢿⣶⣶⡔⢶⣾⣿⣿⣿⣿⢎⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⡼⣯⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⠀⡐⠉⢀⠘⡜⢡⠀⡉⠏⡉⢉⠍⣙⢫⡝⣻⢛⣻⠰⠀⠀⠀⢀⠀⠚⣿⣷⣥⠘⣿⣿⣿⣾⡋⢼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡿⣵⣳⡻⣵⢏⡿⢿⡿⠿⣿⣿⣿⡿⢟⠫⢖⣹⣿⣿⣟⣿⣿⢜⡢⠐⠂⢀⠴⡡⢂⠂⡁⠒⡰⢠⠚⣤⢣⠚⡥⢓⢌⠂⡉⡄⠀⠀⠀⠀⠈⠹⣿⣷⣸⣿⣿⣾⠍⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⢶⣯⠷⡭⠞⡤⢁⠀⠀⢀⠀⠂⡔⡌⠳⣌⣾⣿⣳⢿⣳⣿⢺⠅⠄⠀⠸⢄⠡⢂⡅⠂⠡⣀⠡⡉⠤⢩⠙⡰⣩⣘⣲⡄⠐⡀⠀⠀⠀⠀⢢⠘⢻⣽⣶⣿⠍⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣟⡾⣹⡱⢋⡔⢠⠠⣁⠢⢌⣲⠴⣭⣳⣶⢿⣳⣿⣻⣗⡟⣌⠛⡀⠀⠁⠀⢎⡒⡴⠁⠡⠘⢲⣷⣷⣷⣾⣤⣥⣤⣈⠀⢄⠰⢡⠤⠠⡤⠀⢻⡆⢻⡧⠃⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡝⣾⡱⣍⠧⡘⢆⠲⣤⢷⣯⣼⣿⢷⣻⣭⣳⡽⣿⣻⡽⡚⢄⠫⠥⠐⢀⠈⠤⠡⢑⠂⠃⡁⢊⡷⢉⠻⣿⣿⣿⣿⣿⣿⡦⡝⢦⢚⣋⡵⣷⣸⣷⢹⠓⠀⠀⠀⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⣽⢣⡟⣬⣳⣹⣮⣷⣿⣿⣿⡿⣯⡿⣽⣳⢟⣾⣻⣽⢣⡏⢸⠐⢢⠁⡦⠂⢁⡑⣈⠆⡱⣘⣼⠃⠌⡒⡹⢌⡟⣿⣿⣿⣿⣽⣯⢶⡏⠈⣿⣧⣹⣼⣷⡀⢤⡬⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⣿⣗⡿⣼⣻⣵⣷⣿⣿⣿⣿⣿⣽⡷⣿⣯⢿⣞⣧⣟⣾⢧⣟⣈⠛⢢⠏⡐⣄⣶⣶⣷⣾⡗⢻⠁⠂⡐⢡⠱⣉⠞⣵⢺⣿⣿⣿⣿⣿⣿⣦⠼⣿⣯⣧⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢯⣿⣻⣷⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⢷⣿⣟⣯⣿⣾⣿⣿⣿⣿⣶⣷⣾⣽⣿⣿⣿⠻⢛⡑⢢⠘⣀⠢⣁⣳⣬⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣳⢿⣻⣯⣿⣾⣿⣿⣿⣟⡾⣵⣿⣿⢿⣋⠓⢢⡘⣤⣼⣤⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⡇⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣯⣿⣿⢻⡏⡻⢿⣟⣿⣿⣿⣿⣿⣿⣯⣟⣷⣻⣟⣷⣿⣾⡿⣿⢿⣛⣩⣴⣤⣿⣶⣿⣿⣾⡿⢿⣿⣟⣿⣿⣿⣿⡿⣿⣿⣿⡿⠽⠬⣷⢿⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣎⣿⣧⢻⣞⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣷⢿⣜⣧⣛⣧⣯⣽⣾⡾⣟⣿⠉⠰⡿⠟⡏⢹⣿⣿⠋⠴⡵⢯⣿⠻⢾⣹⡟⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡼⣿⣬⢿⣿⣿⣿⣿⣿⡍⠙⠓⠻⣿⠛⢻⡿⠿⠿⠿⢿⡿⠛⠛⠻⡏⠂⠻⠛⠀⠀⠃⠀⣡⣿⡿⣃⠜⡢⢇⣽⡟⠬⣣⣿⣻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣿⢿⣷⣏⢿⣧⢿⣿⣿⣿⣿⣿⡄⠀⠀⠁⠀⠘⠇⠀⠀⠀⢸⠁⠀⠀⠀⠃⠀⠀⠀⠀⠀⢄⣴⣿⣿⣓⠩⣰⢫⣿⣿⠩⣸⣟⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣯⣿⣘⣿⡞⣿⣟⣿⣿⣿⣿⣿⣄⣀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⣀⣀⣤⣠⣴⣿⣿⣛⣧⡇⠘⢄⡆⣿⠛⢤⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣎⢿⣧⣿⡾⣽⣿⣿⣿⣿⣿⣿⣿⣧⣄⣀⣀⣠⣤⣤⣤⣤⣾⡿⣿⡟⠿⠤⣼⢳⣻⣾⠳⠓⠨⣾⠟⣻⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⡞⣿⡾⣟⣷⣻⣿⣿⣿⣿⣿⡛⠻⠿⠿⢿⣿⣿⠿⡿⠟⠿⠇⠈⠁⢀⡐⣎⣿⡟⠠⠁⠀⠠⡿⢿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣞⣷⣿⣞⣿⣟⣿⣿⣿⣟⡿⣿⡠⢤⣀⠈⠄⡀⡀⠀⠤⢦⢀⡭⣉⣗⡿⢿⠀⠄⡀⣀⢸⠡⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣿⣿⣿⣿⣿⣿⡾⣟⡿⣞⣿⢿⣝⠻⢿⣿⣯⣷⣏⣟⣿⣛⣟⣛⣽⡹⣜⣮⣼⠽⠋⠔⢠⠎⠔⡁⢠⠇⠷⣿⢟⣛⢋⠻⣤⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣾⣿⠿⣿⣟⢾⣻⣿⣿⣿⣿⣿⣿⢻⡽⣾⢿⣻⢿⢦⡙⡜⣣⢛⡛⠜⡹⢘⠣⢦⠕⠁⡂⠐⠈⠀⡰⠃⢠⠀⡆⠋⣘⣿⣏⠜⠠⠉⡀⢻⣿⣶⡉⠒⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿⡿⣟⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡽⣚⣯⢿⣺⡹⡜⣡⠳⣌⠳⢌⣣⡝⡱⢊⡱⠀⢢⢘⣀⠤⢤⠊⠠⢁⣊⣸⣿⡗⠨⢁⠐⠠⢸⣿⣛⠛⠣⠶⣀⣈⠑⠂⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⡿⢿⣽⣿⣿⣟⡞⣦⣳⣿⣿⢿⠾⣿⣿⣿⣿⣿⣿⣷⡏⡷⣻⢲⡕⢧⢡⠣⠤⡉⠷⢦⢏⡑⠢⡍⠇⠐⠸⠀⢆⡞⢀⡜⣵⣿⣿⣾⣅⠳⡠⠀⠁⢘⣿⣯⠀⠀⠀⠀⠈⠙⠷⢳⣒⣆⡙⡒⠄⢀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢯⣟⡿⣼⣿⣿⣽⣚⢶⣹⣿⠿⣩⣿⣿⣿⢿⣻⣿⣿⣿⣷⢣⢛⠻⣜⡆⢫⢐⠃⢱⠈⡅⣋⣰⠡⠇⠀⠘⠀⠀⡎⢀⡾⣶⣿⣿⢿⣿⣿⣿⡴⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠣⠿⢍⣛⠳⢄⣀⠀⠀⠀⠀
⢾⣿⣿⣳⣶⣷⣶⣿⣿⣿⣏⣿⣿⣿⣿⡿⣽⣻⣿⢿⣾⣿⣿⣷⡭⣷⣹⣷⣟⣿⣿⣿⣻⡿⣿⢿⣿⣿⣿⣏⡾⡱⡸⠜⣂⠆⢎⠠⠒⠠⡀⢀⠀⢀⠀⡐⠀⠌⣡⣾⣽⣿⡟⣿⣇⠸⣿⣿⣿⣄⡆⢸⣿⠷⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣻⣷⣤⣀⡀
⣸⣿⣾⣿⣿⣿⣿⣿⣿⡞⡵⣿⣿⣿⣿⣽⣷⢫⡟⡼⣻⣾⣿⣿⡽⣯⣽⣿⣿⣿⣿⣟⣿⣽⡿⣿⣽⣻⣿⣿⣿⢾⡱⣊⢔⠪⢄⠣⡈⠡⠐⠂⠌⢠⠏⠥⢞⣗⣳⣿⣿⠯⡝⡼⡧⠄⠀⣿⣿⣿⣿⣦⣈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣟⡿⣽⡳⣿⣿⣿⣿⢾⡭⣟⡟⡼⣹⣿⣿⣿⠼⣯⣟⣿⣿⣿⣿⣟⣿⣾⣻⣽⣞⡷⣿⣿⣿⣿⣷⣷⢬⠚⡤⠒⡄⠣⣝⡶⠬⢶⢶⣿⣿⣿⣿⣿⢧⡉⡗⣘⢻⡁⢂⠀⠘⠿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹
⣿⣿⣿⣿⣿⣿⣷⣿⣽⣟⡷⣽⣻⣿⣯⣟⢾⣭⣛⡜⣽⣿⣿⣿⣿⣳⢯⣿⣿⣿⣷⣿⣯⣿⣻⢷⣯⣟⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣿⣶⣿⣿⣿⣿⡿⣿⢢⠑⣬⣤⢻⠁⠀⠀⠐⢲⡞⠀⠀⡀⡀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠀""")
    label.pack()
    labelText = Label(jumpscarewindow, text= "The correct number is:", foreground='white', background='black', font=("Papyrus", 25, 'bold'))
    labelText.place(x=20, y=20)
    labelText2 = Label(jumpscarewindow, text=f"{guess}", foreground='white', background='black',
                      font=("Papyrus", 50, 'bold'))
    labelText2.place(x=130, y=80)

    button = Button(jumpscarewindow, text="EXIT", foreground='white', background='black', font=("Arial",15,'bold'), command=leave)
    button.place(x=1820, y=1000)

    jumpscarewindow.mainloop()



windows = Tk()

windows.title("Case Study")
windows.config(bg='black')
windows.geometry('250x250')
windows.attributes('-fullscreen', True)

label = Label(windows, text="Guess a number between 1 and 100",
              font=('Lucida Console', 20,'bold'),
              bg='black',
              fg='red'
              )
label.place(x=680, y=640)

label1 = Label(windows, text="G u  es s",
              font=('Papyrus',46,'bold'),
              relief=SUNKEN,
              bd=2,
              padx=5,
              pady=2,
               bg='Red'
              )
label1.place(x=620, y=120)
label2 = Label(windows, text="NUMBER",
              font=('Papyrus',52,'bold'),
              relief=SUNKEN,
              bd=2,
              padx=5,
              pady=2,
               bg='#FF0000'
              )
label2.place(x=1000, y=255)
label3 = Label(windows, text="t   h   e",
              font=('Lucida Handwriting',26,'bold'),
              relief=RAISED,
              bd=2,
              padx=5,
              pady=2
              )
label3.place(x=860, y=220)
label4 = Label(windows, text="Horror Version",
              font=('Lucida Handwriting',10,'bold'),
              relief=RAISED,
              bd=2,
              padx=5,
              pady=2
              )
label4.place(x=1360, y=360)
entry = Entry(windows,
              font=('Arial', 20, 'bold'),
              foreground='black',
              background='white',
              width=8
              )
entry.place(x=890, y=700)
label5 = Label(windows, text="to LIVE or  to DIE!",
              font=('Papyrus', 30,'bold'),
              bg='black',
              fg='red'
              )
label5.place(x=770, y=550)
label6 = Label(windows, text=f"Chances: {guessLives}",
              font=('Papyrus',20,'bold'),
               bg='black',
               fg='white'
              )
label6.place(x=50, y=500)
label7 = Label(windows, text="",
              font=('Papyrus',32,'bold'),
               bg='black',
               fg='white'
              )
label7.place(x=740, y=860)
buttons = Button(windows,
                 text='GUESS',
                 font=("Arial Rounded MT Bold", 10, "bold"),
                 relief=RAISED,
                 bd=3,
                 pady=10,
                 padx=20,
                 fg='black',
                 bg='#C0C0C0',
                 activebackground='red',
                 activeforeground='black',
                 command=click
                 )
buttons.place(x=900, y=780)


windows.mainloop()
