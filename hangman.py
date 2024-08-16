
word = input('enter a word for p2 to guess: ')

max_guess = len(word)
wrong_guess = len(word) * 2 - 1

# i is the controller of the iteration through word
i = 0

#you have to keep this here because otherwise the saved list will reset
string_holder = []
string_holder.extend('_' * len(word))

print(type(word))
print(f'you have {len(word)} letters to guess')

# iterate for each letter in the word
# i here is counting each iteration for each char in the word
# while wrong_guess < max_guess - 1 :
while wrong_guess >= max_guess and i < max_guess:
  # while :

    user_char = input('Enter a letter: ')
    # fist check for duplicate values in the string_holder
    if (user_char.lower()) in string_holder:
        print('you have already guessed that')


    # check for correct values and replace any instance of a correct char
    elif (user_char.lower()) in word:
      for letter in range(len(word)):
        if word[letter] == user_char:
            string_holder[letter] = user_char
      i += 1
      print('correct_guess', string_holder)

    # this reset pos in word check if you get incorrect
    else:
      wrong_guess -= 1
      if wrong_guess - len(word) + 1 == 0:
        print(f'eeer.  no more guesses left.  word was {word}')
      else:
        print(f'incorrect, you have {wrong_guess - len(word) + 1} guesses left')
        print('try again\n')

    # final gamewinning check
    if ''.join(string_holder) == ''.join(word):
      i = 10000
      print('Congrats, you guessed the word')
# done

