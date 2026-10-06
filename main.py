from pyscript import document, display

display(target="div1") #literal object

#variable objects
name = "Aryana Cassandra E. Vargas" #string 
age = 14 #int 
height1 = 157.48 #float 
dream_destination = ["Italy", "Switzerland", "Sweden"] #list 
student_type = True #boolean
preferences = {"color" : "lilac",
     "car_brand" : "Ferrari",
     "shoe_size" : "6",
     "best_friend" : "Imee Anika Marc Villenueva Mallari"
} #dictionary 
favorite_fruits = {"Mango", 
"Strawberry", 
"Peach"
} #set 
daysoftheweek = ("Monday", 
"Tuesday", 
"Wednesday", 
"Thursday", 
"Friday", 
"Saturday", 
"Sunday"
) #tuple 

display("Who am I: " + name, target="div1")
display("How old am I: " + str(age), target="div1")
display("How tall am I(cm): " + str(height1), target="div1")
display("Where I'd like to go: " + str(dream_destination), target="div1")
display("Student Type: " + str(student_type), target="div1")
display("What I like: " + str(preferences), target="div1")
display("My Favorite Fruits: " + str(favorite_fruits), target="div1")
display("What are the Days of the Week: " + str(daysoftheweek), target="div1")

def adding_numbers(e):
    document.getElementById("div2").innerHTML = "" # clears previous output
    num1 = float(document.getElementById('input1').value) # get 1st input
    num2 = float(document.getElementById('input2').value) # get 2nd input
    result = num1 + num2 #use operator to compute/add
    display(result, target = "div2") #display output in div