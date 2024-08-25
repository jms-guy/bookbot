def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    chars = count_characters(text)
    print(f"{count} words in text")
    print(chars)
    #print(sorting(chars))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered = text.lower()
    characters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    counter = 0
    char_dict = dict.fromkeys(characters, counter)
    for char in lowered:
        if char in char_dict:
            char_dict[char] += 1
    return char_dict

#def sorting(chars):
    



main()