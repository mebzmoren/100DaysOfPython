#creating class
class User:
    def __init__(self):                                                         #constructor, initialize attributes
        print("creating user...")
class Car:
    def __init__(self, seats):
        print("creating car...")
        self.seats = seats                                                       #to create an attribute      
        print("entering race mode...")
        self.seats = 2
class UserNew:                                                                  #another way of writing
    def __init__(self, user_id, name):                         
        print("creating user...")
        self.id = user_id
        self.name = name
        self.followers = 0                                                      #can have a default value instead of it being passes as a parameter
        self.following = 0
    def follow(self, user):
        print("following...")
        user.followers += 1
        self.following += 1
user_1 = User()
user_1.id = "01"
user_1.name = "hi"
print(f"ID: {user_1.id} Name: {user_1.name}\n")
user_2 = User()
user_2.id = "02"
user_2.name = "hello"
print(f"ID: {user_2.id} Name: {user_2.name}\n")
car = Car(5)                                                                    #initializes number of seats
print(f"Number of seats: {car.seats}\n")
car.race_mode()
print(f"Number of seats: {car.seats}\n")
user_3 = UserNew("03", "good, day")
print(f"ID: {user_3.id} Name: {user_3.name} Followers: {user_3.followers} Following: {user_3.following}\n")
user_4 = UserNew("04", "good, night")
print(f"ID: {user_4.id} Name: {user_4.name} Followers: {user_4.followers} Following: {user_4.following}\n")
user_3.follow(user_4)
print(f"ID: {user_3.id} Name: {user_3.name} Followers: {user_3.followers} Following: {user_3.following}")
print(f"ID: {user_4.id} Name: {user_4.name} Followers: {user_4.followers} Following: {user_4.following}\n")