import random
import string

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letters = []
    letters_counter = {}
    while len(letters) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        if letters_counter.get(random_letter) and letters_counter.get(random_letter) >= LETTER_POOL[random_letter]:
            continue
        else:
            letters.append(random_letter)
            if letters_counter.get(random_letter):
                letters_counter[random_letter] += 1
            else:
                letters_counter[random_letter] = 1
    return letters

def uses_available_letters(word, letter_bank):
    for letter in word:
        if word.count(letter) > letter_bank.count(letter):
            return False
    return True

        

def score_word(word):
    letter_score = {
        ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
        ("D", "G"): 2,
        ("B", "C", "M", "P"): 3,
        ("F", "H","V","W", "Y"): 4,
        ("K",):5,
        ("J", "X"): 8,
        ("Q", "Z"): 10,
    }
    score = 0
    for letter in word.upper():
        for key in letter_score:
            if letter in key:
                score += letter_score.get(key)
    if 7<= len(word) <= 10:
        score += 8
    return score
    

def get_highest_word_score(word_list):
    word_score = {}
    for word in word_list:
        word_score[word] = score_word(word)
    max_score = max(list(word_score.values()))
    winners = []
    for key, value in word_score.items():
        if value == max_score:
            winners.append((key, value))
    min_value = len(winners[0][0])
    for item in winners:
        min_value = min(min_value, len(item[0]))
    winner = None
    for item in winners:
        if len(item[0]) == 10:
            return item
        elif len(item[0]) == min_value:
            winner = item
    return winner