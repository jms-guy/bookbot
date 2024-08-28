def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    chars = count_characters(text)
    chars_sorted_list = dict_to_sorted_list(chars)
    
    print(f"--- Being report of {book_path} ---")
    print(f"{count} words found in the document")
    print()
    for i in chars_sorted_list:
        if not i["char"].isalpha():
            continue
        print(f"The '{i['char']}' character was found {i['num']} times.")

    print("End report.")
    
def sort_on(n):
    return n["num"]

def dict_to_sorted_list(chars):
    sorted_list = []
    for ch in chars:
        sorted_list.append({"char": ch, "num": chars[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered = text.lower()
    characters = ("'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'")
    counter = 0
    char_dict = dict.fromkeys(characters, counter)
    for char in lowered:
        if char in char_dict:
            char_dict[char] += 1
    return char_dict

#def sorting(chars):
    



main()