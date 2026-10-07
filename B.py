class Flash_Card:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return f"{self.word}({self.meaning})"
dictoi = []
print("Welcome to Flash Card application!")
while True:
    word = input("Enter a word: ")
    meaning = input("Enter the meaning of this word: ")
    flashcard = Flash_Card(word, meaning)
    dictoi.append(flashcard)
    option = input("Would you like to add anoter flash-card? (Y/N)").upper().strip()
    if option == "N":
        break

for i in dictoi:
    print(i, end = ", ")



        