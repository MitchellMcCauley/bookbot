def word_counter(file_contents):
    words_list = file_contents.split()
    word_count = len(words_list)
    return word_count

def letter_counter(file_contents):
    letter_counts = {}

    for letter in file_contents:
        letter = letter.lower()  # normalize everything to lowercase

        if letter.isalpha():  # only count actual letters, ignore spaces/punctuation
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    return letter_counts

def sort_on(dict):
    return dict["num"]

def sort_letter_dicts(letter_counts):
    letter_list = []  # Start with an empty list.
    
    # Loop through each letter and its count in the letter_counts dictionary.
    for char, count in letter_counts.items():
        # Only include alphabetical characters.
        if char.isalpha():
            # Append a new dictionary for each letter.
            letter_list.append({"char": char, "num": count})
    
    # Sort the list in descending order based on the "num" value.
    letter_list.sort(reverse=True, key=sort_on)
    
    return letter_list