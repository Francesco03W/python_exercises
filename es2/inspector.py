def clean_book(source_filename, destination_filename):
    """
    Remove everything except the book itself. Return the number of lines of the cleaned book

    source_filename : where to find the book to be cleaned
    destination_filename : where to store the cleaned book

    >>> clean_book("stevenson.txt", "stevenson_clean.txt")
    2530
    """
    f_input=open(source_filename)
    f_output=open(destination_filename,'w')


    header=True # in intestazione
    # tail=False non è necessario, ritorno appena trovo quella linea.
    lines_written=0
    for line in f_input:
        if header == True: #-1 è l'indice dell'ultimo elemento della stringa, ossia il carattere newline \n
            if line[:-1] == "*** START OF THIS PROJECT GUTENBERG EBOOK THE STRANGE CASE OF DR. ***":
                header=False
        else:
            if line[:-1] == "*** END OF THIS PROJECT GUTENBERG EBOOK THE STRANGE CASE OF DR. ***":
                return lines_written
            else:
                f_output.write(line)
                lines_written+=1
    f_input.close()
    f_output.close()

# Devo fare controllo case sensitive?
def count_unique_words(filename):
    """
    Count the number of unique words in a file

    filename : path to a file

    >>> count_unique_words("stevenson_clean.txt")
    6039
    """
    unique_words=[]
    f_input=open(filename)
    for line in f_input:
        words_line=[] #contiene le parole della singola linea    
        #rimuovo il carattere newline che potrebbe creare nuove parole
        line_clean=line[:-1]
        words_line=line_clean.split()
        for word in words_line:
            #attenzione, words_line è una lista, nel nostro caso ogni elemento è str
            if word not in unique_words:
                unique_words.append(word)
    return len(unique_words)



if __name__ == "__main__":
    import doctest
doctest.testmod()