dictionary = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
with open('Input', 'r') as file:
    calibration = file.read()


def word_to_number(text, dictionary):

    words = text.split()
    print(words)
    for i in range(len(words)):
        final = ''
        temporary = ''
        for j in range(len(words[i])):
            if words[i][j].isalpha():
                temporary += words[i][j]
                for key, value in dictionary.items():
                    if key in temporary:
                        number = temporary.replace(key, value)
                        final_number = ''.join(char for char in number if char.isdigit())
                        final += final_number
                        temporary = str(words[i][j])
            elif words[i][j].isdigit():
                final += words[i][j]
                temporary = ''
        words[i] = final
    return words


words = word_to_number(calibration, dictionary)
result = 0

for index, element in enumerate(words):
    new_element = ''.join(char for char in element if char.isdigit())
    if len(new_element) > 2:
        new_element = new_element[0] + new_element[-1]
    elif len(new_element) == 1:
        new_element = new_element[0] + new_element[0]
    words[index] = new_element
    result = result + int(words[index])

print(result)
