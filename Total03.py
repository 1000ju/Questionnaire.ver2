# 고등학교 + 대학교 양식 / 최적화
import easygui
import AgeTest01
import DataTest01
from range import college_range
from range import highschool_range
import EnterInput
from EnterInput import global_value
# 입력 결과 list를 class로 만들어서
# class에 저장한 값을 가져올 수 있음
EnterInput.start_input()  # 실행
student_value = global_value()  # class -> 입력값 가져오려고
value_list = student_value.value

if student_value.school == 1:  # 대학교
    student = college_range()
    Total = int(value_list.pop(0))
    xlsx_fpath = value_list.pop(0)
    print("Total ", Total)
    print("fpath ", xlsx_fpath)
elif student_value.school == 2:  # 고등학교
    student = highschool_range()
    freshman = int(value_list.pop(0))
    sophomore = int(value_list.pop(0))
    junior = int(value_list.pop(0))
    Total = freshman + sophomore + junior
    xlsx_fpath = value_list.pop(0)
    print("freshman ", freshman)
    print("sophomore ", sophomore)
    print("junior ", junior)
    print("Total ", Total)
    print("fpath ", xlsx_fpath)

# 엑셀 불러오기
fpath = r'{}'.format(xlsx_fpath)
# fpath = r'C:\Users\COM\Desktop\기타 등등\파이썬 자동화 - 설문지\고등학교 - 울산 공고.xlsx'


# 상단의 if문에 추가해서 축약할 수 있지만 기능 구현은 따로 분리해두는 것이 가독성에 좋을 것 같아 분리했다.
if student_value.school == 1:  # 대학교
    AgeTest01.College_Age(
        Total, fpath, student.b_gender,
        student.b_age, student.b_grade, student.b_major,
        student.a_gender, student.a_age, student.a_grade,
        student.a_major)
elif student_value.school == 2:  # 고등학교
    AgeTest01.Highschool_Age(Total, freshman, sophomore, junior, fpath,
                             student.b_gender, student.b_age, student.b_grade,
                             student.a_gender, student.a_age, student.a_grade)


# fpath 사용 -> age, data 모듈을 사용한 후 저장하는 과정이 필요. 즉, 업데이트마다 fpath로 접근해야함
# 더 좋은 방식이 있으면 적용. 현재는 fpath를 이용
DataTest01.TotalData(Total, fpath, student.b_start, student.b_end,
                     student.a_start01, student.a_end01, student.a_start02, student.a_end02)


print("모든 작업을 완료하였습니다. 파일을 열어 확인해보시길바랍니다")
