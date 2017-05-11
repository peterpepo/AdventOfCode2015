def decimalToAlphabet(sourceString):
    mapping = {i-ord("a"):chr(i) for i in range(ord("a"), ord("z")+1)}

    current = int(sourceString)

    output_string = ""

    while current != 0:
        remainder = current % len(mapping)
        remainder_string = mapping[remainder]

        output_string = remainder_string + output_string

        current = current // len(mapping)

    return output_string


def alphabetToDecimal(sourceString):
    mapping = {chr(i): i-ord("a") for i in range(ord("a"), ord("z") + 1)}
    print(mapping)

    output_number = 0

    for i in range(len(sourceString)-1, -1, -1):
        current_number = mapping[sourceString[i]]
        add_to_total = pow(len(mapping), len(sourceString)-1-i) * current_number
        output_number += add_to_total

    return output_number


def getPaddedPassword(sourceString, length):
    return (length-len(sourceString))*'a'+sourceString


print(alphabetToDecimal("abcdefgh"))  # cf
print(getPaddedPassword(8,decimalToAlphabet("334123303")))
print(decimalToAlphabet(334123304))
