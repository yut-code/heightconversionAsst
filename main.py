# Module 4 Height Conversion Assignment
# Teresa Yu
# This program will convert a user-inputted height from imperial to metric units

# import everything needed from Tkinter
from tkinter import *
from tkinter import messagebox

# creating a window named with the title 'Height Converter' 
window = Tk()
window.title('Height Convertor')

# creating label widgets to show text in the window
# first we want to greet the user and ask that their height is
welcomeLabel = Label(window, text="Welcome to the Height Convertor!", fg='#d89eff', font=("Hevetica 18 bold"))
question = Label(window, text="What's your height?", font="bold")
feetLabel = Label(window, text="Feet: ")
inchesLabel = Label(window, text="Inches: ")

# creating entry widgets so the user can type in their height
feetEntered = Entry(window, width=5)
inchesEntered = Entry(window, width=5)

# defining command when Calculate Button is clicked. This function first takes the information in the entry widgets using the get() method. We must typecast into a float (for most accuracy) due to how the get() function returns the information as a string. 
def convertHeight():
  feet = float(feetEntered.get())
  inches = float(inchesEntered.get())
  # To calculate from imperial to metric units, we must multiply the total number of inches by 2.54cm. If the calculated height has more than 2 decimal places, it will be rounded to the nearest hundreth. In order to concatenate the metric height, it must be typecasted into a string.
  totalInches = feet*12+inches
  metricHeight = str(round(totalInches*2.54,2))
  # show a message saying 'You are __ cm'
  messagebox.showinfo(message='You are '+ metricHeight + ' cm')

# creating a button for the user to click to calculate convert their height into cm
# the button is purple with white text. when hovered, the button will turn white and the text will turn black by default
calculateButton = Button(text='Calculate cm', command=convertHeight, bg='#d89eff', fg='white', padx= 10, pady=12)

# display and arrage the label, entry and button widgets on the screen using the grid() method. 
# rows are horizontal sections, and columns are vertical sections of the window
# columnspan means the widget takes up n columns, in this case it is 2
# sticky is the which side/direction of the section the widget 'sticks to'
# pady is how many pixels to pad vertically outside the section's borders
welcomeLabel.grid(row = 0, columnspan=2)
question.grid(row = 1, columnspan = 2, pady = 5)

feetLabel.grid(row = 2, column = 0, sticky = E)
feetEntered.grid(row = 2, column = 1, sticky = W)

inchesLabel.grid(row = 3, column = 0, sticky = E)
inchesEntered.grid(row = 3, column = 1, sticky = W)

calculateButton.grid(row = 4, pady = 10, columnspan=2)

# program will loop until the user closes the window
window.mainloop()

