#differenza tra uses_all e uses_only:
#uses_all: controllo se una parola usa TUTTE le lettere disponibili.
#uses_only: controllo se una parola usa SOLO le lettere disponibili (e nessune altre)

def uses_all(word,required):
    """
    Check whether a word uses all the required letters

	word : word to be checked
	required: string of the required letter 
    
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    
    for required_letter in required.lower():
        if required_letter not in word.lower():
                return False
    return True

def uses_only(word,available):
    """
    Checks whether a word uses only the available letters

	word : word to be checked
	available : string of the available letters
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    for letter in word.lower():
        if letter not in available.lower():
            return False
    return True


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

    if len(word)<4:
        return False
    
    # si può scrivere usando if .... in ....
    return( uses_all(word,required) and uses_only(word,available))


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
    l=len(word)
    if l < 4:
        return 0
    if l > 4:
        if uses_all(word,available):
            return l + 7
        else:
            return l
    return 1

#problema: line include il \n!

#piuttosto che ragionare con gli indici c'è metodo str.strip che ritorna la stringa senza carattere capo e coda definiti in argomento
#utile per togliere newline
#https://docs.python.org/3.4/library/stdtypes.html
def spelling_bee():
    total_score=0
    for line in open("words.txt"):
        word=line[:len(line)-1] #ricorda che l'estremo superiore è escluso -> meglio word=line.split() se c'è solo 1 parola per riga
        word_score=0

        if check_word(word,'ACDLORT','R'):
            word_score=score_word(word,'ACDLORT')
            print(word,word_score)
            total_score+=word_score
    print("Total score:",total_score)

if __name__ == "__main__":
	spelling_bee()
    



