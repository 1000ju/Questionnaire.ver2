from tkinter import Tk, Entry, Button
from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용하겠다.
root = Tk()                      # root라는 창을 생성
root.geometry("400x400")       # 창 크기설정
root.title("학교 양식을 선택하십시오")    # 창 제목설정
root.option_add("*Font", "맑은고딕 15")  # 폰트설정
root.resizable(False, False)  # x, y 창 크기 변경 불가
entry_value = []
school = 0


def get_entry_value(entry_list):

    for entry in entry_list:
        value = entry.get()
        # print("EnterInput Entry value : " + value)
        entry_value.append(value)

    return


def btn2press(Radio_value, Radio_value1):                   # 함수 btn2press() 정의   / widget 부품
    root.destroy()
    global school  # 전역변수를 함수에서 쓰기위해서 필요 *****************************
    if Radio_value.get() == 1:         # 각 양식 별 입력 데이터를 제시
        school = 1
        root2 = Tk()
        root2.title("대학교 양식 입력창")
        root2.geometry('480x300')

        Total_lebel = Label(root2, text='총인원 ')
        Total_Entry = Entry(root2)
        xlcel_lebel = Label(root2, text='엑셀 파일주소 ')
        xlcel_Entry = Entry(root2)
        warning_lebel1 = Label(root2, text='파일주소의 쌍따옴표를 제거하고 입력해주십시오.')

        Total_lebel.grid(row=0, column=0, padx=10, pady=10)
        Total_Entry.grid(row=0, column=1, padx=10, pady=10)
        xlcel_lebel.grid(row=1, column=0, padx=10, pady=10)
        xlcel_Entry.grid(row=1, column=1, padx=10, pady=10)
        warning_lebel1.grid(row=2, column=1, padx=10, pady=10)
        # 정확한 위치를 설정해주는 이유는
        # pack같은 단순한 방법은 단일 방향으로만 상하, 좌우 각각으로만 붙일 수 있음
        # 원하는 위치에 원하는 위젯?을 두기 위해선
        # 정확한 좌표로 지정해주는 것이 편했음
        # grid, palce 처럼 위젯 제어가 있는 기능이 복잡한 레이아웃에서는 편리함

        entry_widgets = []  # ************
        entry_widgets.append(Total_Entry)
        entry_widgets.append(xlcel_Entry)
        # 두 번째 상세 데이터 제출 버튼
        ButtonCollege = Button(root2, text="제출", width=10, command=lambda: (
            get_entry_value(entry_widgets), root2.destroy()))
        # lamda를 사용하면 두 개의 command를 사용할 수 있는걸 알게되었다. 왜인진 아직 모르겠다
        ButtonCollege.grid(row=3, column=1)

    if Radio_value1.get() == 2:
        school = 2
        root3 = Tk()
        root3.title("중/고등학교 양식 입력창")
        root3.geometry('480x300')

        Freshman_lebel = Label(root3, text='1학년 ')  # 라벨 이름
        Sophomore_lebel = Label(root3, text='2학년 ')
        Junior_lebel = Label(root3, text='3학년 ')
        Freshman_Entry = Entry(root3)     # 라벨 옆 입력칸
        Sophomore_Entry = Entry(root3)
        Junior_Entry = Entry(root3)
        xlcel_lebel = Label(root3, text='엑셀 파일주소 ')
        xlcel_Entry = Entry(root3)
        warning_lebel1 = Label(root3, text='파일주소의 쌍따옴표를 제거하고 입력해주십시오.')

        Freshman_lebel.grid(row=0, column=0, padx=10, pady=10)
        Freshman_Entry.grid(row=0, column=1, padx=10, pady=10)
        Sophomore_lebel.grid(row=1, column=0, padx=10, pady=10)
        Sophomore_Entry.grid(row=1, column=1, padx=10, pady=10)
        Junior_lebel.grid(row=2, column=0, padx=10, pady=10)
        Junior_Entry.grid(row=2, column=1, padx=10, pady=10)
        xlcel_lebel.grid(row=3, column=0, padx=10, pady=10)
        xlcel_Entry.grid(row=3, column=1, padx=10, pady=10)
        warning_lebel1.grid(row=4, column=1, padx=10, pady=10)

        entry_widgets = []  # ************ 엔트리에서 입력받으니까 엔트리 값만 append
        entry_widgets.append(Freshman_Entry)
        entry_widgets.append(Sophomore_Entry)
        entry_widgets.append(Junior_Entry)
        entry_widgets.append(xlcel_Entry)
        # 두 번째 상세 데이터 제출 버튼
        ButtonCollege = Button(root3, text="제출", width=10, command=lambda: (
            get_entry_value(entry_widgets), root3.destroy()))
        # lamda를 사용하면 두 개의 command를 사용할 수 있는걸 알게되었다. 왜인진 아직 모르겠다
        ButtonCollege.grid(row=5, column=1)

    return


def start_input():

    Radio_value = IntVar()                             # chkvar에 int 형으로 값을 저장
    RadioBox = Radiobutton(
        root, text="대학교", variable=Radio_value, value=1)   # root라는 창에 체크박스 생성
    RadioBox.pack()                                 # 체크박스 배치

    Radio_value1 = IntVar()                            # Radio_value1에 int 형으로 값을 저장
    RadioBox1 = Radiobutton(
        root, text="중/고등학교", variable=Radio_value1, value=2)  # root라는 창에 체크박스 생성
    RadioBox1.pack()                                # 체크박스 배치

    btn2 = Button(root, text="선택", width=10, command=lambda: (
        btn2press(Radio_value, Radio_value1)))  # 버튼을 누르면, (값 2개를 보내서) bnt2press함수 작동
    btn2.pack()                        # 버튼 배치

    root.mainloop()                  # 창 실행
    return


# 입력 결과 list를 class로 만들어서
# class에 저장한 값을 가져올 수 있음
class global_value:
    def __init__(self):
        self.value = entry_value
        self.school = school


# 메인 모듈에서 사용하려면 리스트에 저장된 엔트리 값들이 양식별로 조금 다르다
# 그렇기 때문에 각각의 양식에 맞게 리스트에서 데이터를 순서대로 추출한다
# 대학생 - 총인원, 파일주소
# 중고등학생 - 1학년, 2학년, 3학년, 파일주소
