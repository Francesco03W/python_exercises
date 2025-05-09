def clean_book(source_filename, destination_filename):
    """
    Remove everything except the book itself. Return the number of lines of the cleaned book

    source_filename : where to find the book to be cleaned
    destination_filename : where to store the cleaned book

    >>> clean_book("stevenson.txt", "stevenson_clean.txt")
    2530
    """
    f_input=open(source_filename,'r')
    f_output=open(destination_filename,'w')
    cleaning=False
    lines=0

    header="*** START OF THIS PROJECT GUTENBERG EBOOK THE STRANGE CASE OF DR. ***"
    footer="*** END OF THIS PROJECT GUTENBERG EBOOK THE STRANGE CASE OF DR. ***"

    for line in f_input: 
        clean_line=line.strip()
        if cleaning == True:
            if clean_line == footer:
                f_input.close()
                f_output.close()
                return lines
            f_output.write(line)
            lines+=1
        else:
            if clean_line == header:
                cleaning = True
    return 0 #se non trova mai header

def count_unique_words(filename):
    """
    Count the number of unique words in a file

    filename : path to a file

    >>> count_unique_words("stevenson_clean.txt")
    6039
    """
    f=open(filename,'r')
    unique_words = []
    for line in f:
        clean_line=line.strip()
        words_line=clean_line.split()
        for word in words_line:
            if word not in unique_words:
                unique_words.append(word)
    return len(unique_words)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
