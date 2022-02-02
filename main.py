#importing all necessary libraries
import pyjokes
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#creating widgets
def CreateWidgets():
	readyLabel =Label(root, text = "Get Ready to Laugh with PyJokes", bg = "darkolivegreen")
	readyLabel.grid(row = 1, column = 1, padx = 5, pady = 8)
	
	#defining the next-joke button
	jokeButton = Button(root, text = "Next Joke", width = 12, command = getJoke, bg="lime")
	jokeButton.grid(row = 3, column = 1, padx = 5, pady = 8)
	root.jokeText = Text(root, width = 40, height = 10, bg = "green", wrap = "word")
	root.jokeText.grid(row = 4, column = 0, columnspan = 3, padx = 5, pady = 5)
	root.jokeText.config(state = DISABLED)

def getJoke(): # defining function which fetches the joke
	try:
		#choosing the language
		joke = pyjokes.get_joke(language = "en", category = "all")
		root.jokeText.config(state = NORMAL)
		root.jokeText.delete(0.0, END) # delete old joke from joke-box when next-joke button is clicked
		root.jokeText.insert(0.0, joke)# insert new joke
		root.jokeText.config(state = DISABLED) #this makes it possible for the joke text box to remain unedited
		#the exception creates a messagebox incase pyjokes couldn't be accessed 
	except Exception as e:
		messagebox.showerror("❌ERROR❌", e)
		messagebox.showinfo("Could not access the jokes")

root = tk.Tk() #creates the window

root.geometry("334x254") #setting window geo
root.title("Python For Laughs") #title
root.config(bg = "darkolivegreen") #background
root.minsize(334,254)
root.maxsize(334,254)
icon = PhotoImage(file = 'PyJokes.png') #importing icon
root.iconphoto(False, icon)

language = StringVar()
category = StringVar()

CreateWidgets()

#keeps the window running
root.mainloop()