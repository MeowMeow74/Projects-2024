
def scrabble_score_count():
  word = input('Enter word to get it\'s score: ')

  new_list = word.split(' ')


  score_keep = []

  scrabble_score_key = {
  "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
  "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
  "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10 };

  for each_word in new_list:
    # this iterates for each word in the input
    score = 0
    for letter in each_word.upper():
      # this iterates for each letter in the word

      for dict_pos in scrabble_score_key:
        # this checks each score and keeps count

        if letter == dict_pos:
          score += scrabble_score_key[dict_pos]

    score_keep.append({'word': each_word, 'score': score})
  return score_keep




scrabble_score_count()