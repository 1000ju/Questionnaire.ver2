# from range import college_range 대학생 양식 문자 범위 불러오기
# college_range = college_range() 객체 생성
# print(college_range.b_start)  객체로 해당 정보에 접근해서 사용
# 핵심은 클래스로 해당 값을 관리한다
import change


class college_range:
    def __init__(self):
        # 사전 설문지 문자열 범위x
        self.b_gender = change.change('B')
        self.b_age = change.change('C')
        self.b_grade = change.change('F')
        self.b_major = change.change('G')
        # 사후 설문지 문자열 범위
        self.a_gender = change.change('L')
        self.a_age = change.change('M')
        self.a_grade = change.change('P')
        self.a_major = change.change('Q')

        # 데이터 생성 범위
        self.b_start = change.change('M')
        self.b_end = change.change('V')
        self.a_start01 = change.change('B')
        self.a_end01 = change.change('K')
        self.a_start02 = change.change('W')
        self.a_end02 = change.change('AF')


class highschool_range:
    def __init__(self):
        # 사전 설문지 문자열 범위x
        self.b_gender = change.change('B')
        self.b_age = change.change('C')
        self.b_grade = change.change('F')

        # 사후 설문지 문자열 범위
        self.a_gender = change.change('L')
        self.a_age = change.change('M')
        self.a_grade = change.change('P')

        # 데이터 생성 범위
        self.b_start = change.change('L')
        self.b_end = change.change('U')
        self.a_start01 = change.change('B')
        self.a_end01 = change.change('K')
        self.a_start02 = change.change('V')
        self.a_end02 = change.change('AE')
