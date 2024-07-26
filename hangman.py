word = input('enter a word for p2 to guess: ')

max_guess = len(word)
wrong_guess = len(word) * 2 - 1

# i is the controller of the iteration through word
i = 0

#you have to keep this here because otherwise the saved list will reset
string_holder = []
string_holder.extend('_' * len(word))

print(f'you have {len(word)} letters to guess')

# iterate for each letter in the word
# i here is counting each iteration for each char in the word
# while wrong_guess < max_guess - 1 :
while wrong_guess >= max_guess and i < max_guess:
  # while :


    user_char = input('Enter a guess: ')

    #check if user inputed charachter is equal to pos of correct word
    # but if you get one wrong it needs to remeber pos of word
    # here i will not count up towards main while loop and will iterate as long ase
    # i is less than max_guess
    if user_char == word[i]:
      # need function to replace letters in string
      string_holder[i] = user_char
      i += 1
      print('correct_guess', string_holder)

    else:
      # this reset pos in word check if you get incorrect
      wrong_guess -= 1
      print(string_holder)

      # we correcting math here
      if wrong_guess - len(word) + 1 == 0:
        print(f'eeer.  no more guesses left.  word was {word}')
      else:
        print(f'incorrect, you have {wrong_guess - len(word) + 1} guesses left')
        print('try again\n')


