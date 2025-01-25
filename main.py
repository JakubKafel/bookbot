#count word number
def get_num_words(text):
    words = text.split()
    return len(words)

#open text
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count all characters, return dictionary 
def count_characters(text):
    lower_text = text.lower()
    set_text = set(lower_text)
   
    char_count = dict.fromkeys(set_text,0)

    for i in range(len(lower_text)):
        char_count[lower_text[i]] +=1

    return char_count

#list of dictionaries sorting 
def sort_on(dict):
    return dict["num"]

#report printout in target format
def report(text,book_path):

    char_dict = count_characters(text)
    sorted_chars_dict = []
    num_words = get_num_words(text)
    
    #dictionary to list
    for char in char_dict:
        if char.isalpha():
            sorted_chars_dict.append({"char":char,"num":char_dict[char]})

    sorted_chars_dict.sort(reverse=True,key=sort_on)
    
    #report printout
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{num_words} words found in the document\n")
    for char in sorted_chars_dict:
        print(f"The '{char["char"]}' character was found {char["num"]} times")


    print("--- End report --")
    
def main():
    book_path = "/books/frankenstein.txt"
    text = get_book_text(book_path)
    report(text,book_path)

main()