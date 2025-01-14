def main():
    book_path= "books/frankenstein.txt"
    text = get_book_text(book_path)
    count= get_word_count(text)
    letters= get_letter_count(text)
    alpha= get_alphabet(letters)
    get_report(alpha,count)


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

def get_alphabet(letter_count):
   letters=letter_count
   report= {}
   for letter in letters:
        if letter.isalpha()== True:
            report[letter] = letters[letter]
   return report

def get_report(dict,word):
    letters=dict
    print("--- Begin report of books/frankenstein.txt ---")
    print(word," words found in the document")
    print(" ")
    for letter in letters:
        print("the '",letter,"' character was found ",letters[letter]," times")
    
    return
    

main()
