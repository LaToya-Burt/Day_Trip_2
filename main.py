#print("Hello World")
import random


trip_destination=["Hawaii", "Texas", "Mars", "Fuji"]
resturants=["Wendys", "McDonalds", "Subway", "Moes"]
transportation=["Tricycle", "Car", "Bus", "Train"]
entertainment=["Movies", "Shopping", "Bowling", "Rafting"]



my_dictionary={ "Destination":random.choice(trip_destination), 
"Food":random.choice(resturants), 
"Ride" : random.choice(transportation), 
"Fun": random.choice(entertainment)}

destination=(random.choice(trip_destination))
food=(random.choice(resturants))
ride=(random.choice(transportation))
fun=(random.choice(entertainment))


introduction= "Welcome to Day Trip Generator"
print(introduction)
print("")


    
    
def trip_place():
    while True:
        print(f"How does {random.choice(trip_destination)} sound for your trip?")

        choice=input("Would you like to go there? Y/N " )


        if choice =="Y": 
         print (f"Awesome {my_dictionary['Destination']} sounds fun")
         break

        elif choice==("N"):
            print("Lets try again.")   
            my_dictionary["Destination"]= random.choice(trip_destination)  
        else:
            print ("Please Type Captial Y or N.")
        


def trip_food():
    while True:
     print(f"Do you like to eat {random.choice(resturants)}? " )
     choice=input("Would you like to eat there? Y/N " )

     if choice =="Y": 
        print(f"Awesome {my_dictionary['Food']} sounds great")
        break

     elif choice==("N"):
        print("Lets try again.")
        my_dictionary["Food"]=random.choice(resturants)
     else:
        print("Please Type Captial Y or N.")    
    



def trip_ride():
    while True:
        print(f"How about using a {random.choice(transportation)} to get around?")
        choice=input("Would you like to use that? Y/N " )
    
        if choice =="Y": 
           print(f"Awesome a {my_dictionary ['Ride']} sounds fun")
           break

        elif choice=="N":
         print("Lets try again.")
         my_dictionary["Ride"]=random.choice(transportation)
           
        else:
          print ("Please Type Captial Y or N.")



def trip_fun():
    while True:
        print(f"How about {random.choice(entertainment)} for some fun?")
        choice=input("Would you like to do that? Y/N " )

        if choice =="Y": 
            print(f"Awesome {my_dictionary['Fun']} sounds fun")
            break
        elif choice=="N":
            print("Lets try again.")
            my_dictionary["Fun"]= random.choice(entertainment)
           
        else:
            print ("Please Type Captial Y or N.")



def run():
    trip_place()
    trip_food()
    trip_ride()
    trip_fun()

run()

def satisfied_trip():
    while True: 

        print(f"So you are going to {random.choice(trip_destination)},eating {random.choice(resturants)},while using {random.choice(transportation)}, and going {random.choice(entertainment)}.")
        ask_user=input ("Do you like this trip?" )

        if ask_user== "Y" :
             print( "Have a great time.")
             break
        elif ask_user=="N":
            print("Lets take it from the top!")
            
            trip_place()
        else:
            print('Please Use Capital Y/N')  

satisfied_trip()
