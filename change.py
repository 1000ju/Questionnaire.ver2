# A ~ AF등 2자리가 넘는 문자 열 범위를 계산

def change(alphabet):

    if len(alphabet) == 2:
        cut_alphabet = alphabet[1]  # AF에서 F를 의미
        # change('Z')를 쓴 이유는 Z의 알파뱃 순번이 필요한데 이미 단일 알파벳에 대한 계산 기능은 구현해두었기 때문에 해당 기능을 사용하는 것임
        column = ord(cut_alphabet) - ord('A') + 1 + change('Z')
        # print(cut_alphabet)

    elif len(alphabet) == 1:
        column = ord(alphabet) - ord('A') + 1

    return column

# alphabet = 'C'
# column = ord(alphabet) - ord('A')
# print(column)
