import random
import openpyxl


# 엑셀 불러오기
fpath = r'C:\Users\COM\Desktop\기타 등등\파이썬 자동화 - 설문지\고등학교 - 에너지고등학교.xlsx'
wb = openpyxl.load_workbook(fpath)

# 엑셀 시트 선택 - 사전 / 사후
before_sheet = wb["사전설문지"]
after_sheet = wb["사후설문지"]


# 함수1 : 학년별로 수정
# sheet는 엑셀 시트를 받아오는 배열인데 any라서 그냥 받아로 수 있나?
def Age(freshman, sophomore, junior, sheet, age, grade):  # age, grade는 열의 문자 범위
    start_row = 4
    age_column = age   # C - 사전 M - 사후
    grade_column = grade  # F - 사전 P

    for i in range(freshman):
        age_cell = sheet[age_column + str(start_row + i)]
        age_cell.value = 17
        grade_cell = sheet[grade_column + str(start_row + i)]
        grade_cell.value = 1

    for i in range(sophomore):
        age_cell = sheet[age_column + str(start_row + freshman + i)]
        age_cell.value = 18
        grade_cell = sheet[grade_column + str(start_row + freshman + i)]
        grade_cell.value = 2

    for i in range(junior):
        age_cell = sheet[age_column +
                         str(start_row + freshman + sophomore + i)]
        age_cell.value = 19
        grade_cell = sheet[grade_column +
                           str(start_row + freshman + sophomore + i)]
        grade_cell.value = 3

    print("나이 수정이 완료되었습니다")
    return sheet


# 함수2 : l~ae열의 정보 생성 - 3,4,5로 생성 / 가끔 2
def data(row_range, sheet, start, end):  # row_range는 전체 인원 수, start와 end는 열의 문자 범위
    start_row = 4   # 4 ~ 1019
    start_column = start    # ord('L')
    end_column = end  # ord('Z') + 5 + 1  # AE의 위치 = Z + 5

    for column in range(start_column, end_column):
        if (column - ord('Z') <= 0):
            column_letter = chr(column)  # L ~ AE

        # Z다음은 AA로***************************
        elif (column - ord('Z') > 0):
            column_letter = 'A' + chr(ord('A') + (column - ord('Z') - 1))
        # print(column_letter)

        for row in range(start_row, row_range + start_row):
            data_cell = sheet[column_letter + str(row)]
            temp = random.randrange(2, 6)
            # 값이 2인 경우 70%로 3~5로 변경
            if temp == 2 and random.randrange(0, 11) <= 7:
                temp = random.randrange(3, 6)
            data_cell.value = temp

    print("내용을 생성하였습니다")
    return sheet


# 메인
freshman = int(input("1학년 : "))
sophomore = int(input("2학년 : "))
junior = int(input("3학년 : "))
# age_before = input("사전 설문지 age 열 : ")
# grade_before = input("사전 설문지 grade 열 : ")
# age_after = input("사후 설문지 age 열 : ")
# grade_after = input("사후 설문지 grade 열 : ")


Total = freshman + sophomore + junior
# 사전 설문지
Before1_sheet = Age(freshman, sophomore, junior, before_sheet, 'C', 'F')
Before2_sheet = data(Total, Before1_sheet, ord('L'), ord('Z') + 5 + 1)

# 사후 설문지 - 범위가 V ~ AO = Z+15
After_sheet = data(Total, after_sheet, ord('B'), ord('K') + 1)
After1_sheet = Age(freshman, sophomore, junior, After_sheet, 'M', 'P')
After2_sheet = data(Total, After1_sheet, ord('V'), ord('Z') + 15 + 1)

# 수정한 엑셀 파일 저장
print("설문지 엑셀 파일을 수정하였습니다")
wb.save(fpath)


# 자동 생성 웹 페이지 만들어서 아무나 사용할 수 있게 (양식이 변경되어도 데이터 생성 범위를 제공받아서 생성할 수 있도록)
