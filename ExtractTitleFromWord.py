def get_word_list(file_name):
    """Extract titles from the word list
    :param file_name: The input .txt file.
    :return: A word list with titles
    """
    # Read data from file
    word_list = []
    word_set = set()
    file = open(file_name, 'r')
    data = file.read()
    file.close()

    # Process
    data_len = len(data)
    letter_idx = 0
    temp_word = ""
    flag_in_quotes = False
    while letter_idx < data_len:
        if data[letter_idx] == "《" and flag_in_quotes:
            return ["Error: invalid < in data."]
        elif data[letter_idx] == "《" and not flag_in_quotes:
            flag_in_quotes = True
            temp_word = ""
        elif data[letter_idx] == "》" and flag_in_quotes:
            flag_in_quotes = False
            temp_word = temp_word.replace("<", "《")
            temp_word = temp_word.replace(">", "》")
            word_list.append(temp_word)
            word_set.add(temp_word)
            temp_word = ""
        elif data[letter_idx] == "》" and not flag_in_quotes:
            return ["Error: invalid > in data."]
        elif flag_in_quotes:
            temp_word += data[letter_idx]
        letter_idx += 1

    return list(word_set)

get_word_list("test.txt")
