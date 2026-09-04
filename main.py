from pyscript import display
from js import document

display(target="div1")
name = "Name: Ary" #string
age = "Age: 14" #integer
height = "Height: 157 cm" #float
countries = "Countries: Italy, Switzerland, Sweden" #list
student_type = False #boolean
info = "Favorite color: Lilac, | Car Brand: Audi, | Shoe_Size: 5.5, | Bestfriend: Dani"
favorite_fruits = "Favorite Fruits:  Mango, Strawberry, kiwi, grapes, mangosteen" #set
days_of_the_week = "Days: Monday, Tuesday, Wednesday,Thursday, Friday, Saturday, Sunday" #tuple

display(name, target="div1")
display(age, target="div1")
display(countries, target="div1")
display(student_type, target="div1")
display(info, target="div1")
display(favorite_fruits, target="div1")
display(days_of_the_week, target="div1")

def adding_numbers(e):
    input1 = float(document.getElementById("input1").value)
    input2 = float(document.getElementById("input2").value)
    result = input1 + input2
    display(result, target="output1")