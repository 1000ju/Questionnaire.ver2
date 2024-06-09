import random


def Data(row_range, sheet, start, end):  # row_range는 전체 인원 수, start와 end는 열의 문자 범위
    start_row = 4
    start_column = start
    end_column = end

    for column in range(start_column, end_column + 1):  # 마지막 반복문의 종료 범위가 맞는지 확인************
        if (column - ord('Z') <= 0):
            column_letter = chr(column)  # L ~ AE

        elif (column - ord('Z') > 0):
            column_letter = 'A' + chr(ord('A') + (column - ord('Z') - 1))

        for row in range(start_row, row_range + start_row):
            data_cell = sheet[column_letter + str(row)]
            temp = random.randrange(2, 6)
            # 값이 2인 경우 70%로 3~5로 변경
            if temp == 2 and random.randrange(0, 11) <= 7:
                temp = random.randrange(3, 6)
            data_cell.value = temp

    print("내용을 생성하였습니다")
    return sheet


def major():
    start_row = 4
