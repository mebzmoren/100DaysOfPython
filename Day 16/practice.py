# #object oriented programming
# import turtle               #imported module
# timmy = turtle.Turtle()     #fetched a class
# print(timmy)                #prints loction where object is saved
# timmy.shape("turtle")       #changes shape of the object
# timmy.color("red", "green") #changes color
# timmy.forward(100)          #moves turtle forward
# my_screen = turtle.Screen() #window where the turtle will show up
# print(my_screen.canvheight) #object.attribute(data), prints the hight of the canvass
# my_screen.exitonclick()     #allows the program to run until click has been detected

#modifying object attributes & calling methpds
import prettytable                                                  #import module
table = prettytable.PrettyTable()                                   #fetched a class
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])  #Creates a column with rows
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "l"                                                   #accesses an attribute/field, aligns the whole table
print(table)                                                        #prints the table