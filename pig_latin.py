#initial for loop
vowels = ['a', 'e', 'i', 'o', 'u']
# get_ string
word = input('What do you want to translate: ')

#holds the chars for translated list need to convert backn


# this function should in general:
# 1. turn string into list
# 2. pop the first letter of the string and then
# 3. extend it to the end of the 'list'

# this function will return thd translated_word as a list
def first_letter_check(check):
  word_list = word.split(' ')
  translated_word = ''
  # iterate through eatch string in the word_list list
  for string in word_list:
    translated_word += ' '.join(loopstring(string))
    
    # every first instance of a vowel
    # new_sentence.append()
  return translated_word


# function for looping through string
def loopstring (string):
  counter = 0
  new_string = []
  # loop abd check every char in the string
  for counter in range(len(string)):
    # if counter0 returns true, first letter is in vowels, if not will iterate through string to find first vowel
    if string[counter] in vowels:
      new_string.append(f'{string[counter :len(string)]}{string[0:counter]}ay ')
      return new_string
  # print(new_string)
    # counts up one to look for next vowel

  counter += 1



print(f'Translated sentence:{first_letter_check(word)}')
# translated_word = ' '.join(first_letter_check(word))

