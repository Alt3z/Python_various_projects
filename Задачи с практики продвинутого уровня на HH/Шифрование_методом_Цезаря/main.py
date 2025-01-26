def encode_string(string: str, shift: int) -> str:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = []
    n = len(alphabet)

    for char in string:
        if char == " ":
            result.append(" ")
        else:
            idx = alphabet.index(char)
            new_idx = (idx + shift) % n
            result.append(alphabet[new_idx])

    return "".join(result)


input_string = input()
shift = int(input())

encoded_string = encode_string(input_string, shift)
print(encoded_string)
