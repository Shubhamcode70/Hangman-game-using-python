import random
word_list = ["apple", "mango", "orange", "pineapple"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

random_word = random.choice(word_list)
print(random_word)

#replacing the letter with blank list
display = []
for _ in range(len(random_word)):
    display +=  "_"
print(display)

game_over = False
lives = 6
while not game_over:
    user_guess = input("Enter Your Guess : ").lower()
    #replacing the match with the random word letter with guess word letter with user guess input
    #random_word
    #user_guess
    #display

    for random_letter in range (len(random_word)):
        letter = random_word[random_letter]
        if letter == user_guess:
            display[random_letter] = letter
    print(display)
    
    #check for lives | lives out of 5
    if user_guess not in random_word:
        lives = lives - 1
        print(f"{lives} lives remaining")
        if lives == 0:
            game_over = True
            print("You Lost the Game")
    else:
        print(lives)
        
    print(stages[lives])
    
    
    if "_" not in display:
        game_over = True
        print("You Win")
        

    

