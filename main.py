#print("Hello World")
import random
from tkinter import N

trip_destination=["Hawaii", "Texas", "Mars", "Fuji"]
resturants=["Wendys", "McDonalds", "Subway", "Moes"]
transportation=["Tricycle", "Car", "Bus", "Train"]
entertainment=["Movies", "Shopping", "Bowling", "Rafting"]



my_dictionary={ "Destination":"destination", "Food": "food", "Ride": "ride", "Fun": "fun"}

destination=(random.choice(trip_destination))
food=(random.choice(resturants))
ride=(random.choice(transportation))
fun=(random.choice(entertainment))


introduction= "Welcome to Day Trip Generator"
print(introduction)
print("")


def trip_place():

    print(f"How does {destination} sound for your trip?")

    choice=input("Would you like to go there? Y/N " )

    if choice ==("Y"): 
        print(f"Awesome {destination} sounds fun")
    
    elif choice==("N"):
          print("Lets try again.")
        
           
    else:
        print ("Please Type Captial Y or N.")
        


trip_place()

def trip_food():

    print(f"Do you like to eat {food}? " )
    choice=input("Would you like to eat there? Y/N " )

    if choice ==("Y"): 
        print(f"Awesome {food} sounds great")
    elif choice==("N"):
        print("Lets try again.")
           
    else:
        print ("Please Type Captial Y or N.")

trip_food()

def trip_ride():
    print(f"How about using a {ride} to get around?")
    choice=input("Would you like to use that? Y/N " )

    if choice ==("Y"): 
        print(f"Awesome a {ride} sounds fun")
    elif choice==("N"):
        print("Lets try again.")
           
    else:
        print ("Please Type Captial Y or N.")

trip_ride()

def trip_fun():
    print(f"How about {fun} for some fun?")
    choice=input("Would you like to do that? Y/N " )

    if choice ==("Y"): 
        print(f"Awesome {fun} sounds fun")
    elif choice==("N"):
        print("Lets try again.")
           
    else:
        print ("Please Type Captial Y or N.")

trip_fun()

def run():
    trip_place()
    trip_food()
    trip_ride()
    trip_fun()

run()

#make the run stop!!!!
#make a statement that holds all of the answers 
#how to loop if they say N
# have user say this trip is complete
def satisfied_trip():
    print(f"So you are going to {trip_destination},eating {trip_food},while using {trip_ride,} and going {trip_fun}./n Have a great time")
    ask_user=input ("Do you like this trip?" )

    if ask_user==("Y" ):
             print( "Have a great time.")
    elif ask_user==("N" ):
            print("Lets take it from the top!")
satisfied_trip()