import random

words = ["tree", "ocean", "mountain", "river", "glacier", "waterfall"]
computer_choice = words[random.randint(0, len(words) - 1)]
dashes = list("_"*len(computer_choice))
lives = 0
hangman_stages = [
    r"""  
      ------
      |    
      |    
      |    
      |    
      |    
    =========
    """,
    r"""  
      ------
      |    O  
      |    
      |    
      |    
      |    
    =========
    """,
    r"""  
      ------
      |    O  
      |    |  
      |    
      |    
      |    
    =========
    """,
    r"""  
      ------
      |    O  
      |   /|  
      |    
      |    
      |    
    =========
    """,
    r"""  
      ------
      |    O  
      |   /|\  
      |    
      |    
      |    
    =========
    """,
    r"""  
      ------
      |    O  
      |   /|\  
      |   /    
      |    
      |    
    =========
    """,
    r"""  
      ------
      |    O  
      |   /|\  
      |   / \  
      |    
      |    
    =========
    """
]

print(f"GUESS THE WORD:")


while True:
    if computer_choice!="".join(dashes):
        print("Word: " + "".join(dashes))
        user = input("Enter a letter: ")
        if user in computer_choice:
            for i,char in enumerate(computer_choice):
                if user.lower()==char:
                    dashes[i] = char
        else:
            lives+=1
            print("You have guess the wrong letter!")
            print(hangman_stages[lives])

        if lives==6:
            print("The man has been hanged. You lose!")
            break
    else:
        print(f"You have guessed the word '{computer_choice}' correctly. You won!")
        break