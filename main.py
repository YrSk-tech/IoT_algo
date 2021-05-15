def rabina_karpa_algo(search_pattern, input_text, prime_number, number_of_characters=256):
    pattern_indexes = []
    hash_pattern = 0
    hash_text = 0
    length_text = len(input_text)
    length_pattern = len(search_pattern)

    for i in range(length_pattern):
        hash_pattern = (number_of_characters * hash_pattern + ord(search_pattern[i])) % prime_number
        hash_text = (number_of_characters * hash_text + ord(input_text[i])) % prime_number
    remainder_of_string = length_text - length_pattern

    for i in range(remainder_of_string + 1):
        if hash_pattern == hash_text:
            if str(i) == str(i + len(search_pattern) - 1):
                pattern_indexes.append('Pattern "' + search_pattern + '" found at index ' + str(i))
            else:
                pattern_indexes.append('Pattern "' + search_pattern + '" found at index ' + str(i)
                                       + '-' + str(i + len(search_pattern) - 1))

        if i < remainder_of_string:
            hash_text = (number_of_characters * hash_text - ord(input_text[i]) * pow(number_of_characters,
                                                                                     length_pattern)
                         + ord(input_text[i + length_pattern])) % prime_number
    if not pattern_indexes:
        pattern_indexes = "No patterns in text found"
    return pattern_indexes


if __name__ == '__main__':
    test_prime_number = 997
    with open('rabina_karpa.in', 'r') as input_file:
        text_from_input, pattern_from_input = [line.rstrip() for line in input_file]

    result = rabina_karpa_algo(pattern_from_input, text_from_input, test_prime_number)
    print(result)

    with open('rabina_karpa.out', 'w') as file:
        file.write(str(result))
