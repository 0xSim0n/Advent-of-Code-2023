with open('Input', 'r') as file:
    calibration = file.read()

split_calibration = calibration.split()
result = 0

for index, element in enumerate(split_calibration):
    new_element = ''.join(char for char in element if char.isdigit())
    if len(new_element) > 2:
        new_element = new_element[0] + new_element[-1]
    elif len(new_element) == 1:
        new_element = new_element[0] + new_element[0]
    split_calibration[index] = new_element
    result = result + int(split_calibration[index])

print(result)
