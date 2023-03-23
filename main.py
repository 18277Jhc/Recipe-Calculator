'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# Import the required library
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

# Create an instance of tkinter frame and window
win=Tk()
win.geometry("700x300")

name = askstring('Name', 'What is Player name?')
showinfo('Hello!', 'Hi, {}'.format(name))

win.mainloop()
print("Welcome to the Recipe Cost Calculator!\n")
recipe_name = input("Please enter the name of the recipe: ")
serving_size = int(input("Please enter the serving size: "))

# Create an empty list to store ingredients
ingredients = []

# Ask for the ingredient details from the user
while True:
    ingredient_name = input("\nEnter the name of the ingredient (or 'q' to quit): ")
    if ingredient_name == 'q':
        break
    ingredient_amount = float(input("Enter the amount of the ingredient (in grams, milliliters, etc.): "))
    ingredient_cost = float(input("Enter the cost of the ingredient): "))
    ingredients.append({'name': ingredient_name, 'amount': ingredient_amount, 'cost': ingredient_cost})

  
# Calculate the total cost of the recipe
total_cost = 0
for ingredient in ingredients:
    total_cost += (ingredient['amount'] * ingredient['cost'] / ingredient['amount'])

# Calculate the cost per serving
cost_per_serving = total_cost / serving_size

# Print the results
print("\nRecipe Name: ", recipe_name)
print("Serving Size: ", serving_size)
print("Total Cost: $", round(total_cost, 2))
print("Cost per Serving: $", round(cost_per_serving, 2))
