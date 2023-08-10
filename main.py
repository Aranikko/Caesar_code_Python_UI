user_input = input("Enter the text: ")
output = []

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

upper_user_input = user_input.upper()
list_user_input = list(upper_user_input)

# Обработка сдвига
shift = int(input("Enter shift: "))

for ui in range(len(list_user_input)):
    if list_user_input[ui] in alphabet:
        index = alphabet.index(list_user_input[ui])
        shifted_index = (index + shift) % len(alphabet)
        output.append(alphabet[shifted_index])
    else:
        output.append(list_user_input[ui])

result = ''.join(output)
print("encrypted text:", result)