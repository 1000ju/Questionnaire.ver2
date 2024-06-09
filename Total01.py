import openpyxl
import PracticeAge
import data
import cut

# 엑셀 불러오기
fpath = r'C:\Users\COM\Desktop\기타 등등\파이썬 자동화 - 설문지\대학교 - 울산과학대 서부.xlsx'
wb = openpyxl.load_workbook(fpath)

# # 엑셀 시트 선택 - 사전 / 사후
# before_sheet = wb["사전설문지"]
# after_sheet = wb["사후설문지"]


# 메인
Total = int(input("전체 인원 수 : "))
# 사전 설문지 문자열 범위x
b_gender = 'B'
b_age = 'C'
b_grade = 'F'
b_major = 'G'

# 사후 설문지 문자열 범위
a_gender = ' L'
a_age = 'M'
a_grade = 'P'
a_major = 'Q'
# ---------------------------------------------------------------------ok

# 사전 + 사후 나이
# pratice 함수에 저장되어 있는걸 가져온것이니 수정 필요 ***************
# 대학생은 학년별 인원 수가 정해진 것이 아니라 total만 있으면 만들 수 있음
sheet_result = PracticeAge.College_Age(
    Total, wb, b_gender, b_age, b_grade, b_major, a_gender, a_age, a_grade, a_major)
Before1_sheet = sheet_result["사전설문지"]
After1_sheet = sheet_result["사후설문지"]

# # 사전 설문지
# Before2_sheet = data.Data(Total, Before1_sheet,
#                           cut.str_slice('M'), cut.str_slice('AF'))

# # 사후 설문지
# After_sheet = data.Data(Total, After1_sheet,
#                         cut.str_slice('B'), cut.str_slice('K'))
# After2_sheet = data.Data(Total, After1_sheet, cut.str_slice(
#     'W'), cut.str_slice('AP'))  # After1_sheet가 아니라 After2_sheet가 되어야하는거 아닌가?

# 수정한 엑셀 파일 저장
print("설문지 엑셀 파일을 수정하였습니다")
sheet_result.save(fpath)
# wb.save(fpath)


# Before1_sheet = age.College_Age(Total, before_sheet, 'C', 'F', 'G')
# After1_sheet = age.College_Age(Total, After_sheet, 'M', 'P', 'Q')
