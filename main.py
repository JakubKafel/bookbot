def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    lower_text = text.lower()
    set_text = set(lower_text)
   
    char_count = dict.fromkeys(set_text,0)

    for i in range(len(lower_text)):
        char_count[lower_text[i]] +=1

    return char_count

def sort_on(dict):
    return dict["num"]

def report(text,book_path):

    char_dict = count_characters(text)
    sorted_chars_dict = []
    num_words = get_num_words(text)
    for char in char_dict:
        if char.isalpha():
            sorted_chars_dict.append({"char":char,"num":char_dict[char]})

    sorted_chars_dict.sort(reverse=True,key=sort_on)
    

    print(f"--- Begin report of {book_path} ---\n")
    print(f"{num_words} words found in the document\n")
    for char in sorted_chars_dict:
        print(f"The '{char["char"]}' character was found {char["num"]} times")


    print("--- End report --")
    
def main():
    book_path = "/root/workspace/github.com/JakubKafel/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    #num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    #charater_dictionary = count_characters(text)
    #print(charater_dictionary)

    report(text,book_path)

main()