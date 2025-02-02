def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    print(word_count(file_contents))
    print(letter_count(file_contents))
    print(sort(file_contents))


def word_count(text):
     return len(text.split())

def letter_count(text):
    lowercase_text = text.lower()
    count = {}
    for char in lowercase_text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count   

def sort(count):
    character_list = letter_count(count)
    alphabet_list = {}
    for char in character_list:
        if char.isalpha():
            alphabet_list[char] = character_list[char]
    sorted_alphabet = dict(sorted(alphabet_list.items()))
    return sorted_alphabet

main()
