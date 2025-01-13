def main():
    book_path= "books/frankenstein.txt"
    text = get_book_text(book_path)
    count= get_word_count(text)
    letter= get_letter_count(text)
    print(letter)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(book):
    words = book.split()
    i=0
    for word in words:
        i+=1
    
    return i

def get_letter_count(text):
    words = text.split()
    count = {}
    for word in words:
        letters= word.lower()
        for letter in letters:
            value= count.get(letter, 0)
            value+=1
            count[letter]=value
    
    return count


main()
