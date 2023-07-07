def create_files(filename):
    large_words = "./files/large-words.txt"
    small_words = "./files/small-words.txt"

    word_count = {}
    unique_words = set()

    with open(filename, "r") as in_stream:
        for line in in_stream:
            words = line.strip().split() # Split the line into words
            
            for word in words:
                unique_words.add(word)  # Add word to the set of unique words

                if len(word) >= 3:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

    # Write large words to large-words.txt
    with open(large_words, "w") as large_file:
        for word in unique_words:
            if len(word) >= 3:
                large_file.write(word + "\n")

    # Write small words to small-words.txt
    with open(small_words, "w") as small_file:
        for word in unique_words:
            if len(word) < 3:
                small_file.write(word + "\n")

    return len(unique_words)


def ex3():
    total_words = create_files("./files/words.txt")
    print(f"Total words: {total_words}.")

ex3()