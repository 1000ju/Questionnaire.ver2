import random
import openpyxl

# 다만 이 함수에서 아쉬운 점은 wb코드가 매번 중복되는 것을 최소화하고 싶다
# => wb코드 중복이라하면, 매번 업데이트마다 fpath로 새로이 접근하는 것을 의미
# => 완성한 지금, 사전, 사후 업데이트마다 새로이 여는게 충돌 없이 원활하게 작동할 것 같다


def Data(Total, fpath, start_column, end_column, BeforeAfter):
    start_row = 4
    wb = openpyxl.load_workbook(fpath)
    if BeforeAfter == "Before":
        xl_sheet = wb["사전설문지"]
    elif BeforeAfter == "After":
        xl_sheet = wb["사후설문지"]

    # end_column+1해줘야 end_column까지 계산한다
    for column in range(start_column, end_column + 1):

        for row in range(start_row, Total + start_row):

            temp = random.randrange(1, 6)
            # 값이 1,2인 경우 70%로 3~5로 변경******************
            if temp <= 2 and random.randrange(0, 11) <= 7:
                temp = random.randrange(3, 6)
            xl_sheet.cell(row=row, column=column, value=temp)

    print("데이터 내용을 생성하였습니다")
    wb.save(fpath)
    return


# 사전, 사후 설문지에 데이터를 넣어야한다.
# TotalData 함수에 모든 범위, 총인원, fpath 데이터 생성에 필요한 모든 값을 가져와서 Data함수를 이용하여 계산
def TotalData(Total, fpath, b_start, b_end, a_start01, a_end01, a_start02, a_end02):
    # 사전 설문지
    Data(Total, fpath, b_start, b_end, "Before")

    # 사후 설문지
    Data(Total, fpath, a_start01, a_end01, "After")
    Data(Total, fpath, a_start02, a_end02, "After")
    return
