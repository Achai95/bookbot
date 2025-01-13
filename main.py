def main():
    book_path= "books/frankenstein.txt"
    text = get_book_text(book_path)
    count= get_word_count(text)
    print(count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(book):
    words = book.split()
    i=0
    for word in words:
        i+=1
    
    return i


main()
