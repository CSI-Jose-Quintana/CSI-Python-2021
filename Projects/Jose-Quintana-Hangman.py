import random
word_list = ["buchipluma", "guasibiri", "glopeta", "acicalao", "masucamba", "sandungueo", "pichaera", "feca", "blinblineo", "banshee" ]

def get_word(word_list):
  word = random.choice(word_list)
  return word.upper()

def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("Let's play Hangman")
  print("Theme: Reggaeton's Words")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess = input("Guess a letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("Your already tried", guess, "!")
      elif guess not in word:
        print(guess, "Isn't in the word :(")
        tries -= 1
        guessed_letters.append(guess)
      else:
        print("Nice one", guess, "is in the word!")
        guessed_letters.append(guess)




def display_hangman(tries):
    stages = [  """
                    --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   / \\
                    -
                    """,
                    """
                     --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   / 
                    -
                    """,
                    """
                     --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   
                    -
                    """,
                    """"
                     --------
                    |    |
                    |    O
                    |   /|
                    |    |
                    |   
                    -
                    """,
                    """
                     --------
                    |    |
                    |    O
                    |    |
                    |    |
                    |   
                    -
                    """,
                    """
                      --------
                    |    |
                    |    O
                    |    
                    |    
                    |   
                    -
                    """,
                    """
                      --------
                    |    |
                    |    
                    |    
                    |    
                    |   
                    -
                    """,
    ]

