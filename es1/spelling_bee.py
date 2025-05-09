def score_word(word, available):
    """
    Compute the score for an acceptable word

	word : word to be scored
	available : string of the available letters
    
    >>> score_word('card', 'ACDLORT')
    1
    >>> score_word('color', 'ACDLORT')
    5
    >>> score_word('cartload', 'ACDLORT')
    15
    """
    length=len(word)
    if length == 4:
        return 1
    if length > 4:
        if uses_all(word,available.lower()):
            return length+7
        else:
            return length

def check_word(word, available, required):
    """
    Check whether a word is acceptable

	word : word to check
	available : string of seven available letters
	required : string of the single required letter
    
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) < 4:
        return False

    if (uses_only(word,available.lower()) and uses_all(word,required.lower())):
        return True
    return False


def uses_all(word, required):
    """
    Check whether a word uses all the required letters

	word : word to be checked
	required: string of the required letter

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_only(word, available):
    """
    Checks whether a word uses only the available letters

	word : word to be checked
	available : string of the available letters
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    
    for letter in word:
        if letter not in available:
            return False
    return True

def main():
    f=open("words.txt","r")
    total_score=0
    for word in f:
        clean_word=word.strip()
        if check_word(clean_word,'ACDLORT','R'):
            score=score_word(clean_word,"ACDLORT")
            total_score+=score
            print(f'{clean_word} {score}')
    print(f'Total score {total_score}')
        
if __name__ == "__main__":
    main()

