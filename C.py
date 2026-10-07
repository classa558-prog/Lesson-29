import random
class Fruit_Quiz:
    dictoi = {"Apple":"Red", 
              "Orange":"Orange",
              "Agrim":"Peach",
              "Peach":"Peach"}
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.dictoi.items()))
            inputoi = input(f"What is the color of {fruit}? ").strip().capitalize()
            if inputoi == color:
                print("Right answer")
            else:
                print("Wrong answer")
            user_play = input("Would you like to play again? (1/0)").strip()
            if user_play == "0":
                print("Bye!")
                break
print("Welcome to the Fruit_Quiz! ")
obj = Fruit_Quiz()
obj.quiz()
                
    
   